m = '[?????]'
n = '[?????]'

a = 'abcdefghijklmnopqrstuvwxyz'
p = ' !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

assert len(m) == 63 and set(m).issubset(set(a + p))
assert len(n) == 7  and set(n).issubset(set(a))
assert m.count('tjctf{') == 1 and m.count('}') == 1 and m.count(' ') == 5

print(str([x for z in [[[ord(m[i]) ^ ord(n[j // 3]) ^ ord(n[i - j - k]) ^ ord(n[k // 21]) for i in range(j + k, j + k + 3)] for j in range (0, 21, 3)] for k in range(0, len(m), 21)] for y in z for x in y])[1:-1])

o = [1, 18, 21, 18, 73, 20, 65, 8, 8, 4, 24, 24, 9, 18, 29, 21, 3, 21, 14, 6, 18, 83, 2, 26, 86, 83, 5, 20, 27, 28, 85, 67, 5, 17, 2, 7, 12, 11, 17, 0, 2, 20, 12, 26, 26, 30, 15, 44, 15, 31, 0, 12, 46, 8, 28, 23, 0, 11, 3, 25, 14, 0, 65]