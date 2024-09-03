'''Probabilities for Sums in Rolling Cubic Dice'''

def rolldice_sum_prob(sum_, dice_amount):

    if sum_ > dice_amount * 6 or sum_ < dice_amount:
        return 0
    else:

        mat_s = []
        c = [1, 2, 3, 4, 5, 6]
        s = [1, 1, 1, 1, 1, 1]
        k = 1

        while k < dice_amount:
            mat_s.clear()
            mat_s.append(s + [0] + [0] + [0] + [0] + [0])
            mat_s.append([0] + s + [0] + [0] + [0] + [0])
            mat_s.append([0] + [0] + s + [0] + [0] + [0])
            mat_s.append([0] + [0] + [0] + s + [0] + [0])
            mat_s.append([0] + [0] + [0] + [0] + s + [0])
            mat_s.append([0] + [0] + [0] + [0] + [0] + s)
            s.clear()
            for i in range(len(mat_s[0])):
                summ = 0
                for j in range(6):
                    summ += mat_s[j][i]
                s.append(summ)
            k += 1
            fist_num_c = c[0]
            c.clear()
            for h in range(fist_num_c + 1, k * 6 + 1):
                c.append(h)

        idx = c.index(sum_)
        rez = s[idx] / 6 ** dice_amount