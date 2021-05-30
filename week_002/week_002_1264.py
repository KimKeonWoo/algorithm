base = "aeiou"

while True:
    count = 0
    temp = input()
    temp = temp.replace(" ", "")
    temp = temp.lower()
    if temp == "#":
        break
    for i in temp:
        for j in base:
            if i == j:
                count += 1
    print(count)