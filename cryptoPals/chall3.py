import itertools
import math
import binascii
import scipy
from scipy.stats import chisquare

letterFrequency = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182 
}
 
def xor(key, ct):
    res = b''
    for c in ct:
        res += bytes([key^c])
    return res

# chi-squared goodness-of-fit >> NOT WORKING
def chiSquareScore(msg):
    expectedFreqs = list(letterFrequency.values())
    observedFreqs = []

    for letter, freq in letterFrequency.items():
        observedFreqs.append( msg.lower().count(ord(letter))/len(msg) )

#    score = 0
#    counted = []
#    for b in msg:
#        if b not in counted:
#            c = chr(b).lower()
#            if c in letterFrequency:
#                counted.append(b)
#                expected = len(msg)*letterFrequency[c] 
#                score += math.pow( msg.count(b) - expected, 2)/expected
#    print(counted)
    return chisquare(observedFreqs, expectedFreqs)

def charFreqScore(msg):
    letterFrequency = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182 
}

    score=0
    for b in msg:
        c = chr(b).lower()
        if c in letterFrequency:
            score += letterFrequency[c]
    return score

def xoredKeyScore(msg):
    scores = []
    for key in range(0, 256):
#        xored = xor(key, msg).lower()
        xored = xor(key, msg)
        scores.append( (xored, key, charFreqScore(xored)) )
    return scores

def getResults(xoredKeyScore):
    return sorted(xoredKeyScore, key=lambda tup: tup[2])[-1:]

def printResults(result):
    for i in range(0, len(result)):
        print("String: {}\nKey: {}\nScore: {}".format(result[i][0], chr(result[i][1]), result[i][2]))

if __name__ == "__main__":
    h = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    msg = binascii.a2b_hex(h)
    
    xoredKeyScore = xoredKeyScore(msg)

    results = getResults(xoredKeyScore)
    #printResults(results)
    printResults(results)
