n = int(input())

for _ in range(n):
    arr = input()
    cnt = 0

    # pivot_1 : 비교할 문자열을 자르는 인덱스 시작지점
    for pivot_1 in range(len(arr)):

        # pivot_2 : 비교할 문자열을 자르는 인덱스 끝지점
        sub_arr = ""
        for pivot_2 in range(pivot_1, len(arr)):
            sub_arr += arr[pivot_2]

        temp_pre = -1
        for i in sub_arr:
            if i == temp_pre:
                break

            print("%s || %s || %s" % (sub_arr, temp_pre, i), end="  ####  ")
            if i == "?":
                if temp_pre == "0":
                    temp_pre = "1"
                elif temp_pre == "1":
                    temp_pre = "0"
                cnt += 1

            elif i != temp_pre:
                temp_pre = i
                cnt += 1
            print(temp_pre)

    print(cnt)

1
10
1?
101
10?
1?1
1??
