while True:
    n = int(input())
    if n == 0:
        break

    result = 1 #결과 값 (항상 +1)
    cnt = 1    #도달하고 싶은 횟수
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
        if cnt == n:
            break

        #현재 값에 중복 숫자가 없을경우 +1
        cnt += 1
        result += 1

    #결과 출력
    print(result)