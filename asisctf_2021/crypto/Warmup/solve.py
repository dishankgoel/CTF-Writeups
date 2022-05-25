

from Crypto.Util.number import *
enc = ''
with open('output.txt', 'r') as f:
    t = f.read()
    enc = t[6:]

p = len(enc)


for s_mod_p in range(p, 2, -1):
    dec = [' ' for i in range(p)]
    dec[0] = enc[0]
    for i in range(p - 1):
        val = pow(s_mod_p, i, p)
        dec[val] = enc[i + 1]

    msg = "".join(dec)

    print(msg[:15], "{}/{}".format(s_mod_p, p))
    if msg.startswith("ASIS{"):
        print(s_mod_p)
        print(msg)
        break

# Solution
# 10927
# ASIS{_how_d3CrYpt_Th1S_h0m3_m4dE_anD_wEird_CrYp70_5yST3M?!!!!!!}
