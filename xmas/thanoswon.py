import requests

host = "http://challs.xmas.htsp.ro:1341/"
port = 1341
while 1:
    r = requests.get(host)

    print(r.text)