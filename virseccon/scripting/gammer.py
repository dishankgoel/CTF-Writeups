from pwn import *
import string

p = remote('jh2i.com', 50012)

possible = string.printable
flag = "LLS{"
print(p.recvuntil("let's see it!"))
while 1:
    for k in possible:
        p.sendline(flag + k)
        verdict = p.recvuntil("let's see it!").split()[-13]
        if(verdict == b'CORRECT!'):
            flag += k
            break
    print(flag)