from Crypto.Util.number import *
import json
from hashlib import sha256

def xor(a, b):
    return bytes([i^^j for (i, j) in zip(a, b)])

flag = open('flag.txt', 'rb').read()
p = 13080400379037251631420589005467506153010556623322367437838784262754481760554380160904625118260600346898196818112877306008743893988016721941145512925655703
n = 20

G = Matrix(GF(p), json.load(open('gen')))
u = vector(GF(p), json.load(open('u')))

secret_key = getPrime(64)
out = []

for i, b in enumerate(bin(secret_key)[2:]):
    round_key = getRandomRange(0, p-1)
    if int(b):
        w = [int(j) for j in (G^round_key)*u]
    else:
        w = [int(getRandomRange(0, p-1)) for _ in range(n)]
    
    out.append(w)

key = (2*sha256(long_to_bytes(secret_key)).digest())[:len(flag)]
ct = xor(key, flag)
out = {"flag": ct.hex(), "secret": out}
json.dump(out, open("flag.enc", "w"))
