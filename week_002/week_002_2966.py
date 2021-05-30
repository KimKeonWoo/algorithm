n = int(input())
ans = input()

base1 = n * "ABC"
base2 = n * "BABC"
base3 = n * "CCAABB"


#상근 : Adrian 정답 갯수 계산
cnt_A = 0
for i in range(len(ans)):
    if base1[i] == ans[i]:
        cnt_A += 1

#창영 : Bruno 정답 갯수 계산
cnt_B = 0
for i in range(len(ans)):
    if base2[i] == ans[i]:
        cnt_B += 1


#현진 : Goran 정답 갯수 계산
cnt_G = 0
for i in range(len(ans)):
    if base3[i] == ans[i]:
        cnt_G += 1

#정답 출력
result = max(cnt_A, max(cnt_B, cnt_G))
arr_ans = [[cnt_A, 'Adrian'], [cnt_B, 'Bruno'], [cnt_G, 'Goran']]

print(result)
for i in range(3):
    if arr_ans[i][0] == result:
        print(arr_ans[i][1])
