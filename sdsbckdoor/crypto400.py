from math import floor, sqrt
l = list(map(int,input().split()))
keys = [[] for i in range(len(l))]
for i in range(len(l)):
    for key in range(1010, 12323):
        for plain in range(48,123):
            decrpyt = (key+plain)/2 + sqrt(key*plain)
            decrpyt = floor(decrpyt)%255
            if decrpyt == l[i] and chr(plain).isalnum() and key == 10807:
                keys[i].append(key)
                print("{} {}".format(chr(plain), key))
ans = set(keys[0])
for i in range(1, len(l)):
    ans = ans.intersection(set(keys[i]))

print(ans)