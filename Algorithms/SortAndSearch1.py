# mistake: quick_sort infinite loop because I did not initialize boundary = low.

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    left_pointer, right_pointer = 0, 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            sorted_arr.append(left[left_pointer])
            left_pointer += 1
        else:
            sorted_arr.append(right[right_pointer])
            right_pointer += 1

    sorted_arr.extend(left[left_pointer:])
    sorted_arr.extend(right[right_pointer:])

    return sorted_arr


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)
    return arr          

def partition(arr, low, high):
    boundary = low
    pivot = arr[high]
    for index in range(low, high):
        if arr[index] < pivot:
            arr[index], arr[boundary] = arr[boundary], arr[index]
            boundary += 1
    arr[boundary], arr[high] = arr[high], arr[boundary]
    return boundary 


def binary_search(arr, low, high, x):
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr, mid+1, high, x)
        else:
            return binary_search(arr, low, mid-1, x)
    return 'Does not exist'
        
arr = [1, 8, 4, 3, 2, 6, 10, 7, 9, 5]
n = len(arr)
ms = merge_sort(arr)
qs = quick_sort(arr, 0, n-1)
print(ms)
print(qs)

ms_sort = binary_search(ms, 0, n-1, 3)
qs_sort = binary_search(qs, 0, n-1, 3)

print(ms_sort)
print(qs_sort)
                              




                              
            
