n = int(input())
arr = [0] * n

def prime(num):
    if num // 10 == 0 and (num in [2, 3, 5, 7]):
        return True
    if num <= 1:
        return False
    if num % 2 == 0:
        return False

    temp = round(num ** 0.5) + 1
    for i in range(3, temp+1, 2):
        if num % i == 0:
            return False
    return True


def recur(cur):
    if cur == n:
        for i in range(n):
            print(arr[i], end="")
        print("")
        return

    for i in range(1, 10):
        temp = 0
        for j in range(cur):
            temp = temp*10 + arr[j]
        temp = temp*10 + i

        if not prime(temp):
            continue

        arr[cur] = i
        recur(cur+1)

recur(0)