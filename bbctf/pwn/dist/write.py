from pwn import *
import os

env = dict(os.environ)
env["LD_PRELOAD"] = 'libc-2.27.so'
p = process('./write', env=env)

input("attach")

t = p.recvuntil("(q)uit")
print(t.split())

puts = t.split()[1]

stack = t.split()[3]

# print(t.split())

p.interactive()