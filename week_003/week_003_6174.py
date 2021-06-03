base = ["1111", "2222", "3333", "4444", "5555", "6666", "7777","8888","9999"]

m = int(input())
for _ in range(m):
    n = input()
    if n in base:
        break

    temp = n
    cnt = 0
    while True:
        if temp == "6174":
            break

        arr = []
        for i in temp:
            arr.append(int(i))

        arr_asc = arr[:]
        arr_desc = arr[:]
        arr_asc.sort()
        arr_desc.sort(reverse=True)

        desc = arr_desc[0] * 1000 + arr_desc[1] * 100 + arr_desc[2] * 10 + arr_desc[3]
        asc = arr_asc[0] * 1000 + arr_asc[1] * 100 + arr_asc[2] * 10 + arr_asc[3]
        temp = desc - asc
        temp = str(temp)
        for i in range(4):
            if len(temp) == 4:
                break
            temp = "0" + temp

        cnt += 1
    print(cnt)

