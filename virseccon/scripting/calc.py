from pwn import *

p = remote('jh2i.com', 50003)

print(p.recvuntil("\n\n"))
curreq = p.recv().split()
# print(p.recv())
while 1:
    print(curreq)
    var = curreq[-2]
    print(var)
    curreq = curreq[:-2]
    print(curreq)
    terms = []
    i = 0
    curt_term = []
    while(curreq[i] != b'+' and curreq[i] != b'-' and curreq[i] != b'='):
        curt_term.append(curreq[i])
        i += 1
    terms.append((b'+', curt_term))
    curt_term = []
    curr_sign = curreq[i]
    i += 1
    target = int(curreq[-1])
    while(i < len(curreq)):
        if(curreq[i] == b'+'):
            terms.append((curr_sign, curt_term))
            curr_sign = b'+'
            curt_term = []
        elif(curreq[i] == b'-'):
            terms.append((curr_sign, curt_term))
            curr_sign = b'-'
            curt_term = []
        elif(curreq[i] == b'='):
            terms.append((curr_sign, curt_term))
            break
        else:
            curt_term.append(curreq[i])
        i += 1

    print(terms)
    print(target)

    var_term = []
    for k in terms:
        if(var not in k[1]):
            if(k[0] == b'+'):
                if(len(k[1]) == 1):
                    target = target - int(k[1][0])
                else:
                    product = 1
                    for s in k[1]:
                        if(s != b'*'):
                            product *= int(s)
                    target = target - product
            if(k[0] == b'-'):
                if(len(k[1]) == 1):
                    target = target + int(k[1][0])
                else:
                    product = 1
                    for s in k[1]:
                        if(s != b'*'):
                            product *= int(s)
                    target = target + product
        else:
            var_term = k
    if(len(var_term[1]) == 1):
        if(var_term[0] == b'-'):
            target = (-1)*target
    else:
        product = 1
        for k in var_term[1]:
            if(k != b'*' and k != var):
                product *= int(k)
        if(var_term[0] == b'+'):
            target = target/(product)
        else:
            target = (-1)*(target/product)

    print(target)
    p.sendline(str(int(target)))
    curreq = p.recv().split()
    if(curreq == []):
        curreq = p.recv().split()
# print(p.recv())
# print(p.recv())

p.interactive()