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
            arr[index], arr[boundary] = arr[boundary], arr[index]
            boundary += 1

    arr[boundary], arr[high] = arr[high], arr[boundary]

    return boundary

def bs(arr, low, high, x):
    mid = (low+high) // 2
    
    if arr[mid] == x:
        return mid
    
    elif arr[mid] < x:
        return bs(arr, mid, high, x)
    
    elif arr[mid] > x:
        return bs(arr, low, mid, x)
    
arr = [10, 4, 6, 7, 2, 3]
ms = mergesort(arr)
qs = quicksort(arr, 0, len(arr) - 1)
print(ms)
print(qs)
print(bs(ms, 0, len(arr)-1, 7))
