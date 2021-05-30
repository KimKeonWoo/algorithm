base = [500, 100, 50, 10, 5, 1]

n = 1000 - int(input())

cnt = 0
for i in base:
    if n <= 0:
        break
    while True:
        n -= i
        if n < 0:
            n += i
            break
        cnt += 1

print(cnt)