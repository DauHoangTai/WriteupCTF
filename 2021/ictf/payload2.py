from Crypto.Util.Padding import pad, unpad
first_cookie = bytes.fromhex("24b7271315c8809ae34019e428ba060d97ce0f33928437ca7f6fb2d201ac67fa7d9cee7f00dac9c9")
# print(first_cookie )
cookie_admin = (first_cookie[:8] + bxor(first_cookie[8:], pad(b"ImaginaryCTFUser", 16), pad(b"admin", 16))).hex()
print(cookie_admin)