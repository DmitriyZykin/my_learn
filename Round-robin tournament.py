'''A function build_matches_table that receives the number of teams
(always a positive and even number) and returns a matrix.'''

def matches(my_list):
    day = []
    for i in range(len(my_list)//2):
        day.append((my_list[i],my_list[-1-i]))
    return day

def build_matches_table(teams: int) -> list[list[(int, int)]]:
    my_list = []
    result = []
    for i in range(1,teams+1):
        my_list.append(i)
    print(my_list)
    result.append(matches(my_list))
    last_list = my_list
    while last_list[-1] != my_list[1]:
        last_list = [last_list[0]] + [last_list[-1]] + last_list[1:-1]
        result.append(matches(last_list))
        print(last_list)
    return result
print(build_matches_table(10))