a = input()
b = ''
d = "S0th3combination1sonetw0thr3efourf1ve"
for x in d:
    if(x == "a"):
        b += '@'
    elif(x == "@"):
        b += 'a'
    elif(x == "o"):
        b += '0'
    elif(x == "0"):
        b += 'o'
    elif(x == "e"):
        b += '3'
    elif(x == "3"):
        b += 'e'
    elif(x == 'l'):
        continue
    else:
        b += x
print(b)
print(len(b))

# d = "S0th3combination1sonetw0thr3efourf1ve"
# if(len(a)%4 == 0) and b == d:
#     print("You got the flag!")

