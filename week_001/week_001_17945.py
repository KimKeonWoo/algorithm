a, b = map(int, input().split())
result = ""

if (a >= -1000 and a <= 1000) and (b >= -1000 and b <= 1000):
    for i in range(-1000010, 1000010):
        if 0 == i*i + 2*a*i + b:
            result += str(i) + " "

print(result)


