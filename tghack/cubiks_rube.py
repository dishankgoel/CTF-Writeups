from pwn import *
import pycuber as pc

# p = remote('cubiks.tghack.no',7001)

# print(p.recv())

t = pc.Cubie()

mycube = pc.Cube(t)

print(mycube)