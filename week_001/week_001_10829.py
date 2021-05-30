n = int(input())
result = ""

while True:
    result += str(n % 2)
    n //= 2
    if n == 1:
        result += "1"
        break

print(result[::-1])