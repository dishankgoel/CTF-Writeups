from Crypto.Util.number import *
from secret import p, q, r, flag

e=65537
n1 = p*r
n2 = q*r
m1 = bytes_to_long(flag[:len(flag)//2])
m2= bytes_to_long(flag[len(flag)//2:])
c1 = pow(m1, e, n1)
c2 = pow(m2, e, n2)

print (f'n1 = {n1}')
print (f'n2 = {n2}')
print (f'c1 = {c1}')
print (f'c2 = {c2}')
print (f'e = {e}')