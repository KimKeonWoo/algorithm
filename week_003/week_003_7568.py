#몸무게, 키
base = []

n = int(input())
for _ in range(n):
    x, y = map(int,input().split())
    base.append([x, y])

result = []
for i in range(n):
    temp = 1
    for j in range(n):
        if i == j:
            continue
        if base[i][0] < base[j][0] and base[i][1] < base[j][1]:
            temp += 1
    print(temp, end=" ")

