from pwn import *
from PIL import Image
import os

img = open("queen.png", "rb").read()


# for h in range(500, 1000):
#     for w in range(500, 1000):
#         print("[*] Trying {} x {}".format(h, w))
#         wb = p32(w)[::-1]
#         hb = p32(h)[::-1]
#         new_img = img[:16] + wb + hb + img[24:]
#         print(new_img[:30])
#         t = open("queen_ans.png", "wb")
#         t.write(new_img)
#         t.close()
#         os.system("png-parser -o queen_ans1.png queen_ans.png > /dev/null")
#         try:
#             im = Image.open("queen_ans1.png")
#             im.verify()
#             exit()
#         except:
#             continue



w, h = 705, 504

print("[*] Trying {} x {}".format(h, w))
wb = p32(w)[::-1]
hb = p32(h)[::-1]
new_img = img[:16] + wb + hb + img[24:]
print(new_img[:30])
t = open("queen_ans.png", "wb")
t.write(new_img)
t.close()
os.system("png-parser -o queen_ans1.png queen_ans.png > /dev/null")
try:
    im = Image.open("queen_ans1.png")
    im.verify()
    exit()
except:
    print("not worked")

