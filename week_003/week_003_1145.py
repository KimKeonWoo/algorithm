arr = list(map(int, input().split()))
arr.sort()

for i in range(arr[0], arr[0]*arr[1]*arr[2] + 1):
    temp = 0
    for j in arr:
        if i % j == 0:
            temp += 1

    if temp >= 3:
        print(i)
        break