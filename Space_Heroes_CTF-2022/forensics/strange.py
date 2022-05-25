from datetime import datetime

l = [b'Wed Mar 23 13:02:11 2022 31', b'Wed Mar 23 13:02:11 2022 35', b'Wed Mar 23 13:02:12 2022 46', b'Wed Mar 23 13:02:12 2022 20', b'Wed Mar 23 13:02:13 2022 33', b'Wed Mar 23 13:02:13 2022 42', b'Wed Mar 23 13:02:14 2022 26', b'Wed Mar 23 13:02:15 2022 20', b'Wed Mar 23 13:02:15 2022 35', b'Wed Mar 23 13:02:15 2022 30', b'Wed Mar 23 13:02:15 2022 49', b'Wed Mar 23 13:02:16 2022 37', b'Wed Mar 23 13:02:16 2022 31', b'Wed Mar 23 13:02:17 2022 57', b'Wed Mar 23 13:02:17 2022 33', b'Wed Mar 23 13:02:18 2022 11', b'Wed Mar 23 13:02:18 2022 19', b'Wed Mar 23 13:02:19 2022 57', b'Wed Mar 23 13:02:19 2022 20', b'Wed Mar 23 13:02:20 2022 35', b'Wed Mar 23 13:02:20 2022 4', b'Wed Mar 23 13:02:20 2022 57', b'Wed Mar 23 13:02:21 2022 20', b'Wed Mar 23 13:02:22 2022 5', b'Wed Mar 23 13:02:22 2022 49', b'Wed Mar 23 13:02:22 2022 37', b'Wed Mar 23 13:02:24 2022 52', b'Wed Mar 23 13:02:24 2022 57', b'Wed Mar 23 13:02:26 2022 35', b'Wed Mar 23 13:02:26 2022 18', b'Wed Mar 23 13:02:26 2022 57', b'Wed Mar 23 13:02:27 2022 49', b'Wed Mar 23 13:02:28 2022 4', b'Wed Mar 23 13:02:28 2022 47', b'Wed Mar 23 13:02:28 2022 18', b'Wed Mar 23 13:02:28 2022 19', b'Wed Mar 23 13:02:29 2022 57', b'Wed Mar 23 13:02:30 2022 34', b'Wed Mar 23 13:02:31 2022 18', b'Wed Mar 23 13:02:31 2022 20', b'Wed Mar 23 13:02:31 2022 6', b'Wed Mar 23 13:02:32 2022 57', b'Wed Mar 23 13:02:33 2022 50', b'Wed Mar 23 13:02:33 2022 18', b'Wed Mar 23 13:02:34 2022 57', b'Wed Mar 23 13:02:35 2022 30', b'Wed Mar 23 13:02:35 2022 49', b'Wed Mar 23 13:02:36 2022 21', b'Wed Mar 23 13:02:36 2022 20', b'Wed Mar 23 13:02:36 2022 35', b'Wed Mar 23 13:02:37 2022 2', b'Wed Mar 23 13:02:37 2022 49', b'Wed Mar 23 13:02:37 2022 34', b'Wed Mar 23 13:02:39 2022 42', b'Wed Mar 23 13:02:40 2022 27', b'Wed Mar 23 13:02:43 2022 28']

data = []

for a in l:
    d = b" ".join(a.split(b' ')[:-1]).decode()
    m = a.split(b' ')[-1]
    t = datetime.strptime(d, "%a %b %d %H:%M:%S %Y")
    data.append((t, m))

# data.sort()
# print([str(i[0]) for i in data])
print("".join([chr(int(i[1], 16)) for i in data]))
print("".join([chr(int(i[1], 16)) for i in data])[::-1])
