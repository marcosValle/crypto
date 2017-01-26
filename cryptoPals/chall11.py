# This solution only works for pts with lots of repetitions. This is due to the weak solution to chall8
import chall7
import chall8
import chall9
import chall10
import os
import random

def genAesKey():
    return os.urandom(16)

def encryption_oracle(pt):
    numBytes = random.randint(5,10)
    pt = pt + os.urandom(numBytes)
    numBytes = random.randint(5,10)
    pt = os.urandom(numBytes) + pt

    algo = random.randint(0,1)

    pt = chall9.pad(pt, 16)
 
    if algo % 2 == 0:
        return chall7.aesEncECB(pt, genAesKey()), 'ECB'
    else:
        iv = os.urandom(16)
        return chall10.encCBC(pt, iv, genAesKey()), 'CBC'

def detectEcbCbc(ct):
    if chall8.detectECB(ct):
        return 'ECB'
    else:
        return 'CBC'

def genPts(n):
    result = []
    for i in range(n):
        number = random.randint(0, 255)
        char = bytes([number])
        result.append(char*1000)
  
    return result

if __name__ == '__main__':
    passed = 0
    for pt in genPts(100):
        ct, realMode = encryption_oracle(pt)
        if detectEcbCbc(ct) == realMode:
            print('PASSED')
            passed += 1
        else:
            print('fail')
    print(passed)
