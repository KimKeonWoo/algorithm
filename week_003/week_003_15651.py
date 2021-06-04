arr = [0] * 100
n, m = map(int, input().split())


def recur(cur):
    #n까지
    if cur == n:
        for i in range(n):
            print(arr[i], end=" ")
        print("")
        return

    for i in range(m):
        arr[i] = cur
        recur(cur + 1)

recur(1)