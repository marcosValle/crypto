import binascii

m1 = b'attack at dawn' #use bytes instead of str
m2 = b'attack at dusk'

c1 = '6c73d5240a948c86981bc294814d'

#c1 = m1 xor k ==> k = m1 xor c1

# m1: bytes -> hex -> int
# c1: hexStr -> int
key = int(binascii.hexlify(m1),16) ^ int(c1,16)
key = '0'+'{:x}'.format(key)

c2 = int(binascii.hexlify(m2),16) ^ int(binascii.hexlify(bytes.fromhex(key)),16)
c2 = '{:x}'.format(c2)
print(c2)

