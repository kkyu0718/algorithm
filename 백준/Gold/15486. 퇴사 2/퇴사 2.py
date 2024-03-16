import sys
n = int(sys.stdin.readline())
tlst = []
plst = []
dp = [0 for i in range(n+100)]
for i in range(n):
    t, p = map(int, sys.stdin.readline().split())
    tlst.append(t)
    plst.append(p)

dp[0] = plst[0] if tlst[0] == 1 else 0
for i in range(n):
    d = tlst[i]
    dp[i+d-1] = max(dp[i+d-1], dp[i-1]+plst[i])
    dp[i] = max(dp[i], dp[i-1])
print(dp[n-1])