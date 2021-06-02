def recur(cur):
    global cnt_min
    if cur == 4:
        if arr[0]**2 + arr[1]**2 + arr[2]**2 + arr[3]**2 == n:
            temp = 4
            for i in range(4):
                if arr[i] == 0:
                    temp -= 1
            print(temp)
            exit()
        return

    for i in range(cnt_loop): #루트(50000) ~= 250 #입력최대값이 5만임
        arr[cur] = i
        recur(cur + 1)


global cnt_min
global cnt_loop
n = int(input())
cnt_loop = round(n**0.5) + 2
arr = [0]* 4
recur(0)