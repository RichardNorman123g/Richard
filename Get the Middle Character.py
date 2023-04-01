print("Hi welcome to Get the middle character")
print("It is a program which can get the middle of any character you want")
def get_middle(s):
    word = len(s)
    if word == 1:
        print("The middle character is " +"'" + s + "'")
    if word % 2 == 0:
        middle = word // 2
        print("The middle character is " +"'"+ s[middle - 1] + s[middle] + "'")
    elif word % 2 != 0 and word != 1:
        middle = word // 2
        print("The middle character is " +"'"+ s[middle]+"'")
    
word = get_middle(input("type a word "))
