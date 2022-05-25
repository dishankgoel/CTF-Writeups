import json

data = open('packets_json.json').read()

data = json.loads(data)
flag = 'X'*1000
for i in range(len(data)):
    d = data[i]
    btatt = d["_source"]["layers"]["btatt"]
    offset = int(btatt["btatt.offset"]) - 1
    val = btatt["btatt.value"]
    val = [chr(int(i, 16)) for i in val.split(":")]
    val = "".join(val)
    flag = flag[:offset] + val + flag[offset + len(val):]
print(flag)
