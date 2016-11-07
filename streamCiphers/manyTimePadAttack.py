from collections import Counter

m1 = "BANANAS ARE COOL"
m2 = "PINEAPLES ARE COOLER THOUGH"
m3 = "HOLY BEAVER, WE NEED MORE MSGS"
m4 = "ONCE UPON A TIME THERE WAS"
m5 = "A BIG FAT MSG IN A"
m6 = "CRAPPY CRYPTO ALGORITHM WHICH"
m7 = "WE ARE NOW TRYING TO CRACK"
m8 = "DAMN, WE STILL NEED SOME MORE"
m9 = "MR TRUMPS HAIRCUT IS SO"
m10 = "AWESOME. I NEED TO GET MY HAIR CUT LIKE HIS."
k = "this key is freaking awesome"

# First step is to eliminate the entropy added by the random key, since it could contain any chrs (including non alphanumeric). We remove the key by xoring the CTs.

# Now we have the results of alphanumeric strings. It will mostly contain random chrs (xor of two samecase alphanumerics) and spaces (xor of different cases alphanumerics).

# Well, actually the result of xoring different case letters could be spaces and also numbers and punctuations. So our initial result will probably contain some mistakes. 

def xorDec(m, k):
    if len(m)>len(k):
        return "".join(chr(ord(a)^ord(b)) for a,b in zip(m[:len(k)],k))
    else:
        return "".join(chr(ord(a)^ord(b)) for a,b in zip(m,k[:len(m)]))


msgsMatrix = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]
ctMatrix = []
for m in msgsMatrix:
    ctMatrix.append(xorDec(m, k))

# xor(two same case letters) = random chr
# xor(different case letters) = punctuation or numbers
# The special thing here is about ' ' (space) chr. 
# xor(letter with space) = flips letter case
# So if we xor(m1, m2) we should obtain a lot of random chrs and a few letters (lower of capital). Those letters are the result of the xor of a letter and a space in m1 or m2.
# The function then checks xor(c1,c2) = xor(m1,m2) for letters. We then know that in this position (in m1 or m2), there is a space.
# Next step is to find out if the space is in m1 or m2. If apply function above with each xor of msgs, we can check for the same positions that are letters in the result.

#for rot in range(1,10):
#    xoredMatrix = [xorDec(xorDec(a, k), xorDec(b,k)) for (a,b) in zip(msgsMatrix, msgsMatrix.rotate(rot))]

print("CTs: ")
for count, c in enumerate(ctMatrix):
    print("c{} : {}".format(count, c))
print("\nLet's crack c1\n")

xoredMatrix = [xorDec(ctMatrix[0],c) for c in ctMatrix if ctMatrix[0]!=c]

counter = Counter()
for x in xoredMatrix:
    for index, c in enumerate(x):
        if(c.isalpha()):
            counter[index] += 1

print(counter)

spaces=[]
for K,V in counter.items():
    if V>6:
        print("Position {} is probably a SPACE!".format(K))
        spaces.append(K)

for i in range(1,len(ctMatrix[0])):
    if i in spaces:
        print('_', end="")
    else:
        print('*', end="")

print()

# Good, we know where the spaces are! Now let's use the most common 3 letters words crib:

