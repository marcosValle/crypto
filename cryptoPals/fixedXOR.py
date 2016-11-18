import binascii

def fixedXOR(h1, h2):
    b1= binascii.unhexlify(h1)
    b2= binascii.unhexlify(h2)

#    return "".join("{:02x}".format(a^b) for a,b in zip(b1,b2))
    return "".join(hex(a^b)[2:] for a,b in zip(b1,b2))


h1 = '1c0111001f010100061a024b53535009181c'
h2 = '686974207468652062756c6c277320657965'

print(fixedXOR(h1, h2))
