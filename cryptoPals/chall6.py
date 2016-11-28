# Break repeating-key XOR
import binascii
from itertools import cycle
import chall3

# Can we improve it? I bet we do :)
def hammingDist(m1, m2):
    assert len(m1) == len(m2)
    binStr = "".join("{0:b}".format(a^b) for a,b in zip(m1,m2))

    diff=0
    for b in binStr:
        if b=='1':
            diff += 1

    return diff
    
def findKeysizeBySize(ct, size):
    key_dist = []
    for KEYSIZE in range(2,41):
        a = ct[0 : KEYSIZE]
        avg = 0
        for i in range(2,size+2):
            b = ct[(i-1)*KEYSIZE : i*KEYSIZE]

# Can we get the keysize in place, without key_dist?
            avg += hammingDist(a,b)/(size+2)
        key_dist.append( (KEYSIZE, avg/KEYSIZE) )

    return sorted(key_dist, key=lambda tup: tup[1])
 
def newBlocks(ct, KEYSIZE):
    blocks = []
    for i in range(0, KEYSIZE):
        block = b''
        for b in ct[i::KEYSIZE]:
            block += bytes([b])
        blocks.append(block)
    return blocks

def breakRepSingByteXor(ct):
    KEYSIZE = findKeysizeBySize(ct, 10)[0][0]
    nBlock = newBlocks(ct,KEYSIZE)

    key = ''
    for block in nBlock:
        key += chr(chall3.breakSingleByteXor(block)[0][1])

    pt = "".join(chr(ord(a)^b) for a,b in zip(cycle(key), ct))
    return key,pt

ct64 = ''
fname = "6.txt"
with open(fname) as f:
    ct64 = f.read().strip()
    
ct = binascii.a2b_base64(ct64)
print(breakRepSingByteXor(ct))
