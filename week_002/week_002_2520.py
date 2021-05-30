n = int(input())
base_mix = [8, 8, 4, 1, 9]
base_top = [1, 30, 25, 10]

for _ in range(n):
    sibal = input()

    # c:우유, y:계란, su:설탕, sa:소금, f:밀가루
    arr = list(map(int, input().split()))
    can_mix = 1000010  # 가능한 재료 배수
    for i in range(len(arr)):
        if 0 <= arr[i] < 1000010:
            can_mix = min(can_mix, (arr[i] / base_mix[i]))
        else:
            can_mix = 0
            break

    # b:바나나, sg:딸기잼, cg:초코잼, w:호두
    arr = list(map(int, input().split()))
    can_top = 0 #가능한 토핑 갯수
    for i in range(len(arr)):
        if 0 <= arr[i] < 1000010:
            can_top += arr[i] // base_top[i]
        else:
            can_top = 0
            break

    print(min(can_top, int(can_mix * 16)))
