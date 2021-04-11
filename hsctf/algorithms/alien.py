a = open('alien.txt').readlines()
for i in range(len(a)):
    a[i] = [int(i) for i in a[i].split()]

assert len(a) == len(a[0])
n = len(a)

dp = [[None]*n]*n
neg = [[None]*n]*n
dp[0][0] = a[0][0]

neg[0][0] = 1 if a[0][0] == -1 else 0

for i in range(1, n):
    dp[i][0] = dp[i-1][0] + a[i][0]
    dp[0][i] = dp[0][i-1] + a[0][i]
    neg[i][0] = neg[i-1][0] + 1 if a[i][0] == -1 else neg[i-1][0]
    neg[0][i] = neg[0][i-1] + 1 if a[0][i] == -1 else neg[0][i-1]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        neg[i][j] = neg[i-1][j] + neg[i][j-1] - neg[i-1][j-1] + 1 if a[i][j] == 1 else neg[i-1][j] + neg[i][j-1] - neg[i-1][j-1]

ans = 0

def solve_1d(a, k, left, right):
    n = len(a)
    presum = [a[0]]
    d = {}
    ans = 0
    for i in range(1, n):
        presum[i] = presum[i-1] + a[i]
            






for i in range(n):
    for j in range(i+1, n):


