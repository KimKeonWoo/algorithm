n, m = map(int, input().split())
base1 = list(map(int, input().split()))
base1.sort()
base2 = [0] * len(base1)

def recur(cur):
    if cur == m:
        for i in range(m):
            print(base1[base2[i]], end=" ")
        print("")
        return

    else:
        for i in range(n):
            base2[cur] = i
            recur(cur+1)

recur(0)