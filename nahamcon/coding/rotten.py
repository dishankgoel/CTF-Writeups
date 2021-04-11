from pwn import *
from string import ascii_lowercase
p = remote("jh2i.com", 50034)

s = p.recv().strip()
p.sendline(s)
flag = ['']*100

while 1:
    s = p.recv().strip()
    # print(s)
    offset = s[0] - ord('s')
    # print(offset)
    new = ''
    for i in range(len(s)):
        if(chr(s[i]) in ascii_lowercase):
            new += chr(97 + (((s[i]-97) - offset)%26 + 26)%26)
        else:
            new += chr(s[i])
    if("'" in new):
        k = new.split()
        flag[int(k[-6]) - 1] = k[-1][1]
    # print(new)
    p.sendline(new)
    print("".join(flag))
