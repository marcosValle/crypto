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

if __name__ == "__main__":
    with open("7.txt") as f:
        ct = binascii.a2b_base64(f.read())
    key = b"YELLOW SUBMARINE"
    print(ct)
    print(aesDecECB(ct, key))
