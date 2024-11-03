''' If the value is present in the sorted array, the function returns its position '''

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low < high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess < item:
            low = mid
        elif guess > item:
            high = mid
        else:
            return mid
    return "The element is not in the list"

my_list = [1,3,5,7,9]
print(binary_search(my_list,-3))