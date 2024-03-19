import sys
n, m = 10, 2000
dp = [[0 for j in range(n+1)] for i in range(m+1)]
for i in range(1, m+1):
    dp[i][1] = 1
for j in range(2, n+1):
    for i in range(1, m+1):
        end = i // 2
        for k in range(1, end+1):
            dp[i][j] += dp[k][j-1]
            
t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    
    # print(dp)
    answer = 0
    for i in range(m+1):
        answer += dp[i][n]
    print(answer)
    # print(dp)