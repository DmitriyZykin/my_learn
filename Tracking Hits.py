'''Tracking Hits for Different Sum Values for Different Kinds of Dice'''

def reg_sum_hits(number_dice, number_sides_die):
    matrix_numbers = []
    count_dice = 1
    list_sum = []
    list_numbers = []
    for k in range(number_sides_die):
        list_sum.append(1)
        list_numbers.append(k+1)

    while count_dice < number_dice:

        matrix_numbers.clear()
        for h in range(number_sides_die):
            matrix_numbers.append([0]*h + list_sum + [0]*(number_sides_die-1-h))

        list_sum.clear()
        for i in range(len(matrix_numbers[0])):
            summ = 0
            for j in range(number_sides_die):
                summ += matrix_numbers[j][i]
            list_sum.append(summ)

        count_dice += 1
        fist_number = list_numbers[0]
        list_numbers.clear()
        for f in range(fist_number + 1, count_dice * number_sides_die + 1):
            list_numbers.append(f)

    rez = []
    for g in range(len(list_sum)):
        rez.append([list_numbers[g],list_sum[g]])
    return rez



