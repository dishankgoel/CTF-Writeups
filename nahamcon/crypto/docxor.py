f = open('homework', 'rb').read()
l = open('new', 'wb')
# k = 'FLAG{'
from binascii import hexlify

def xor(passw):
    return(b"".join([bytes(chr(f[i]^ord(passw[i%len(passw)])),'utf-8') for i in range(len(f))]))

# for i in range(0, len(f) - len(k)):
#     passw = ''.join([chr(f[i+m]^ord(k[m])) for m in range(len(k))])
#     assert len(passw) == 5
#     if(passw[0] == passw[-1]):
#         print(xor(passw[:-1]))

    # print("====================================================")

# for a in ascii_lowercase:
#     for b in ascii_lowercase:
#         for c in ascii_lowercase:
#             for d in ascii_lowercase:
#                 key = a+b+c+d
#                 print(xor(key))
head = chr(0x50) + chr(0x4b) + chr(0x3) + chr(0x4)
# print(head[1])
key = "".join([chr(f[i]^ord(head[i])) for i in range(4)])
print(key)
print(len(key))
# print(key)
# print(hexlify(bytes(key, 'utf-8')))
new = xor(key)
l.write(new)
l.close()