from Crypto.Cipher import AES
# from secret import flag
import time
from hashlib import md5


# key = md5(str(int(time.time()))).digest()
# padding = 16 - len(flag) % 16
# aes = AES.new(key, AES.MODE_ECB)
# outData = aes.encrypt(flag + padding * hex(padding)[2:].decode('hex'))
# print outData.encode('base64')


f = open('encrypted', 'r')
k = f.read()
m = k.decode('base64')
for l in range(1585324144 - 172800 - 100000,1585324144):
    key = md5(str(l)).digest()
    aes = AES.new(key, AES.MODE_ECB)
    print(aes.decrypt(m))