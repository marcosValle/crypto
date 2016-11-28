from Crypto.Cipher import AES
import binascii

with open("7.txt") as f:
    ct = binascii.a2b_base64(f.read())

key = "YELLOW SUBMARINE"
aes = AES.new(key, AES.MODE_ECB)

pt = aes.decrypt(ct)
print(pt.decode('utf-8'))
