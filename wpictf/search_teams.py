import requests

for number in range(1,26):
    r = requests.get('https://ctf.wpictf.xyz/teams?page={}'.format(number))
    a = r.text
    if('WPI{' in a):
        print(a)
    print(number)