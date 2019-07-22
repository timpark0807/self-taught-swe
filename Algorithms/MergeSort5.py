def merge_sort(arr):

    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):

    left_pointer, right_pointer = 0, 0
    new_list = []

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            new_list.append(left[left_pointer])
            left_pointer += 1
        else:
            new_list.append(right[right_pointer])
            right_pointer += 1

    while left_pointer < len(left):
        new_list.append(left[left_pointer])
        left_pointer += 1
    while right_pointer < len(right):
        new_list.append(right[right_pointer])
        right_pointer += 1

    return new_list

arr = [10, 34, 4, 76, 5]
print(merge_sort(arr))
