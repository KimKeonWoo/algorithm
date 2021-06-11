n, m = map(int, input().split())
arr = [0] * 10
visited = [False] * (n+1)

def recur(cur):
    if cur == m:
        for i in range(0, m):
            print(arr[i], end=" ")
        print("")
        return

    for i in range(1, n+1):
        if visited[i]:
            continue

        visited[i] = True
        arr[cur] = i
        recur(cur + 1)
        visited[i] = False

recur(0)