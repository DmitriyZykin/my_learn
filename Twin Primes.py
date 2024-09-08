''' Function that counts the number of sets of twin primes from 1 to n.'''

def twin_prime(n):
    if n >= 4:
        num = 4
        number1 = 2
        number2 = -1
        count_twin = 2
        while num <= n+1:
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
                number2 = num
            if number1 + 2 == number2:
                count_twin += 1
            number1 = number2
            num += 1
        return count_twin
    else:
        return 0