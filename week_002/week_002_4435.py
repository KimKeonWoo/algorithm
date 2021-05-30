base1 = [1, 2, 3, 3, 4, 10]
base2 = [1, 2, 2, 2, 3, 5, 10]

n = int(input())
for take in range(n):
    gan = list(map(int, input().split()))
    sau = list(map(int, input().split()))

    total_gan = 0
    for i in range(len(gan)):
        total_gan += gan[i] * base1[i]

    total_sau = 0
    for i in range(len(sau)):
        total_sau += sau[i] * base2[i]

    if total_gan > total_sau:
        print("Battle %d: Good triumphs over Evil" % (take+1))
    elif total_gan == total_sau:
        print("Battle %d: No victor on this battle field" % (take+1))
    else:
        print("Battle %d: Evil eradicates all trace of Good" % (take+1))