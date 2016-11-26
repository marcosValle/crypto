import itertools
import math
import binascii

def preProcess(msg):
    for b in msg:
        if b not in range(32,127):
            return ''
    return msg

def xor(key, ct):
    res = b''
    for c in ct:
        res += bytes([key^c])
    return res

# chi-squared goodness-of-fit
def score(msg):
    letterFrequency = { 'e': 0.12702, 't':0.09056, 'a':0.08167, 'o':0.07507, 'i':0.06966, 'n':0.06749, 's':0.06327, 'h':0.06094, 'r':0.05987, 'd':0.04253, 'l':0.04025, 'c':0.02782, 'u':0.02758, 'm':0.02406, 'w':0.02360, 'f':0.02228, 'g':0.02015, 'y':0.01974, 'p':0.01929, 'b':0.01492, 'v':0.00978, 'k':0.00772, 'j':0.00153, 'x':0.00150, 'q':0.00095, 'z':0.00074 }
    score = 0
    for b in range(ord('a'), ord('z')+1):
        if b in msg:
            expected = len(msg)*letterFrequency[chr(b)] 
            score += math.pow( msg.count(b) - expected, 2)/expected
    return score

def xoredKeyScore(msg):
    scores = []
    for key in range(ord('a'), ord('z')+1):
        xored = xor(key, msg).lower()
        scores.append( (xored, key, score(xored)) )
    return scores


h = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
msg = binascii.a2b_hex(h)

xoredKeyScore = xoredKeyScore(msg)

qntResults = 3
result = sorted(xoredKeyScore, key=lambda tup: tup[2])[:qntResults]

for i in range(0, qntResults):
    print("String: {}\nKey: {}\nScore: {}".format(result[i][0].decode('ascii'), chr(result[i][1]), result[i][2]))
