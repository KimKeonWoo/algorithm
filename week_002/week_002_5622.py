base1 = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
base2 = ['', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0

n = input()
for i in n:
    for j in range(len(base2)):
        for k in base2[j]:
            if k == i:
                result += base1[j]
print(result)