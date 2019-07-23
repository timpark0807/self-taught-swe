def merge_sort(arr):
    
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    
    left_pointer, right_pointer = 0, 0
    result = []
    
    while left_pointer < len(left) and right_pointer < len(left):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result


def binary_search(arr, answer):
    low = arr[0]
    high = arr[len(arr)-1]
    guess = 0

    while guess != answer:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess < answer:
            low = arr[mid]
        elif guess > answer: 
            high = arr[mid]

    return guess


    

sorted_arr = merge_sort([9, 8, 7, 6, 10, 3, 4, 2, 5, 1])

print(sorted_arr)
binary_search(sorted_arr, 4)
