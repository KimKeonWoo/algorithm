n = int(input())

a = n
for i in range(2, n + 1):
    if i * i > n:
        break

    while a % i == 0:
        a //= i
        print(i)

if a != 1:
    print(a)