n = int(input())
base = []
choice = []
result = 999999

for _ in range(n):
    temp = list(map(int, input().split()))
    base.append(temp)

def recur(cur, cnt):
    global result

    if cur == n or cnt == n:
        sour = 1
        bitter = 0
        for i in range(len(choice)):
            sour *= choice[i][0]
            bitter += choice[i][1]

        if sour == 1 and bitter == 0:
            return
        result = min(result, abs(bitter - sour))
        return

    choice.append(base[cur])
    recur(cur+1, cnt+1)
    choice.pop()
    recur(cur+1, cnt)

recur(0, 0)
print(result)