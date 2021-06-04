n = int(input())
arr = list(map(int, input().split()))
result = 0

for pivot_1 in range(n-3):
    for pivot_2 in range(pivot_1+1, n-2):
        for pivot_3 in range(pivot_2+1, n-1):
            for pivot_4 in range(pivot_3+1, n):
                ## 각 단계의 결과값 계산
                temp_1 = 1
                for a in range(pivot_1+1):
                    temp_1 *= arr[a]

                temp_2 = 1
                for a in range(pivot_2, pivot_3):
                    temp_2 *= arr[a]

                temp_3 = 1
                for a in range(pivot_3, pivot_4):
                    temp_3 *= arr[a]

                temp_4 = 1
                for a in range(pivot_4, n):
                    temp_4 *= arr[a]

                temp = temp_1 + temp_2 + temp_3 + temp_4
                result = max(result, temp)
print(result)

