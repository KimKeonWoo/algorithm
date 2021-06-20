n = int(input())

for _ in range(n):
    m = int(input())

    result = False

    for i in range(2, 10**6 + 1):
        if i * i > m:
            break

        if m % i == 0:
            result = True
            break

    if result:
        print("NO")
    else:
        print("YES")