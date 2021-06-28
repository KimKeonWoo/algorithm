n = int(input())
base = list(map(int, input().split()))
index = [0 for i in range(n)]
result = 0
visited = [False for i in range(n)]

def max_dif(index_arr):
    temp = []
    for i in index_arr:
        temp.append(base[i])

    sum = 0
    for i in range(len(temp) - 1):
        sum += abs(temp[i] - temp[i+1])
    return sum


def recur(cur):
    global result
    if cur == n:
        result = max(result, max_dif(index))
        return

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        index[cur] = i
        recur(cur+1)
        visited[i] = False

recur(0)
print(result)