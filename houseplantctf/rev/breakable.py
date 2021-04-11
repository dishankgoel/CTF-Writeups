s = "k33p_1t_in_pl41n"

key = "ÒdÝ¾¤¤¾Ùà*åÐcÝÆ¥ÌÈá*ÏÜ¦aã"
flag1 = "**"
flag2 = ""
print(len(key))
print(len(s))

for i in range(len(s)-2):
    flag1 += chr((ord(key[i]) - ord(s[i]) + 256) % 256)

for i in range(len(s)-2, len(key)):
    flag2 += chr((ord(key[i]) - ord(s[i - len(s) + 2 + 2]) + 256) % 256)


print(len(flag1))
print(len(flag2))
print(flag1)
print(flag2)
# print(key[:len(s)-2])