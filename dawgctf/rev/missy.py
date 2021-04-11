s = "AõQÑMaÕéi\x89\x19Ý\t\x11\x89Ë\x9dÉiñmÑ}\x89ÙµY\x91Y±1YmÑ\x8b!\x9dÕ=\x19\x11yÝ"

t = s[::-1]

rev = ""

for i in range(len(t)):
    rev += chr(int(bin(ord(t[i]))[2:].zfill(8)[::-1],2))

flag = ""
for i in range(len(rev)):
    new = ""
    c = bin(ord(rev[i]))[2:].zfill(8)
    for j in range(8):
        if(c[j] == '0'):
            new += '1'
        else:
            new += '0'

    flag += chr(int(new, 2))

print(flag)

