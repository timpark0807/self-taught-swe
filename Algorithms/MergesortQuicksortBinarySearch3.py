def mergesort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left, right = mergesort(arr[:mid]), mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    lp, rp = 0, 0
    new_list = []
    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            new_list.append(left[lp])
            lp += 1
        else:
            new_list.append(right[rp])
            rp += 1

    new_list.extend(left[lp:])
    new_list.extend(right[rp:])

    return new_list

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
            arr[boundary], arr[index] = arr[index], arr[boundary]
            boundary += 1

    arr[boundary], arr[high] = arr[high], arr[boundary]
    return boundary

def binarysearch(arr, low, high, x):
    mid = (low + high) // 2
    
    if arr[mid] == x:
        return mid

    if arr[mid] < x:
        return binarysearch(arr, mid + 1, high, x)

    if arr[mid] > x:
        return binarysearch(arr, low, mid-1, x)

arr = [0, 4, 3, 5, 2, 1]
ms = mergesort(arr)
qs = quicksort(arr, 0, len(arr) - 1)
print(ms, qs)

bs = binarysearch(ms, 0, len(arr) - 1, 4)
print(bs)
