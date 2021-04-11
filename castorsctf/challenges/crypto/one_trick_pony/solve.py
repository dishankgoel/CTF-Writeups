from pwn import *
from string import printable

pos = printable
flag = 'castorsCTF{'

p = remote("chals20.cybercastors.com" ,14422)
p.recv()

while 1:
    for i in pos:
        # print(p.recv())
        print("trying {}".format(i))
        p.sendline(flag + i)
        ans = p.recvline()
        ans = ans.split()[-1]
        if(ans == b"b''"):
            print("Found!! {}".format(flag + i))
            flag += i
            break