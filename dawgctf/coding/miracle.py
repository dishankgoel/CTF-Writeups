from pwn import *

ans = ['7:53', '9:06', '6:44', '9:12', '8:24', '10:05', '8:24', '8:45', '9:35', '6:55', '8:48', '8:46', '10:00', '8:36', '7:30', '7:40', '9:24', '9:30', '9:24', '8:24', '7:45', '8:54', '6:46', '9:00', '8:36', '8:34', '9:02', '9:30', '7:18', '8:34', '8:37', '8:37', '8:41', '9:00', '8:36', '7:44', '8:45', '8:28', '9:00', '7:55', '8:30', '8:28', '8:14', '6:52', '8:37', '8:20', '9:00', '8:24', '7:30', '8:24', '8:28', '6:56', '8:35', '7:48', '8:00', '6:57', '7:48', '8:00', '8:00', '8:34', '8:30', '8:10', '8:10', '8:48', '8:00', '8:20', '9:13', '7:30', '10:00', '9:10', '7:31', '9:42', '8:45', '8:38', '7:30', '8:45', '8:20', '8:30', '7:30', '8:10', '8:54', '7:50', '9:00', '8:45', '7:36', '7:40', '8:15', '7:14', '9:17', '8:04', '8:20', '8:10', '8:36', '8:00', '8:42', '6:44', '8:37', '8:37', '8:00', '8:00', '7:49', '8:20', '7:00', '8:37', '8:24', '8:24', '8:00', '8:01', '8:57', '9:30', '7:15', '8:52', '9:45', '10:00', '7:48', '7:59', '8:52', '8:34', '8:37', '8:37', '8:30', '7:00', '8:36', '8:52', '7:18', '8:34', '8:20', '10:00', '8:00', '8:20', '8:33', '7:30', '8:21', '9:22', '8:37', '8:00', '7:42', '8:37', '9:10', '7:30', '8:37', '11:30', '8:34', '8:24', '7:46', '8:45', '8:00', '10:00', '8:24', '10:00', '8:24', '8:20', '8:10', '7:06', '8:12', '7:50', '10:00', '8:12', '7:45', '8:07', '7:39', '8:37', '7:43', '8:30', '8:34', '8:07', '8:37', '8:00', '8:30', '7:30', '8:20', '8:24', '8:06', '8:37', '10:00', '8:24', '7:10', '7:40', '9:10', '8:48', '8:30', '8:54', '8:42', '8:37', '8:00', '8:48', '7:55', '7:55', '8:40', '7:30', '7:54', '7:54', '8:24', '8:00', '8:40', '7:43', '8:20', '8:25', '8:10', '8:19', '8:12', '8:48', '8:00', '8:42', '8:5', '8:37', '7:30', '8:30', '8:20', '7:59', '8:36', '8:10', '7:30', '7:55', '7:32', '8:15', '7:40', '8:24', '8:10', '7:40', '7:35', '7:15', '8:35', '7:45', '8:24', '8:45', '6:42', '8:30', '7:30', '8:37', '8:37', '8:37', '7:48', '8:20', '7:50', '8:20', '7:30', '8:20', '8:14', '8:24', '8:30', '8:15', '7:30', '8:30', '8:24', '8:38', '8:40', '7:40', '8:27', '7:26', '7:15', '8:42', '8:11', '8:40', '7:30', '8:34', '7:43', '8:25', '7:30', '8:36', '8:00', '8:27', '6:54', '8:46', '8:40', '8:24', '8:20', '8:00', '8:00', '10:00', '8:48', '8:34', '8:22', '7:27', '8:40', '8:50', '8:00', '8:40', '8:20', '8:34', '8:52', '8:53', '8:00', '7:49', '8:50', '8:00', '8:46', '8:37', '8:36', '7:52', '8:50', '8:05', '8:30', '8:45', '8:45', '7:30', '8:48', '8:3', '8:37', '8:4', '8:45', '8:54', '8:00', '8:12', '8:24', '7:57', '8:37', '7:41', '7:30', '8:37', '8:37', '8:10', '6:31', '8:30', '8:15', '8:18', '6:55', '8:20', '8:18', '7:48', '8:20', '6:23', '9:31', '8:00', '8:13', '7:24', '8:30', '8:37', '8:37', '6:15', '9:2', '7:36', '7:36', '8:42', '8:04', '8:45', '8:12', '8:37', '6:08', '8:34', '8:24', '7:44', '8:42', '7:41', '8:00', '8:26', '8:42', '8:20', '8:24', '7:25', '8:42', '8:30', '8:33', '7:50', '7:48', '8:00', '7:41', '8:07', '7:42', '6:35', '7:40', '7:30', '10:06', '6:40', '8:40', '7:47', '8:45', '8:48', '7:45', '9:12', '9:46', '8:20', '7:53', '8:40', '8:13', '8:16', '8:42', '8:24', '7:30', '8:45', '8:30', '7:10', '8:45', '8:42', '7:46', '8:24', '7:49', '8:20']
print(len(ans))
while 1:
    p = remote('ctf.umbccd.io', 5300)
    i = 0
    while 1:
        f = 0
        b = 0
        try:
            s = p.recvuntil("my pace?").split()
        except:
            print(p.recv())
            # input()
            p.interactive()
            fix = ans[-1].split(':')[0] + ":" + str(int(ans[-1].split(':')[-1]) - 1).zfill(2)
            ans = ans[:-1]
            ans.append(fix)
            print("fixed")
            print(ans)
            break
        if(i >= len(ans)):
            time = s[-4].decode('utf-8')
            mile = float(s[-6].decode('utf-8'))
            h,m,sec = str(time).split(':')
            print(h)
            print(m)
            print(sec)
            print(s)

            val = (int(h)*60 + int(m) + int(sec)/60)/mile
            val = str(val)
            minutes = val.split('.')[0]
            k = val.split('.')[1]
            # if(len(k) == 1):
            #     k = k + "0"
            # else:
            #     k = k[:2]
            k = "0." + k
            k = float(k)
            k = round((k*6)/10,2)
            k = str(k).split('.')[1]
            if(len(k) == 1):
                k += '0'
            seconds = k
            # seconds = str(int(k)*(6/10)).split('.')[0]
            # roundq = str(int(k)*(6/10)).split('.')[1]
            # if(int(roundq) > 5):
            #     seconds = str(int(seconds) + 1)
            # if(len(seconds) == 1):
            #     seconds = '0' + seconds
            # else:
            #     seconds = seconds[:2]
            # if(seconds == "43"):
            #     seconds = "44"
            # if(seconds == "02"):
            #     seconds = "24"
            # if(seconds == "34" and b == 0):
            #     seconds = "35"
            #     b = 1
            # if(seconds == "54" and f==0):
            #     seconds = "55"
            #     f = 1
            # if(seconds == "39"):
            #     seconds = "40"
            # if(seconds == "01"):
            #     seconds = "02"
            # if(seconds == "27"):
            #     seconds = "28"
            final = minutes + ':' + seconds
            # print(final)
            p.sendline(final)
            print(final)
            ans.append(final)
            i += 1
        else:
            print(s)
            final = ans[i]
            p.sendline(final)
            print("{} => {}".format(i, final))
            i += 1
        # print(p.recv())
        # print(p.recv())
    p.close()
    # p.interactive()