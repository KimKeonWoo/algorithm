pre_ans_arr = []
for i in range(123, 988):
    num_str = str(i)
    pre_ans_arr.append(num_str)

n = int(input())

for _ in range(n):
    ans, cnt_stk, cnt_ball = map(int, input().split())
    ans_str = str(ans)

    now_ans_arr = []
    for i in range(123, 988):
        num_str = str(i)
        temp_stk = 0
        temp_ball = 0

        if num_str[0] == '0' or num_str[1] == '0' or num_str[2] == '0':
            continue
        if num_str[0] == num_str[1] or num_str[0] == num_str[2] or num_str[1] == num_str[2]:
            continue

        for j in range(3):
            for k in range(3):
                if j == k and ans_str[j] == num_str[k]:
                    temp_stk += 1
                elif ans_str[j] == num_str[k]:
                    temp_ball += 1

        if cnt_stk == temp_stk and cnt_ball == temp_ball:
            try:
                if pre_ans_arr.index(num_str) >= 0:
                    now_ans_arr.append(num_str)
            except ValueError:
                continue
    pre_ans_arr = now_ans_arr
    now_ans_arr = []

print(len(pre_ans_arr))