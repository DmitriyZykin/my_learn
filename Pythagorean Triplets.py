''' Finding the Pythagorean triplets whose product is equal to n'''

def pythagorean_triplet(n):
    a = int(n ** (1 / 3))
    b = a + 1
    c = b + 1
    while a * a + b * b != c * c or a * b * c != n:
        if c > a + 2:
            if b > a + 1:
                a += 1
            else:
                b += 1
                a = int((n / c / b))
        else:
            c += 1
            b = int((n / c) ** (1 / 2))
            a = b - 1
    return [a,b,c]