import base64

f = open('baby.onion', 'r')
t = f.read()
i = 0
while 1:
    try:
        k = ''
        # print(len(f))
        # print(ord(f[-1]))
        # print(f[-4:])
        for i in range(0, len(t)-1, 2):
            k += chr(int(t[i:i+2], 16))

        t = base64.b64decode(k)
        print(i)
        i += 1
    except:
        print(k)
        print(t)