from Crypto.Cipher import AES
import base64


key = base64.b64decode('BG0I2BRlkbTPevVsWzdozg==')
ciphertext = base64.b64decode('RTRvInzt/bzxdJgClIpZTftgpE2FwyjMyQMwCTnjQa0=')

print(len(key))

obj = AES.new(key, AES.MODE_CBC, key[:16])

print(obj.decrypt(ciphertext))

