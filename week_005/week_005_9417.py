n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    m = len(arr)
    result = 1

    a, b = -1, -1
    for i in range(m):
        for j in range(m):
            if i == j:
                continue

            a, b = arr[i], arr[j]

            while a % b != 0:
                temp = a % b
                a = b
                b = temp

            result = max(result, b)
    print(result)