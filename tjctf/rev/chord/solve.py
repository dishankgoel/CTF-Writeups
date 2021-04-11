f = open('notes.txt').read()

chords = {}
for i in open('chords.txt').readlines():
	c, n = i.strip().split()
	chords[c] = n

untangled = ''

# i = 0
# while(i < len(f)):
#     if(i == 60-4 or i == 95-4 or i==209-4):
#         untangled += chords[f[i:i+3]]
#         i += 3
#         continue
#     curr = f[i:i+3]
#     if(curr == "001"):
#         untangled += chords[f[i:i+3]]
#         i += 3
#     elif(curr == "020"):
#         if(f[i+3] == "0"):
#             untangled += chords[f[i:i+4]]
#             i += 4
#         else:
#             untangled += chords[f[i:i+3]]
#             i += 3
#     elif(curr == "010"):
#         if(f[i+3] == "0"):
#             untangled += chords[f[i:i+4]]
#             i += 4
#         else:
#             untangled += chords[f[i:i+3]]
#             i += 3
#     else:
#         untangled += chords[f[i:i+4]]
#         i += 4
#     print(untangled)
#     print(i)
#     print(f[i-4:])

l = {'A':'1', 'B':'2', 'C':'3', 'D':'4', 'E':'5', 'F':'6', 'G':'7'}


s = "FFFcFAFGGbGaFAGDGCEfGGFfGDEfCAEfFCFAFcFcEfFAEfFdFEFcFfDDGd"

flag = ''

for i in s:
    try:
        flag += l[i]
    except:
        flag += i
from binascii import unhexlify
print(unhexlify(flag))
print(f)

print(untangled)

