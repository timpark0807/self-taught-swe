def mergesort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left, right = mergesort(arr[:mid]), mergesort(arr[mid:])

    return merge(left,right)

def merge(left, right):
    result = []
    lp, rp = 0, 0

    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            result.append(left[lp])
            lp += 1
        else:
            result.append(right[rp])
            rp += 1

    result.extend(left[lp:])
    result.extend(right[rp:])

    return result


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

    if low < high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        
        if arr[mid] < x:
            return binarysearch(arr, mid, high, x)
        
        else:
            return binarysearch(arr, low, mid, x)
        
    else:
        return 'N/A'

arr = [5, 2, 1, 3, 4, 9, 7, 8, 6, 10]
qs = quicksort(arr, 0, len(arr)-1)
ms = mergesort(arr)
print(qs)
print(ms)
print(binarysearch(ms, 0, len(arr)-1, 9))
    
