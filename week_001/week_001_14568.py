n = int(input()) #총 사탕갯수
cnt = 0 #경우의 수

#i #남규 - 사실상 3개이상 | 0개 x,영훈보다 2개이상 많이
#j #영훈 - 사실상 1개이상 | 0개 x
#x #택희 - 사실상 2개이상 | 0개 x, 홀수개 x
for i in range(n+1):
    for j in range(n+1-i):
        for x in range(n+1-i-j):
            if i==0 or j==0 or x==0:
                continue
            if i + j + x != n:
                continue
            if i - j < 2:
                continue
            if x % 2 != 0:
                continue
            cnt += 1

if n < 6 and n > 100:
    cnt = 0

print(cnt)
