n = int(input())
base1 = list(map(str, input().split()))
base2 = [0] * (n+1)
visited = [False] * 10
cnt = 0
result = []

def recur(cur):
    if cur == (n+1):
        global cnt, result
        if cnt == 0:
            for i in range(cur):
                print(base2[i], end="")
            print("")
            cnt += 1
        result = base2
        return

    for i in range(10):
        if visited[i]:
            continue

        if cur >= 1:
            if base1[cur-1] == '<' and base2[cur-1] > base2[cur]:
                continue
            elif base1[cur-1] == '>' and base2[cur-1] < base2[cur]:
                continue

        visited[i] = True
        base2[cur] = i
        recur(cur+1)
        visited[i] = False

recur(0)
for i in range(n+1):
    print(result[i], end="")