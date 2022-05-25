import numpy as np

a = np.array([0], dtype=int)
# val = int(input("This hammer hits so hard it creates negative matter\n"))
# if val == -1:
# 	exit()

# for val in range(9223372036854775807 - 100000, 9223372036854775807 + 1):
#     print(val)
#     a[0] = val
#     print("First: {}, {}".format(7*a[0], 7*val))
#     a[0] = (a[0] * 7) + 1
#     print("Ans: {}".format(a[0]))
#     if a[0] == -1:
#         print("flag!")
#         break

val = 2635249153387078802
print(val)
a[0] = val
print("First: {}, {}".format(7*a[0], 7*val))
a[0] = (a[0] * 7) + 1
print("Ans: {}".format(a[0]))
if a[0] == -1:
    print("flag!")
