def check_know(arr):
    global n
    temp_result = 0

    for i in range(n):
        flag = True
        for j in arr_input[i]:
            if j not in arr:
                flag = False
                break
        if flag:
            temp_result += 1

    return temp_result



#temp에서 2개를 조합으로 뽑아 뽑힌 케이스에서 result 값이 가장 큰것을 추출
def recur(cur, cnt):
    global cnt_pick, result

    if cnt_pick > len(temp):
        result = n
        return
    if cnt == cnt_pick:
        result = max(result, check_know(arr_pick))
        return
    if cur == len(temp):
        return

    arr_pick.append(temp[cur])
    recur(cur+1, cnt+1)
    arr_pick.pop()
    recur(cur+1, cnt)


base = 'antic'
n, k = map(int, input().split())
arr_input = []
for _ in range(n):
    arr_input.append(input())


#최소한 5개의 단어를 교육해야 antatica는 읽을 수 있음
if k < 5:
    print(0)
    exit()

#입력단어중 반드시 알아야하는 'antic'는 제거
cnt_pick = k - 5
for i in range(n):
    arr_input[i] = arr_input[i].replace('a', '')
    arr_input[i] = arr_input[i].replace('n', '')
    arr_input[i] = arr_input[i].replace('t', '')
    arr_input[i] = arr_input[i].replace('i', '')
    arr_input[i] = arr_input[i].replace('c', '')

#temp : 입력단어에서 'antic'을 각 단어들 중 중복되지 않게 한 문자열로 축약
temp = ""
for i in range(n):
    for j in arr_input[i]:
        if j in temp:
            continue
        temp += j
arr_pick = []
result = 0

recur(0, 0)
print(result)

