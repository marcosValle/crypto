# PoC of DES exhaustive search attack

from Crypto.Cipher import DES
#from Crypto import Random

def enc(key, plaintext):
    #iv = Random.new().read(DES.block_size)
    cipher = DES.new(key, DES.MODE_ECB)
    msg = cipher.encrypt(plaintext)
    return msg

def dec(key, ct):
    cipher = DES.new(key, DES.MODE_ECB)
    pt = cipher.decrypt(ct)
    return pt

def attack(ct, pt):
    key = 0x0
    while(key<=0xFFFFFFFFFFFFFF):
        cipher = DES.new(key.to_bytes(8, byteorder='big'), DES.MODE_ECB)
        if cipher.decrypt(ct) == pt:
            return key
        key += 1
    return False


key = b'\x00\x00\x00\x00\x00\x00\x00\x12' #key=123
pt = b'sona si latine loqueris '

ct = enc(key, pt)
print("PT: {}".format(pt))
print("CT: {}".format(ct))
print("test: ".format(dec(key, ct)))
print("Decrypted key: {}".format(attack(ct, pt)))

