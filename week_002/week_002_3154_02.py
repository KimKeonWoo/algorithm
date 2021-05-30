def effort(num1, num2):
    x_len = abs(base[num1][0] - base[num2][0])
    y_len = abs(base[num1][1] - base[num2][1])

    return x_len + y_len


#숫자 키보드의 위치 (행열)
base = ['42', '11', '12', '13', '21', '22', '23', '31', '32', '33']

n = input()
hh = []
mm = []

n = list(map(int, n.split(':')))
hh.append(n[0])
mm.append(n[1])

#가능한 '시' 리스트 생성
temp = hh[0]
while True:
    temp += 24
    if temp >= 100:
        break
    hh.append(temp)
temp = hh[0]
while True:
    temp -= 24
    if temp < 0:
        break
    hh.append(temp)

#가능한 '분' 리스트 생성
temp = mm[0]
while True:
    temp += 60
    if temp >= 100:
        break
    mm.append(temp)
temp = mm[0]
while True:
    temp -= 60
    if temp < 0:
        break
    mm.append(temp)


