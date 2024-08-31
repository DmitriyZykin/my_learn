'''find the largest pronic number'''


def next_smaller_pronic(n):
    num = (n**0.5)
    int_num = int(num)
    if num % int_num > 0.5:
        return int_num * (int_num + 1)
    else: 
        return int_num * (int_num - 1)