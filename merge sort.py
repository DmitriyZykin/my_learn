

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left,right)

def merge(left,right):
    left_index, right_index = 0, 0
    length_left = len(left)
    length_right = len(right)
    sort_list = []
    while left_index < length_left and right_index < length_right:
        if left[left_index] <= right[right_index]:
            sort_list.append(left[left_index])
            left_index += 1
        else:
            sort_list.append(right[right_index])
            right_index += 1
    if left_index < length_left:
        for left_index in range(left_index,length_left):
            sort_list.append(left[left_index])
    elif right_index < length_right:
        for right_index in range(right_index,length_right):
            sort_list.append(right[right_index])
    return sort_list

print(merge_sort([8,4,3,7,2,9,1,6,5]))