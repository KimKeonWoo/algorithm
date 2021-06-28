base = input()
n = len(base)
arr_index = []
result = []

def recur(cur, cnt):

    if cnt == n:
        return

    result.append(cur)
    recur(cur)