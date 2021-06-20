n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    A, B = arr[0], arr[1]
    while A % B != 0:
        temp = A % B
        A = B
        B = temp

    gcd = B
    print(arr[0] * arr[1] // gcd)