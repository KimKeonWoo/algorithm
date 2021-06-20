arr = list(map(int, input().split()))
arr.sort(reverse=True)

a, b = arr[0], arr[1]
while a % b != 0:
    temp = a % b
    a = b
    b = temp

gcd = b
print(arr[0] * arr[1] // gcd)
