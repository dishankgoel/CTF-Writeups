s1 = 'ADGJLQETUOZCBM10'
s2 = 'sfhkwryipxvn5238'
s = '1_4m_th3_wh1t3r0s3'



flag = ''

encoding = {}
for i in range(0, 16):
    ans = ['1','1','1','1']
    k = 3
    t = i
    while(t > 0):
        if(t&1 == 0):
            ans[k] = '1'
        else:
            ans[k] = '0'
        k -= 1
        t = t//2
    encoding["".join(ans)] = i
print(encoding)
for i in range(len(s)):
    bin_char = bin(ord(s[i]))[2:].zfill(8)
    even_pos = encoding[bin_char[0] + bin_char[2] + bin_char[4] + bin_char[6]]
    odd_pos = encoding[bin_char[1] + bin_char[3] + bin_char[5] + bin_char[7]]
    flag += s1[even_pos] + s2[odd_pos]

print(flag, len(flag))
print(len(s1))