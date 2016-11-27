import binascii
import singleByteXor as sbx

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
        xoredKeyScore = sbx.xoredKeyScore(binascii.unhexlify(s))
        tuples.append(sbx.getResults(xoredKeyScore)[-1])

sortedTuples = sbx.getResults(tuples)
sbx.printResults(sortedTuples)

