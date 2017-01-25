from Crypto.Cipher import AES
import binascii

def aesDecECB(ct, key):
    aes = AES.new(key, AES.MODE_ECB)
    pt = aes.decrypt(ct)
    return pt

def aesEncECB(pt, key):
    aes = AES.new(key, AES.MODE_ECB)
    ct = aes.encrypt(pt)
    return ct

with open("7.txt") as f:
    ct = binascii.a2b_base64(f.read())

if __name__ == "__main__":
    key = "YELLOW SUBMARINE"
    print(aesDecECB(ct, key))
