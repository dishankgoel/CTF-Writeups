from Crypto.Util.Padding import unpad
from PIL import Image

img = open('chall.encrypted.bmp', 'rb').read()


for i in range(600, 700):
    # for j in range(250, 300):
    j = i
    size = (306, j)
    print(i, j)
    print("Size: {}", i)
    x = hex(size[0])[2:].zfill(4)
    y = hex(size[1])[2:].zfill(4)

    x1 = bytes([int(x[-2:], 16)])
    x2 = bytes([int(x[:2], 16)])

    y1 = bytes([int(y[-2:], 16)])
    y2 = bytes([int(y[:2], 16)])

    header = b"\x42\x4d" + b"\x00"*8 + b"\x36" + b"\x00"*3 + b"\x28" + b"\x00"*3 + x1 + x2 + b"\x00"*2 + y1 + y2 + b"\x00"*2 + b"\x01\x00\x18\x00" + b"\x00"*24 

    data = header + img[len(header):]

    open("new_bmp{}_{}.bmp".format(i, j), "wb").write(data)
    # im = Image.open("new_bmp{}_{}.bmp".format(i, j))
    # im.show()
    # input()
    # im.save()