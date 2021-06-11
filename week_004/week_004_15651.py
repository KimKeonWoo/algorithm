n, m = map(int, input().split())
arr = [0] * 100

def recur(cur):
    if cur == m:
        for i in range(m):
            print(arr[i], end=" ")
        print("")
        return

    else:
        for i in range(1, n+1):
            arr[cur] = i
            recur(cur+1)

recur(0)