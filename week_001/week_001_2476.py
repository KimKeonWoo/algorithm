
cnt = int(input())
sum = 0
result = 0

if cnt >= 2 and cnt <= 1000: #예외처리
    for x in range(cnt):
        a, b, c = map(int, input().split())

        if max(a, max(b,c)) > 6: #예외처리
            break

        if (a == b) and (b == c):
            sum = 10000 + b*1000
        elif(a == b) or (b == c) or (a == c):
            if b == c:
                sum = 1000 + b * 100
            else:
                sum = 1000 + a * 100
        else:
            sum = max(a, max(b, c)) * 100


        result = max(result, sum)
        x += 1

print(result)