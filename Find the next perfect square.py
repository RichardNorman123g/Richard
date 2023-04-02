print("The following code return the next perfect square of a desired number")
print("If it doesn't have a 'next perfect square' it return -1")
import math
def find_next_square(sq):
    num = math.sqrt(sq)
    if num % 1 == 0:
        print(int((num + 1) ** 2))
    else:
        print(-1)

find_next_square(int(input("Pls type a number ")))