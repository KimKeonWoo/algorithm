n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    flag = "YES"

    if min(arr[0], arr[1]) > max(arr[2], arr[3]):
        flag = "NO"
    if max(arr[0], arr[1]) < min(arr[2], arr[3]):
        flag = "NO"
    print(flag)
