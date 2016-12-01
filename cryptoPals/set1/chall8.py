import binascii
import collections

def repeatedBlocks(ct):
    repBlocks = 0

    blocks = [ct[i:i+16] for i in range(0, len(ct), 16)]
    counter = collections.Counter(blocks)
    for i in counter.values():
        repBlocks += i-1 #It always counts each element, so we must subtract 1 from each count
    return repBlocks

def detectECB(ct):
    if repeatedBlocks(ct)>0:
        return ct
    return ''

if __name__ == "__main__":
    with open("8.txt") as f:
        txt = f.read()

    cts = txt.split('\n')

    for ct in cts:
        if detectECB(ct):
            print(detectECB(ct))
