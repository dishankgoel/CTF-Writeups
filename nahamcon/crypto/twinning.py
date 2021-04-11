from pwn import *
from gmpy2 import *
import requests
import re
from Crypto.PublicKey import RSA

def factordb(n):
    def solveforp(equation):
        try:
            if '^' in equation:
                k, j = equation.split('^')
            if '-' in j:
                j, sub = j.split('-')
            eq = list(map(int, [k, j, sub]))
            return pow(eq[0], eq[1])-eq[2]
        except:
            print("Can't find factors on factordb")

    # Factors available online?
    try:
        url_1 = 'http://factordb.com/index.php?query=%i'
        url_2 = 'http://factordb.com/index.php?id=%s'
        s = requests.Session()
        r = s.get(url_1 % n, verify=False)
        regex = re.compile(r"index\.php\?id\=([0-9]+)", re.IGNORECASE)
        ids = regex.findall(r.text)

        if len(ids) < 3:
            # Factordb does not have at least two factors
            return

        p_id = ids[1]
        q_id = ids[2]
        # bugfix: See https://github.com/sourcekris/RsaCtfTool/commit/16d4bb258ebb4579aba2bfc185b3f717d2d91330#commitcomment-21878835
        regex = re.compile(r"value=\"([0-9\^\-]+)\"", re.IGNORECASE)
        r_1 = s.get(url_2 % p_id, verify=False)
        r_2 = s.get(url_2 % q_id, verify=False)
        key_p = regex.findall(r_1.text)[0]
        key_q = regex.findall(r_2.text)[0]
        p = int(key_p) if key_p.isdigit() else solveforp(key_p)
        q = int(key_q) if key_q.isdigit() else solveforp(key_q)
        if p == q == n:
            return("Can't factor numbers")
        return p,q
    except:
        print("Can't factor")
        return("Can't factor")

r = remote("jh2i.com", 50013)
msg = r.recvuntil("PIN?")
print(msg.split())
l = msg.split()
c = mpz(int(l[-5]))
pair = l[-10]
print(pair)
e,n = pair.split(b",")
e,n = mpz(e[1:]), mpz(n[:-1])
print(e)
print(n)
print(c)
p,q = factordb(n)
print(p)
print(q)

if p != q:
    t = (p-1)*(q-1)
else:
    t = p*(q-1)
d = invert(e, t)
key = RSA.construct((int(n), int(e), int(d), int(p), int(q)))
ans = key.decrypt(int(c))
print(ans)

r.interactive()