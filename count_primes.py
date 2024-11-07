'''A function that prints prime numbers and count their from 1 to num'''

def count_primes(num):

    if num < 2:
        return 0

    primes = [2]

    x = 3

    while x <= num:

        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2

    print(primes)
    return len(primes)

print(count_primes(100))