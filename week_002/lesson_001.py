d, m = map(int, input().split())
n = 0
arr1 = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
arr_m = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, m):
    n += arr_m[i]

n += d
result = arr1[n % 7]
print(result)
