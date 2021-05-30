base = ['D', 'C', 'B', 'A', 'E'] #등 = 1 / 배 = 0
#윷 걸 개 도 모

for i in range(3):
    n = list(map(int, input().split()))
    temp = 0
    for j in range(4):
        temp += n[j]
    print(base[temp])