d = "0123456789ABCDEFGHIJKLMNOPQRSTUVWYZABCDEFGHIJK"
k = "6EMUD3BJRAI08GOWF2AIQZH19HPYG7FNVE4CKSBJ5DLTCK"
f = "SNESYT3AYN1CTISL7SRS31RAFSKV3C4I0SOCNTGER0COM5"

flag = ['',]*len(f)

mymap = {}
found = {}

weird_index = {}
swap = []

for i in range(len(k)):
    for j in range(len(d)):
        if( k[i] == d[j] and found.get(k[i], -1) == -1):
            found[k[i]] = 1
            mymap[i] = j
        elif( k[i] == d[j] and found.get(k[i], -1) != -1):
            for m in range(j+1, len(d)):
                if(d[m] == k[i]):
                    mymap[i] = m
                    weird_index[i] = (j, m)
                    break

print(mymap)

for i in range(len(f)):
    if(i in weird_index):
        print("{} => {} and {}".format(f[i], weird_index[i][0], weird_index[i][1]))
    flag[mymap[i]] = f[i]

print(" ".join(flag))
for i in range(len(flag)):
    print(i, end = "")

print()

'''
C A S T O R S C T F R  3  C  0  N  4  I  S  S  A  N  C  E  I  S  K  3  Y  T  O  S  0  L  V  1  N  G  M  Y  S  7  3  R  1  E  5
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45

'''

flag = "C A S T O R S C T F R { 3  C  0  N  4  I  S  S  A  N  C  E _  I  S _ K  3  Y _ T  O _ S  0  L  V  1  N  G _ M  Y  S  7  3  R  1  E  5 }"
print(flag.replace(" ", ""))
