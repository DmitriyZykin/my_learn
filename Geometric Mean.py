''' The function geometric_meanI(), (geometricMeanI javascript)that receives an array
 with the different values of the variable and outputs the geometric mean value.
The negative values and strings will be discarded for the calculations.'''

def geometric_meanI(arr):
    count_num = 0
    count_not_num = 0
    mul_num = 1
    for i in arr:
        if type(i) is int and i >= 0:
            mul_num *= i
            count_num += 1
        else:
            count_not_num += 1
    if (count_num >= 2 and count_num <= 10 and count_not_num <= 1 or
            count_num >= 11 and count_num + count_not_num >= count_not_num * 10):
        return mul_num ** (1/count_num)
    else:
        return 0




# For large values

def geometric_meanII(arr):
    count_num = 0
    count_not_num = 0
    mul_num = 1
    for i in arr:
        if type(i) is int and i >= 0:
            count_num += 1
        else:
            count_not_num += 1
    if (count_num < 2 or count_num >= 2 and count_num <= 10 and count_not_num > 1 or
            count_num >= 11 and count_num + count_not_num < count_not_num * 10):
        return 0
    else:
        for i in arr:
            if type(i) is int and i >= 0:
                mul_num *= i ** (1 / count_num)
        return mul_num

