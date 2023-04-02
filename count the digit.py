print("This program counts the number of digits in a given range of number")
def nb_dig(n, d):
    sum1 = 0
    alp = str(d)
    k = []
    for i in range(0, n + 1):
        k.append(str(i * i))
    k = "".join(k)
    k = list(k)
    for i in k:
        if alp in i:
            sum1 = sum1 + 1
    print(sum1)

nb_dig(int(input("Pls type the range of number you want ")), int(input("What digit do you want to count ")))