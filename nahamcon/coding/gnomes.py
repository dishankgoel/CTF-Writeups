from pwn import *

p = remote("jh2i.com", 50031)

print(p.recvuntil(">"))
p.sendline("6")
p.recvuntil("shop):")

p.sendline("1")

free_gold = "5"
l1 = 0
l2 = 0
l3 = 0
l4 = 0
while 1:
    k = p.recvuntil(">")
    l = k.split()
    gold = int(l[l.index(b'Gold:') + 1])
    print(gold)
    if(gold > 100000):
        p.sendline("6")
        p.recvuntil("shop):")
        p.sendline("5")
        free_gold = str(1)
        p.interactive()
    elif(gold > 10000 and l3 == 0):
        p.sendline("6")
        p.recvuntil("shop):")
        p.sendline("4")
        free_gold = str(2)
        l3 = 1
    elif(gold > 2000 and l2 == 0):
        p.sendline("6")
        p.recvuntil("shop):")
        p.sendline("3")
        free_gold = str(3)
        l2 = 1    
    elif(gold > 1000 and l1 == 0):
        p.sendline("6")
        p.recvuntil("shop):")
        p.sendline("2")
        free_gold = str(4)
        l1 = 1
    else:
        p.sendline(free_gold)


p.interactive()