base_m = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
base_d = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
d, m = map(int, input().split())

temp = 0
for i in range(m):
    temp += base_m[i]
temp += d

print(base_d[temp%7])