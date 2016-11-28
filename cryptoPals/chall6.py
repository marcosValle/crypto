# Break repeating-key XOR

# Can we improve it? I bet we do :)
def hammingDist(m1, m2):
    assert len(m1) == len(m2)
    binStr = "".join("{0:b}".format(a^b) for a,b in zip(m1,m2))

    diff=0
    for b in binStr:
        if b=='1':
            diff += 1

    return diff

m1 = b'this is a test'
m2 = b'wokka wokka!!!'

print(hammingDist(m1,m2))
