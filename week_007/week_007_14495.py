n = int(input())

if n <= 3:
    print(1)
    exit()

dp = [0 for i in range(n+1)]
dp[1], dp[2], dp[3] = 1, 1, 1
for i in range(4, n+1):
    dp[i] = dp[i-1] + dp[i-3]
print(dp[n])
