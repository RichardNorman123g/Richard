print("Hey this program converts any number that has been \
put inside the program in descending order")
def descending_order(num):
    num3 = ""
    arr = []
    number = str(num)
    for i in number:
        arr.append(i)
    num1 = (sorted(arr, reverse=True))
    num2 = num3.join(num1)
    print(int(num2))

descending_order(int(input("type in the number you want to convert ")))