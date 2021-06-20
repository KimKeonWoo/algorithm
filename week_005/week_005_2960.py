n, k = map(int, input().split())
arr = [True] * (n+1)
cnt = 0
result = 0

for i in range(2, n+1):

    if not arr[i]:
        continue

    for j in range(i, n+1, i):
        if arr[j]:
            arr[j] = False
            cnt += 1
            if cnt == k:
                print(j)
                exit()