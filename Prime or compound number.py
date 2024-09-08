'''A function that returns a prime or composite number'''

def prim_com(number):
    lst = [2,3,5]
    if number in lst:
        return 'Prime number'
    elif number % 2 == 0:
        return 'Composite number'
    else:
        x = 3
        while number**0.5+1 > x:
            if number % x == 0:
                break
            else:
                x += 2
        if number % x != 0:
            return 'Prime number'
        else:
            return 'Composite number'

