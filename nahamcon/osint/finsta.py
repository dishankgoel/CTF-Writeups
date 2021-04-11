import requests

url = "https://ctf.nahamcon.com/users?page={}"

for i in range(2,82):
    r = requests.get(url.format(i))
    print(r.text)
    print("trying.. {}".format(url.format(i)))
    if("NahamConTron" in r.text):
        print("Found!! {}".format(url))