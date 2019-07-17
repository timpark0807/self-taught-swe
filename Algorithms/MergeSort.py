def merge_sort(arr):
    
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):

    new_list = []    
    left_pointer, right_pointer = 0, 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            new_list.append(left[left_pointer])
            left_pointer += 1
        else:
            new_list.append(right[right_pointer])
            right_pointer += 1
            
    new_list.extend(left[left_pointer:])
    new_list.extend(right[right_pointer:])

    return new_list

print(merge_sort([12, 4, 13, 2]))
