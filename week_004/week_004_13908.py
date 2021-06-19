n, m = map(int, input().split())
known_arr = list(map(int, input().split()))
base1 = known_arr[:]
for i in range(n-m):
    base1.append(0)
cnt = 0
visited = [False] * 10


def recur(cur):
    global cnt

    if cur == m:
        cnt += 1
        return

    for i in range(10):
        if visited[i]:
            continue


        base1[cur] = i
        recur(cur+1)

recur(0)
print(cnt)
