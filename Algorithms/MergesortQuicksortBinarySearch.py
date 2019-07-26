def merge_sort(arr):
    
    if len(arr) < 2:
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

    new_list.extend(left[left_pointer:])
    new_list.extend(right[right_pointer:])

    return new_list

    
def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)
    return arr 

def partition(arr, low, high):
    pivot = arr[high]
    boundary = low

    for index in range(low, high):
        if arr[index] < pivot:
            arr[index], arr[boundary] = arr[boundary], arr[index]
            boundary += 1

    arr[boundary], arr[high] = arr[high], arr[boundary]

    return boundary


def binary_search(arr, low, high, ans):
    
    mid = (low+high) // 2
    
    if arr[mid] == ans:
        return mid

    if arr[mid] < ans:
        return binary_search(arr, mid + 1, high, ans)
    else:
        return binary_search(arr, low, mid-1, ans) 


    return mid 


arr = [1, 4, 5, 7, 9, 3, 2, 6, 8]
ms = merge_sort(arr)
qs = quick_sort(arr, 0, len(arr)-1)


re = binary_search(ms, 0, len(arr) - 1, 3)
re2 = binary_search(qs, 0, len(arr) - 1, 3)     
print(re, re2)
    
