from pwn import *
from string import printable

pri = "_{}!@abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

p = remote("chals20.cybercastors.com", 14420)

def pad(s):
    pad_b = 16 - len(s) % 16
    return bytes([pad_b]) * pad_b


shift = 'A'*9
block_number = 1
flag = 'Y}'
working_flag = 'Y}'

while 1:
    p.recvuntil("choice:")
    p.sendline("2")
    p.recvuntil(">")
    print(len(shift))
    p.sendline(shift)
    p.recv()
    target = p.recv().split()[-1]
    print(len(target))
    target = target[96*block_number:96*block_number+32]
    print(target)
    print(len(target))

    for i in pri:
        print("Trying {}".format(i))
        p.recvuntil("choice:")
        p.sendline("1")
        p.recvuntil(">")
        padding = pad(bytes(i + working_flag,'utf-8'))
        print(len(padding))
        p.sendline(bytes(i + working_flag,'utf-8') + padding)
        p.recv()
        got = p.recv().split()[-1][0:32]
        print(got)
        if(got == target):
            flag = i + flag
            working_flag = i + working_flag
            print("Found!!! {}".format(flag))
            shift += 'A'
            if(len(flag)%16 == 0):
                working_flag = flag[0:15]
            break

# print(len(target))

p.interactive()