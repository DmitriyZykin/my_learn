'''a program that will calculate the number of trailing zeros in a factorial of a given number'''

def zeros(n):
    count_0 = 0
    for i in range(12):
        if n >= 5**(i+1):
            count_0 += n // 5**(i+1)
        else:
            break
    return count_0