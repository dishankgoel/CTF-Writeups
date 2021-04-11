import hashlib

f = open('../../../../../tryhackme/rockyou.txt', errors='ignore').read().split()
target = '7adebe1e15c37e23ab25c40a317b76547a75ad84bf57b378520fd59b66dd9e12'

for word in f:
    print("Trying {}: {}".format(word, hashlib.sha256(bytes("castorsCTF{" + word + "}", 'utf-8')).hexdigest()))
    if(hashlib.sha256(bytes("castorsCTF{" + word + "}", 'utf-8')).hexdigest() == target):
        print("Found!! {}".format(word))
        break

