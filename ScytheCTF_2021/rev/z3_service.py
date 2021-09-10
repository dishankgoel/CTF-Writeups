from z3 import *

s = Solver()
# a = IntVector("x", 0x20)
a = [BitVec(str(i), 8) for i in range(0x20)]

for i in range(0x20):
    s.add(a[i] > 0)

s.add(((((a[0x1a] * 32 + ((a[0xf] * 32 + (a[2] - a[0x1c]) + a[8]) - a[4])) - (a[9] >> 3)) - a[0xb]) + a[5] * 0x10 + a[0x11] + (a[0xe] >> 1)) == -0x48)
s.add((((a[0x19] +
                 ((((a[0x11] >> 3) +
                   (a[0x16] - (a[0x11] + a[0xc])) + (a[0x1b] >> 2) + a[0] + (a[0x16] >> 1)) - a[1]) -
                 a[0x1d]) + a[0x14]) - a[5]) + (a[4] >> 4)) == 0x10)
s.add((((a[0xe] + ((a[0x10] * 8 - (a[7] + a[0x11] + a[4] + a[0x16])) - a[8]) +
                           (a[0x17] >> 1) + a[6] + a[0xd] + a[5] * 8 + (a[0xc] >> 4)) - a[0x10])
                + a[8] * -4 + a[0x10]) == -0x17)

s.add((((a[0x1f] +
                 ((a[0] + a[0x14] + ((a[2] + a[10] + a[8]) - a[5]) + a[5] * -8 + a[0x10]) - a[0x17]))
                - (a[0x11] >> 2)) + a[3]) == -6)
s.add((a[0x1c] + (((a[8] * 8 +
                           a[2] + ((a[0x12] + ((a[0x16] - (a[0x13] + a[0x14])) - a[4]) +
                                   a[0x10] * -0x20) - (a[0xd] >> 3)) + a[0x15] * -0x20) - a[0x1e]) -
                         a[0x12]) + a[0] * -0x10 + a[0xc] + a[0xb] * -0x10 + a[0xb] + (a[0xe] >> 5))
        == 65)
s.add((((((a[10] + ((((a[0x1a] >> 1) - (a[0x1d] + a[0x1f])) - a[7]) - (a[0] >> 4)) + a[0x1c])
                  - a[0xf]) - a[0x1e]) - (a[0x16] >> 5)) + (a[0x1b] >> 3)) == 0xf)
s.add(((((a[4] >> 2) +
                 a[0x12] + (((a[2] + ((a[0xb] + (a[0x11] - a[7]) + a[0x18] + a[0xd] * -0x20) -
                                     (a[0xf] >> 2)) + a[0x15]) - a[5]) - a[0x1d]) + a[5] * -0x10) -
                a[0x11]) + a[5] * -2 + a[7]) == -0x5a)
s.add((((a[0x11] +
               (((((a[0xf] >> 2) +
                  ((a[0x1d] * 8 - (a[0x16] + a[0x12] * 2 + (a[7] >> 3))) - a[0x1d]) + a[0xc]
                  + (a[3] >> 2)) - a[0x11]) - a[9]) - a[0x11]) + a[0x17] * 2 + a[0] * 32) -
              a[0x1b]) + a[0x19] + a[0x13]) == 0x1e)
s.add((((((((a[0x1c] + (((a[0x14] >> 1) + (a[10] - a[0x1b]) + a[0xc] * 8) - a[0x1c]) +
                               a[4] + a[0x1f] * -8) - a[5]) - a[9]) - a[0x17]) - (a[0x19] >> 2)) -
               a[0x1b]) + a[0xc]) == 119)
s.add((((a[0x19] + (a[0x18] >> 5) +
                           (a[0x1b] - (a[0xc] >> 5)) + a[0xc] * 2 + a[0] * 2 +
                           a[0xd] * -0x20 + a[0xd] * -0x20 + a[0xf] + a[3] + a[0x18] + a[0x16] +
                a[0xb] * -0x20) - a[0x12]) + a[0x18]) == -0x36)

print(s.check())
model = s.model()
# flag = ''.join([chr(int(str(model[a[i]]))) for i in range(len(model))])
# print(bytes(flag))
print([str(model[a[i]]) for i in range(len(model))])