n, cnt = map(int, input().split())
arr = [0] * 10
result = -1
temp_cnt = 0

def recur(cur, sum):
    global cnt, temp_cnt, result
    if sum > n:
        return

    elif sum == n:
        temp_cnt += 1
        if temp_cnt == cnt:
            result = ""
            for i in range(cur - 1):
                print(arr[i], end="+")
            print(arr[cur-1])
            exit()
        return

    else:
        for i in range(1,4):
            arr[cur] = i
            recur(cur+1, sum+i)

recur(0, 0)
print(result)
