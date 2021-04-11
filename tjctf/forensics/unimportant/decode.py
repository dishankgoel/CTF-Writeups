from PIL import Image
from binascii import unhexlify
img = Image.open('unimp.png')

flag = ''

data = img.load()

def decode_bin(flag):
    try:
        return unhexlify(hex(int(flag, 2))[2:])
    except:
        return unhexlify(hex(int(flag, 2))[2:-1])


for i in range(img.width):
    for j in range(img.height):
        pixel = data[i,j]
        if(pixel[1]&2 == 0):
            flag += '0'
        else:
            flag += '1'
        print(decode_bin(flag))
        input()

flag = 'tjctf{n0t_th3_le4st_si9n1fic4nt}'