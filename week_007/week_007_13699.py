n = int(input())
if n == 0:
    print(1)
    exit()

dp = [-1 for i in range(n+1)]
dp[0] = 1
for i in range(1, n+1):
    temp = 0
    for j in range(i):
        temp += dp[j] * dp[i-j-1]
    dp[i] = temp
print(dp[n])