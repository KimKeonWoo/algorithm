n, m, k = map(int, input().split()) #여자, 남자, 인턴쉽 인원
result = 0 #최대 팀 개수

if (m >= 0 and m <= 100) and (n >= 0 and n <= 100) and (k >= 0 and k <= m+n):
    for i in range(0, k+1):
        temp = min((n-i)//2, m-(k-i)) #여자//2 , 남자 중 작은 값 따라가기
        result = max(result, temp)


print(result)
