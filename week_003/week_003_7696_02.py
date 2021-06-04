result = 1  #결과 값 (항상 +1)
index = 1     #현재 횟수
n = 1000010 #도달하고 싶은 횟수
arr = [0]   #전처리 배열 #인덱스 번호를 입력하면 해당 결과값이 나옴
while True:
    #현재 값에 같은 숫자가 2개이상 존재하는지 확인
    temp = str(result)
    flage = True
    for j in temp:
        if temp.count(j) >= 2:
            flage = False
            break

    #현재 값에 같은 숫자가 2개 이상시 continue
    if flage == False:
        result += 1
        continue

    #정답 판별
    if index == n:
        break

    #현재 값에 중복 숫자가 없을경우 +1
    index += 1
    result += 1
    arr.append(result)

while True:
    m = int(input())
    if m == 0:
        break
    print(arr[m])
