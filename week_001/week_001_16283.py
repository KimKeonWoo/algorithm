a, b, n, w = map(int, input().split()) #양식사량, 얌소식사량, 양+염소 전체수, 전체식사량
result = "-1"

if (a >= 1 and a <= 1000) and (b >= 1 and b <= 1000) and (n >= 2 and n <= 1000) and (w >= 2 and w <= 1000000):
    if a == b and n == 2 and w == a+b:
        result = "1 1"
    else:
        for i in range(1, n):
            if w == a*i + b*(n-i):
                if result == "-1":
                    result = ""
                    result += str(i) + " " + str(n-i)
                else:
                    result = "-1" #이미 값이 들어가있는 경우(해가 두 개 이상인경우)
                    break   #근이 2개 이상인 순간 탐색 종료

print(result)
