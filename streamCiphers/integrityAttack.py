# Example of 'MALLEABILITY' property of stream ciphers, i.e., they do not provide integrity.
# In this case Alice sends the message '100' to Bob, but Mallory intercepts the ciphertext and manipulate it, so when Bob decrypts it, he gets the message '900'.

m = "100"
k = "Don't panic"

def xor(a, b):
    return "".join(chr(ord(x)^ord(y)) for x,y in zip(a,b))

#make 100 become 900
def attack(ct, change):
    mod = xor(change,'1') + xor('0', '0') + xor('0', '0')
    return xor(ct, mod)

ctOfMsgSent = xor(m, k) # m xor k
ctOfMsgModified = attack(ctOfMsgSent, '9') # m xor k xor p
decryptedMsg = xor(ctOfMsgModified, k) # (m xor k xor p) xor k = m xor p


print("Sent message: {}". format(m))
print("Received message: {}".format(decryptedMsg))
