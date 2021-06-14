n = int(input())
base1 = list(map(int, input().split()))
base2 = [0] * n
visited = [False] * n
result = 0

def recur(cur):
    global result

    if cur == n:
        temp = 0
        for i in range(0, n, 2):
            temp += abs(base1[base2[i]] - base1[base2[i+1]])
        #     print(base1[base2[i]], end=" ")
        #     print(base1[base2[i + 1]], end=" ")
        # print("    ||    ", end="")
        # print(temp, end=" ")
        # print(result)
        result = max(result, temp)
        return

    else:
        for i in range(n):
            if visited[i]:
                continue

            visited[i] = True
            base2[cur] = i
            recur(cur+1)
            visited[i] = False

recur(0)
print(result)