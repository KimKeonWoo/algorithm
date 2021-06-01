base = []
for _ in range(10):
    base.append(int(input()))

result = 0
temp = []
for i in range(10):
    result += base[i]
    temp.append(result)

result = temp[:]
for i in range(10):
    result[i] = abs(result[i] - 100)
result.sort()

if 100 + result[0] in temp:
    print(result[0] + 100)
elif 100 - result[0] in temp:
    print(100 - result[0])