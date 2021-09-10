x = 'e9 73 6b 7c 05 f4 90 de 99 9a 0b e1 cc 29 54 2d 81 be ea 92 d6 de 0b 35 0c e0 f0 dd 1b 91 3a 45 c1 b2 4e 6b 68 a0 fa 61 f6 0b fc 31 38 31 73 26 6c 7b 8c b7 bb fc 8a bf 8f a8 b6 e2 37 9e 25 68 0d 37 49 9a 58 ee 71 b1 16 bc 96 90 34 74 5c 7c 75 49 2e bf ce 69 60 18 d3 d2 9b c1 b8 9e 75 5d ed a6 a4 7a 5b 41 2e 99 88 9d 3d 77 9a e3 18 d4 f1 53 aa 3f ff 2d eb 8c f4 75 80 e8 36 a8 c5 ae e4 d1 51 0e a6 ea e4 dd 18 fa 2f 0e fd ec ab 75 48 ed d2 67'
func = '1a 7c 75 86 50 bc 19 3b d1 19 e7 c1 45 54 b8 ea c4 46 ea 92 d6 de cc 70 f0 e0 f0 dd 1b 7a 71 ce 84 4e 06 f3 20 2d ef cd d8 0b fc 3e 8e 35 63 29 d2 bb bf f2 47 75 48 34 ca 54 fe 7a 7f 13 28 3c 20 37 49 95 ee ea 79 be a8 7c 1f 41 05 b5 d7 39 89 01 b6 f7 43 7c 1d 35 d3 d2 94 77 bc 8e 7a e3 2d 97 6c 73 1e b9 ad dc 74 9c b6 32 66 d8 5d 38 8d fe 29 42 07 2d 9e 82 bc f8 bd 14 3a a8 c5 46 37 2c ae f1 4d e6 ac 50 25 fa 22 0e fd 04 6e 88 b7 12 42 ae c3'

x = x.split()
func = func.split()


correct_func = func

for i in range(0x94):
    correct_func[i] = int(func[i], 16)^int(x[i], 16)
correct_func[-1] = int(correct_func[-1], 16)

print(','.join([hex(i) for i in correct_func]))

a1 = '37 09 6c cc a0 12 0a 65 48 26 c0 25 f6 e7 c2 64 a7 22 92 bc 21 61 1a c4 73 c2 85 33 8a 30 b9 6e 71 a0 42 f8 5c bd f4 87 8e 69 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
a2 = '7b 4e 25 82 f5 6e 15 7b 27 76 bf 68 e1 ab d5 1e c4 29 df da 48 6d 74 ca 2f c6 ea 35 ee 36 ee 10 48 cf 15 c5 65 ed cc c6 e0 17 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'

a1 = a1.split()
a2 = a2.split()

myin = a1

for i in range(len(a1)):
    myin[i] = chr(int(a1[i], 16)^int(a2[i], 16)^i^42)

print("".join(myin))