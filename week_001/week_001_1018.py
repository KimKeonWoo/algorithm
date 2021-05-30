n, m = map(int, input().split()) #n:세로, m:가로
board = []

for a in range(n):
    board.append(input())

count_W = 0
count_B = 0
result = 1000010


#예외처리 - 범위값 외 입력시 결과는 항상 0
if not((n >= 8 and n <= 50) and (m >= 8 and m <= 50)):
    print("범위 초과")
    result = 0

#단위 체스판(8x8)을 주어진 행렬(mxn)만큼 반복
for i in range(n-7):
    for j in range(m-7):

        #단위 사각형(2x2)의 1,1 ~ 2,2 까지의 비교(8x8체스판 크기만큼)
        for b_i in range(0,8,2):
            for b_j in range(0,8,2):
                #단위 체스판(8x8)의 0,0 지점의 값을 "W"로 가정한 경우
                if board[i + b_i][j + b_j] != "W":
                    count_W += 1
                if board[i + b_i][j + b_j + 1] == "W":
                    count_W += 1
                if board[i + b_i + 1][j + b_j] == "W":
                    count_W += 1
                if board[i + b_i + 1][j + b_j + 1] != "W":
                    count_W += 1

                # 단위 체스판(8x8)의 0,0 지점의 값을 "B"로 가정한 경우
                if board[i + b_i][j + b_j] != "B":
                    count_B += 1
                if board[i + b_i][j + b_j + 1] == "B":
                    count_B += 1
                if board[i + b_i + 1][j + b_j] == "B":
                    count_B += 1
                if board[i + b_i + 1][j + b_j + 1] != "B":
                    count_B += 1

        result = min(result, min(count_W, count_B))
        count_B = 0
        count_W = 0

print(result)
