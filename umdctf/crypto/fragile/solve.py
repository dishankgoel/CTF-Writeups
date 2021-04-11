f = open('ciphertext', 'r').read()
import base64
while True:
    try:
        f = base64.b64decode(f)
    except:
        print(f)
