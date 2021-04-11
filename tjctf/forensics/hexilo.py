from PIL import Image

img = Image.open('hexillology.png')

pix = img.load()

flag = ''
d = {}
l = []
un_flag = set()
# for j in range(1200):
j = 601
for i in range(1800):
    pix_val = pix[i, j]
    if pix_val not in d:
        d[pix_val] = 1
        continue
    else:
        if pix_val not in l:
            l.append(pix_val)


# print(l)

for k in l:
    flag += chr(k[0]) + chr(k[1]) + chr(k[2])

# print(flag)
un_flag.add(flag)

print(un_flag)
