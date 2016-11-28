import binascii
import chall3

fpath = "4.txt"
fileStr = []
finals = []

with open(fpath) as f:
    for line in f:
        l = line.strip()
        fileStr.append(l)

tuples = []
for s in fileStr:
    if len(l)==60:
        xoredKeyScore = chall3.xoredKeyScore(binascii.unhexlify(s))
        tuples.append(chall3.getResults(xoredKeyScore)[-1])

sortedTuples = chall3.getResults(tuples)
chall3.printResults(sortedTuples)

