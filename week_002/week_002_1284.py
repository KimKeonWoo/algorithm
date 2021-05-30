base = [5, 3, 4, 4, 4, 4, 4, 4, 4, 4]
##각 자리들은 지정된 칸 수 + 1칸을 더 필요로함
# 0 : 4cm
# 1 : 2cm
# 나머지 : 3cm


while True:
    n = input()
    if n == "0":
        break

    result = 1
    for i in n:
        result += base[int(i)]
    print(result)

