# Mistake: did not return merge(left,right) on the mergesort call

def mergesort(arr):
    
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    left, right = mergesort(arr[:mid]), mergesort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    
    lp, rp = 0, 0
    sorted_arr = []

    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            sorted_arr.append(left[lp])
            lp += 1
        else:
            sorted_arr.append(right[rp])
            rp += 1
            
    sorted_arr.extend(left[lp:])
    sorted_arr.extend(right[rp:])
    
    return sorted_arr
    

def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p-1)
        quicksort(arr, p+1, high)
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


def binary_search(arr, low, high, x):

    if low < high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid

        if arr[mid] < x:
            return binary_search(arr, mid, high, x)
        else:
            return binary_search(arr, low, mid, x)
    return 'does not exist'

    
arr = [5, 3, 2, 7, 8, 6, 9, 1]
ms = mergesort(arr)
qs = quicksort(arr, 0, len(arr) - 1)
print(ms)
print(qs)
bs = binary_search(ms, 0, len(arr) - 1, 3)
print(bs)
