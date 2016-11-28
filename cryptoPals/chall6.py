# Break repeating-key XOR
import binascii

# Can we improve it? I bet we do :)
def hammingDist(m1, m2):
    assert len(m1) == len(m2)
    binStr = "".join("{0:b}".format(a^b) for a,b in zip(m1,m2))

    diff=0
    for b in binStr:
        if b=='1':
            diff += 1

    return diff

def findKeysize(ct):
    key_dist = []
    for KEYSIZE in range(2,41):
        a = ct[0 : KEYSIZE]
        b = ct[KEYSIZE : 2*KEYSIZE]

# Can we get the keysize in place, without key_dist?
        dist=0
        for x,y in zip(a,b):
            dist += hammingDist( bytes([x]), bytes([y]) )

        key_dist.append( (KEYSIZE, dist/KEYSIZE) )

    return sorted(key_dist, key=lambda tup: tup[1])[0][0]
     
ct64 = ''
fname = "6.txt"
with open(fname) as f:
    ct64 = f.read().strip()
    
ct = binascii.a2b_base64(ct64)
print( findKeysize(ct) )
