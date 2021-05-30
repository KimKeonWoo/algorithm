base = "CAMBRIDGE"
n = input()

for i in n:
    for j in base:
        if i == j:
            n = n.replace(j, "")

print(n)
