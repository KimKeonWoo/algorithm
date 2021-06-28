n = int(input())
arr_sign = list(map(str, input().split()))
arr = [0 for i in range(n+1)]
visited = [False for i in range(10)]
flag = True
first = []
last = []

def recur(cur):
    global flag, first, last

    if cur == n+1:
        if flag:
            first = arr[:]
            flag = False
        else:
            last = arr[:]
        return

    for i in range(10):
        if visited[i]:
            continue

        arr[cur] = i

        if 0 < cur:
            if arr_sign[cur - 1] == '<' and arr[cur - 1] > arr[cur]:
                continue
            elif arr_sign[cur - 1] == '>' and arr[cur - 1] < arr[cur]:
                continue

        visited[i] = True
        recur(cur+1)
        visited[i] = False

recur(0)
for i in range(n + 1):
    print(last[i], end="")
print("")
for i in range(n + 1):
    print(first[i], end="")
