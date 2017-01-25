import chall7 #aesDecECB
import chall9 #padding PKCS7
import base64

def byteList2byte(bl):
    result = b''
    for b in bl:
        result += b
    return result

def encCBC(pt, iv, key):
    blocks = [pt[i:i+16] for i in range(0, len(pt), 16)]
    encBlocks = []

    b0Xored = xor(blocks[0], iv)
    ct0 = chall7.aesEncECB(b0Xored, key)
    encBlocks.append(ct0) # First block uses IV

    for b in range(1, len(blocks)):
        blockXored = xor(blocks[b], encBlocks[b-1])
        blockFunc = chall7.aesEncECB(blockXored, key)
        encBlocks.append(blockFunc)
    return byteList2byte(encBlocks)

def decCBC(ct, iv, key):
    blocks = [ct[i:i+16] for i in range(0, len(ct), 16)]
    decBlocks = []

    ct0Func = chall7.aesDecECB(blocks[0], key)
    b0 = xor(ct0Func, iv)
    decBlocks.insert(0, b0)

    for i in range(1, len(blocks)):
        blockFunc = chall7.aesDecECB(blocks[i], key)
        block = xor(blockFunc, blocks[i-1]) # First block uses IV
        decBlocks.append(block)
    return byteList2byte(decBlocks)

def xor(a,b):
    result = bytearray(a)
    for i, k in enumerate(b):
        result[i] ^= k
    return bytes(result)

if __name__ == "__main__":
    iv = b"0000000000000000"
    key = b"YELLOW SUBMARINE"

    with open('10.txt', 'rb') as f:
        pt = base64.b64decode(f.read())

    paddedPt = chall9.pad(pt,16)
#    print(paddedPt)
    decBlocks = (decCBC(paddedPt, iv, key))
    print(str(decBlocks))
