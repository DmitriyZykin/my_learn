'''The game of tic tac toe'''


def grid(value):
    print('\n')
    print(str(value[7] + '|' + value[8] + '|' + value[9]))
    print('-----')
    print(str(value[4] + '|' + value[5] + '|' + value[6]))
    print('-----')
    print(str(value[1] + '|' + value[2] + '|' + value[3]))
    return '\n'



def vin(list_xo, X_O):
    if list_xo[7] == X_O and list_xo[8] == X_O and list_xo[9] == X_O or \
        list_xo[4] == X_O and list_xo[5] == X_O and list_xo[6] == X_O or \
        list_xo[1] == X_O and list_xo[2] == X_O and list_xo[3] == X_O or \
        list_xo[7] == X_O and list_xo[4] == X_O and list_xo[1] == X_O or \
        list_xo[8] == X_O and list_xo[5] == X_O and list_xo[2] == X_O or \
        list_xo[9] == X_O and list_xo[6] == X_O and list_xo[3] == X_O or \
        list_xo[7] == X_O and list_xo[5] == X_O and list_xo[3] == X_O or \
        list_xo[9] == X_O and list_xo[5] == X_O and list_xo[1] == X_O:
        return 1
    return 0

def draw(list_xo):
    if list_xo[7] != ' ' and list_xo[8] != ' ' and list_xo[9] != ' ' and \
        list_xo[4] != ' ' and list_xo[5] != ' ' and list_xo[6] != ' ' and \
        list_xo[1] != ' ' and list_xo[2] != ' ' and list_xo[3] != ' ':
        return 1
    return 0

def play(X,O,list_moves,new_list):
    new_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    values = [' ', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
    for i in range(1,10):
        num = 0
        while num not in range(1,10):
            num_str = input(f"Ход игрока {list_moves[i]} ")
            if num_str.isdigit():
                num = int(num_str)
            else:
                continue
            if new_list[num] != ' ':
                print("Это поле уже занято")
                num = 0
                continue
        new_list[num] = values[i]
        print(grid(new_list))
        if vin(new_list,'X'):
            return f"Победа игрока {X}"
        if vin(new_list, 'O'):
            return f"Победа игрока {O}"
        if draw(new_list):
            return "Ничья"

my_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
answer = ''
marker = ''
print(grid(my_list))
while answer != 'да' and answer != 'нет':
    answer = input("Хотите сыграть в крестики-нолики? ").lower()
while answer == 'да':
    while marker != 'х' and marker != 'о':
        marker = input("Игрок 1 выберите Х или О: ").lower()
    if marker == 'х':
        x = 1
        o = 2
        moves = ['','1','2','1','2','1','2','1','2','1']
    else:
        x = 2
        o = 1
        moves = ['','2','1','2','1','2','1','2','1','2']

    print(play(x,o,moves,my_list))
    answer = ''
    marker = ''
    while answer != 'да' and answer != 'нет':
        answer = input("Хотите сыграть ещё? ").lower()

print("Пока")
