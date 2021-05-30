n = int(input())
cnt = 0

## 1 <= B <= A <= 500
for b in range(1, 500):
    for a in range(b, 500):
        if b > a:
            break

        if n == (a*a - b*b):
            cnt += 1

# 1 <= N <= 1000
if n < 1 and n > 1000:
    cnt = 0

print(cnt)