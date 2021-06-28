n = int(input())
base = []
dp = [-1 for i in range(n)]

for _ in range(n):
    temp = list(map(int, input().split()))
    base.append(temp)

def recur(cur):
    if cur > n:
        return -9999
    if cur == n:
        return 0

    if dp[cur] != -1:
        return dp[cur]

    dp[cur] = max(recur(cur+base[cur][0]) + base[cur][1], recur(cur+1))
    return dp[cur]

recur(0)
print(max(dp))