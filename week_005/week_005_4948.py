while True:
    n = int(input())
    cnt = 0

    if n == 0:
        exit()
    if n == 1:
        print(1)
        continue


    is_prime = [True] * (2*n+1)

    for i in range(2, 2*n+1):
        if i * i > 2*n:
            break

        if not is_prime[i]:
            continue

        for j in range(i*2, 2*n+1, i):
            is_prime[j] = False

    for i in range(n+1, 2*n+1):
        if is_prime[i]:
            cnt += 1

    print(cnt)