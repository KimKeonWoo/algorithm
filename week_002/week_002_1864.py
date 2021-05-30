import math

base = "-\\(@?>&%"
## "/" : -1에 대응


while True:
    n = input()
    result = 0
    count = 0
    temp = 0
    if n == "#":
        break

    n = n[::-1]
    for i in n:

        if i == "/":
            temp = -1
        else:
            temp = base.find(i)
        result += temp * pow(8, count)
        count += 1
    print(result)

