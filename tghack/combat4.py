from pwn import *


for i in range(1,100000):
    p = remote('combatship4.tghack.no', 5002)
    print(p.recv())
    print(p.recv())
    p.sendline("{} {}".format(1337, i))
    print(p.recv())
    # input()
    p.close()

