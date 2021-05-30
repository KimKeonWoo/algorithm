n = int(input())
cnt = 0

if n >= 3 and n <= 3000:
    for i in range(3, n, 3):
        for j in range(3, n, 3):
            if n-(i+j) < 3 :
                break
            cnt += 1
else:
    cnt = 0

print(cnt)