from Crypto.Cipher import AES
import binascii

with open('dist/flag.txt.enc','rb') as f:
    key = binascii.unhexlify('b5082f02fd0b6a06203e0a9ffb8d7613dd7639a67302fc1f357990c49a6541f3')
    data = f.read()
    iv = data[:AES.block_size]

    data = data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CFB, iv)

    print(cipher.decrypt(data))