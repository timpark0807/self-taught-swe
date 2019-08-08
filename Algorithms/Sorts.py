
def mergesort(arr):
    
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left, right = mergesort(arr[:mid]), mergesort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    lp, rp = 0, 0
    new = []

    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            new.append(left[lp])
            lp += 1
        else:
            new.append(right[rp])
            rp += 1

    new.extend(left[lp:])
    new.extend(right[rp:])

    return new

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

def binarysearch(arr, low, high, x):
    if low < high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binarysearch(arr, mid+1, high, x)
        else:
            return binarysearch(arr, low, mid-1, x)
    return 'Does not exist'

    
arr = [3, 4, 7, 1, 2, 5, 8, 10, 9]
ms = mergesort(arr)
qs = quicksort(arr, 0, len(arr)- 1)
print(ms)
print(qs)
bs = binarysearch(ms, 0, len(arr)-1, 1)
print(bs)
