def effort(num1, num2):
    x_len = abs(int(base[num1][0]) - int(base[num2][0]))
    y_len = abs(int(base[num1][1]) - int(base[num2][1]))

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
hh.sort()
mm.sort()



#결과값 계산
result_len = 999999
result_arr = []
for i in hh:
    for j in mm:
        h_1 = i // 10
        h_2 = i % 10
        m_1 = j // 10
        m_2 = j % 10

        temp_arr = [h_1, h_2, m_1, m_2]
        temp_len = effort(h_1, h_2) + effort(h_2, m_1) + effort(m_1, m_2)
        if result_len > temp_len:
            result_len = temp_len
            result_arr = temp_arr

print("%d%d:%d%d"%(result_arr[0], result_arr[1], result_arr[2], result_arr[3]))
