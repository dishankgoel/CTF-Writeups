import string

# key = "ÐdØÓ§åÍaèÒÁ¡"
key = "ÐdØÓ§åÍaèÒÁ¡*"

f = "h1_th3r3_1ts_m3"

# flag = ''
for k in range(1,255):
    flag = ''
    for i in range(len(f)):
        if(key[i] != '*'):
            flag += chr((ord(key[i]) - ord(f[i]) + 256) % 256)
        else:
            flag += chr((k - ord(f[i]) + 256) % 256)
    print(flag)