'''Probabilities for Sums in Rolling Cubic Dice with 6 Faces'''

def rolldice_sum_prob(sum_, dice_amount):

    if sum_ > dice_amount * 6 or sum_ < dice_amount:
        return 0
    else:

        matrix_numbers = []
        list_numbers = [1, 2, 3, 4, 5, 6]
        list_sum = [1, 1, 1, 1, 1, 1]
        count_cube = 1

        while count_cube < dice_amount:
            matrix_numbers.clear()
            matrix_numbers.append(list_sum + [0] + [0] + [0] + [0] + [0])
            matrix_numbers.append([0] + list_sum + [0] + [0] + [0] + [0])
            matrix_numbers.append([0] + [0] + list_sum + [0] + [0] + [0])
            matrix_numbers.append([0] + [0] + [0] + list_sum + [0] + [0])
            matrix_numbers.append([0] + [0] + [0] + [0] + list_sum + [0])
            matrix_numbers.append([0] + [0] + [0] + [0] + [0] + list_sum)
            list_sum.clear()
            for i in range(len(matrix_numbers[0])):
                summ = 0
                for j in range(6):
                    summ += matrix_numbers[j][i]
                list_sum.append(summ)
            count_cube += 1
            fist_num_c = list_numbers[0]
            list_numbers.clear()
            for h in range(fist_num_c + 1, count_cube * 6 + 1):
                list_numbers.append(h)

        idx = list_numbers.index(sum_)
        rez = list_sum[idx] / 6 ** dice_amount

        return rez