from pwn import *
import base64 

p = remote("chals20.cybercastors.com", 14430)

# print(p.recv())
# p.recv()

p.recvuntil("ready.")

p.sendline("\n")
msg = p.recv()

while 1:
    try:
        msg = p.recvuntil("\n")
    except:
        p.interactive()
    msg = "".join([chr(int(i,2)) for i in msg.split()])
    print(msg)

    print("decoded:")
    msg = msg.split()
    msg = "".join([chr(int(i, 8)) for i in msg])

    print(msg)

    msg = msg.split()
    msg = "".join([chr(int(i, 16)) for i in msg])

    print(msg)

    msg = base64.b64decode(msg)
    print(msg)

    # msg = msg[11:-1]

    print(msg)
    p.sendline(msg)
    print(p.recvuntil("answer!\n"))



p.interactive()