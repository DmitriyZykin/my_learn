'''A function that prints prime numbers from 1 to n'''

def prime(n):
    print(2)
    print(3)
    print(5)
    num = 7
    while num <= n:
        if num % 2 == 0:
            num += 1
            continue
        x = 3
        while num**0.5+1 > x:
            if num % x == 0:
                break
            else:
                x += 2
        if num % x != 0:
            print(num)
        num += 1

