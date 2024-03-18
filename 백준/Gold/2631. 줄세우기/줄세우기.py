n = int(input())
ppl = []
for _ in range(n):
    ppl.append(int(input()))
dp = [0 for _ in range(n)]
# dp[0] = 1
for i in range(n):
    idx = -1
    limit = ppl[i]
    maxppl = 0
    maxidx = -1
    for j in range(i):
        if ppl[j] < limit and dp[j] > maxppl:
            maxidx = j
            maxppl = dp[j]
    if maxidx == -1:
        dp[i] = 1
    else:
        dp[i] = maxppl + 1
print(n-max(dp))