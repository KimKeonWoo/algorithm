n, m = map(int, input().split())
base1 = list(map(int, input().split()))
base1.sort()
base2 = []
visited = [False] * n

for i in range(len(base1)):
    base2.append(i)

def recur(cur):
    if cur == m:
        for i in range(m):
            print(base1[base2[i]], end=" ")
        print("")
        return

    else:
        for i in range(n):
            if visited[i] == True:
                continue

            visited[i] = True
            base2[cur] = i
            recur(cur+1)
            visited[i] = False

recur(0)