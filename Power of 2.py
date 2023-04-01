print("hey this program takes an array and returns the square of those numbers")
def powers_of_two(n):
    arr = []
    for i in range(n+1):
        arr.append(2 ** i)



    print("the square of the numbers you types are ", arr)

ans = powers_of_two(int(input("pls type the numbers you want ")))