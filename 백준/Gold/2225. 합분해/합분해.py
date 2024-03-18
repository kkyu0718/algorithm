n, k = map(int, input().split())

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
dp[0][1] = 1
dp[1][1] = 1
for j in range(1, k+1):
    dp[0][j] = 1
for num in range(1, n+1):
    # print("num=", num)
    dp[num][1] =1
    for knum in range(1, k+1):
    
        # print("knum=", knum)
        for i in range(0, num+1):
                # print(num-i, knum-j, i, j)
                dp[num][knum] += dp[num-i][1]*dp[i][knum-1]

print(dp[n][k]%1000000000)