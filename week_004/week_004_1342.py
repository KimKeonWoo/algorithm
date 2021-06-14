arr = input()
n = len(arr)
base = [0] * n
visited = [False] * n
pre = ""
result_arr = []

def recur(cur):
    global pre

    if cur == n:
        temp = ""
        for i in range(n):
            temp += arr[base[i]]

        if temp in result_arr:
            return

        result_arr.append(temp)
        return

    else:
        for i in range(n):
            if visited[i]:
                continue

            if pre == arr[i]:
                continue

            visited[i] = True
            base[cur] = i
            pre = arr[i]
            recur(cur+1)
            visited[i] = False

recur(0)
print(len(result_arr))