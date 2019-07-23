"""
    Mistake : Did not recursively call merge sort on left and right sides in ms() function
"""
def ms(arr):

    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2

    left, right = ms(arr[:mid]), ms(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    left_pointer, right_pointer = 0, 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result
            


print(ms([15, 7, 6, 12]))
