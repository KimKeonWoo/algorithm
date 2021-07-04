dp = []
for _ in range(9):
    temp_input = input()
    temp_arr = []
    for i in temp_input:
        temp_arr.append(int(i))
    dp.append(temp_arr)

#해당 값이 이미 존재하면 True
def check_unit(cnt, h, y):
    temp_h = h // 3
    temp_y = y // 3
    for a in range(temp_h * 3, 3):
        for b in range(temp_y * 3, 3):
            if cnt == dp[a][b]:
                return True
    return False

#해당 값이 이미 존재하면 True
def check_all(cnt, h, y):
    # 해당 행에 존재하는지
    if cnt in dp[h]:
        return True
    # 해당 열에 존재하는지
    if cnt in dp[y]:
        return True
    # 해당 3x3에 존재하는지
    if check_unit(cnt, h, y):
        return True

def recur(cur, h, y):
    if cur == 81:
        print(dp)
        return

    for i in range(10):
        if dp[h][y] != 0:
            recur(cur+1, h, y)

        dp[h][y] = i
        if check_all(dp[h][y], h, y):
            continue
        if y + 1 == 9:
            recur(cur+1, h+1, 0)
        else:
            recur(cur+1, h, y+1)
        dp[h][y] = 0
    return

if dp[0][0] == 0:
    recur(0, 0, 0)
else:
    for i in range(10):
        dp[0][1] = i
        if check_all(dp[0][1], 0, 1):
            continue
        recur(2, 0, 2)
        dp[0][1] = 0
