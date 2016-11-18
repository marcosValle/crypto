#RESULTS ARE FREAKING VARYING!!!

#3. Single-byte XOR cipher
#  The hex encoded string:
#    1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
#... has been XOR'd against a single character. Find the key, decrypt the message. 

import binascii
from collections import Counter

# xor the cipher with each char
def xorSingleByte(h):
    s = binascii.unhexlify(h).decode('ascii')

    xored = []
    for x in range(256):
        res = ""
        for c in s:
            res += chr(ord(c)^x)
        xored.append(res)
    return xored

# defines which chars are valid to an english word
def setValidChars():
    validChars = []
    for c in range(32, 127): # plz check ASCII table
        validChars.append(chr(c))
    return validChars

# removes strings that have more non-valid chars than defined
def preProcessing(xored, rate):
    validChars = setValidChars()
    numValid = 0
    processed=[]
    for s in xored:
        numValid=0
        for c in s:
            if c in validChars:
                numValid += 1
        if numValid/len(s) >= rate:
            processed.append(s)
    return processed

# return the sum (totalError) of frequency error of each char (letterError) in the string relative to real frequency
def freqError(s):
    letterFrequency = [('e',0.12702), ('t',0.09056), ('a',0.08167), ('o',0.07507), ('i',0.06966), ('n',0.06749), ('s',0.06327), ('h',0.06094), ('r',0.05987), ('d',0.04253), ('l',0.04025), ('c',0.02782), ('u',0.02758), ('m',0.02406), ('w',0.02360), ('f',0.02228), ('g',0.02015), ('y',0.01974), ('p',0.01929), ('b',0.01492), ('v',0.00978), ('k',0.00772), ('j',0.00153), ('x',0.00150), ('q',0.00095), ('z',0.00074)]
    sMostCommon = []
    totalError = 0
    for t in letterFrequency:
        letterError = 0
        letterError = abs(s.count(t[0])/len(s) - t[1])
        totalError += letterError
    
    return (s, totalError)

h = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
xored = xorSingleByte(h)

xoredProc = preProcessing(xored, 0.7)

res=[]
for s in xoredProc:
    tupleS_error = freqError(s)
    res.append(tupleS_error)
d = sorted(res, key=lambda x:x[1])
print(d[:1][0][0])
