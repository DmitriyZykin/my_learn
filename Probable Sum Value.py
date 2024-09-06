'''Find the Most Probable Sum Value or Values, in Rolling N-dice of n Sides'''


def most_prob_sum(dice, number_dice):
    dict_dice = {
        'tetrahedral': 4,
        'cubic': 6,
        'octahedral': 8,
        'ninesides': 9,
        'tensides': 10,
        'dodecahedral': 12,
        'icosahedral': 20
    }
    number_sides_die = dict_dice[dice]
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

    first_number = number_dice
    last_number = number_dice * number_sides_die
    list_sum.sort(reverse=True)
    if list_sum[0] == list_sum[1]:
        rez_number = [(first_number + last_number) // 2, (first_number + last_number) // 2 + 1]
    else:
        rez_number = [(first_number + last_number) // 2]
    rez_prob = max(list_sum) / number_sides_die ** number_dice

    return rez_number,rez_prob

