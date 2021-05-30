def calc_dist(x, y):
    dist_x = abs(x - x_s)
    dist_y = abs(y - y_s)
    return (dist_x ** 2) + (dist_y ** 2)



x_s, y_s = map(int, input().split())
x_e, y_e, dx, dy = map(int, input().split())

dx = dx / 1000
dy = dy / 1000

temp_x = x_e
temp_y = y_e
result = calc_dist(x_e, y_e)
while True:
    #print(temp_x, temp_y, result, end=" || ")
    temp = calc_dist(temp_x + dx, temp_y + dy)
    #print((temp_x+dx), (temp_y+dy), temp)
    if result < temp:
        break

    result = temp
    temp_x += dx
    temp_y += dy

print(round(temp_x), round(temp_y))
