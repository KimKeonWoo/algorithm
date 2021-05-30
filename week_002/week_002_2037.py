#p : 버튼 한 번 누르는데 걸리는 시간
#w : 같은 숫자를 연속으로 찍기위해 기다려야하는 시간
p, w = map(int, input().split())
n = input().strip()


base1 = [3, 3, 3, 3, 3, 4, 3, 4]    # 숫자 키패드에 문자가 곂쳐있는 갯수
base2 = []                          # A = 65 --> index : 0 부터 시작
                                    # A~Z까지 어느 숫자에 맵핑되어있는지
base3 = []                          # A~Z까지 각 문자를 출력하기 위해 걸리는 시간(이전 문자 고려 x)

#base2 셋팅
num_btn = 1
for i in base1:
    num_btn += 1
    for _ in range(i):
        base2.append(num_btn)
base2.append(1)

#base3 셋팅
for i in base1:
    cnt = p
    for j in range(i):
        base3.append(cnt)
        cnt += p
base3.append(p)

#받은 문자열에 대한 index번호 추출 #소요시간 및 키패드 맵핑 위치
base4 = []
for i in n:
    if i == " ":
        index = len(base3) - 1
    else:
        index = ord(i) - 65
    base4.append(index)

#결과 도출
pre_index = base4[0]
result = base3[pre_index]
for i in range(1, len(base4)):
    if base2[pre_index] == base2[base4[i]]:
        if base2[base4[i]] != 1:
            result += w

    result += base3[base4[i]]
    pre_index = base4[i]

print(result)


