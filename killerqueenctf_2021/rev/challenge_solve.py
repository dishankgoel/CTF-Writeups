

def check(a):
    if a >= 33 and a <= 126:
        return 1
    return 0

build = '''9xLmMiI2znmPam'D_A_1:RQ;Il\*7:%i".R<'''
flag = ['' for i in range(len(build))]

for i in range(0, len(build), 2):
    t1 = (ord(build[i]) - 33)
    t2 = (ord(build[i + 1]) - 33)

    axi, axi1 = '', ''
    for g in range(10):
        for h in range(10):
            real_t1 = 93*g + t1
            real_t2 = 93*h + t2
            xi = real_t1 + real_t2 - 153 - 93
            xi1 = real_t1 + 2*real_t2 - 153 - 2*93

            xi = 158 - xi
            xi1 = 158 - xi1

            if check(xi):
                axi = chr(xi)
            if check(xi1):
                axi1 = chr(xi1)

    flag[i] = axi
    flag[i + 1] = axi1

print(flag)
print("".join(flag))
