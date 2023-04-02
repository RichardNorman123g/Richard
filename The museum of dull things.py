def remove_smallest(numbers):
    arr = []
    arr = arr + numbers
    if numbers == []:
        print([])
    else:
        num = min(arr)
        arr.remove(num)
        print(arr)

remove_smallest([163, 48, 10])