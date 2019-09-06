def mergesort(arr):
    
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left, right = mergesort(arr[:mid]), mergesort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    lp, rp = 0, 0
    new_arr = []

    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            new_arr.append(left[lp])
            lp += 1
        else:
            new_arr.append(right[rp])
            rp += 1

    new_arr.extend(left[lp:])
    new_arr.extend(right[rp:])

    return new_arr


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


def binary_search(arr, low, high, x):

    guess = (low + high) // 2
        
    if arr[guess] == x:
        return guess

    if arr[guess] < x:
        return binary_search(arr, guess, high, x)
            
    elif arr[guess] > x:
        return binary_search(arr, low, guess, x)

    
arr = [5, 7, 2, 3, 1, 8, 10]
ms = mergesort(arr)
qs = quicksort(arr, 0, len(arr)-1)


print(qs)
print(ms)
print(binary_search(arr, 0, len(arr)- 1, 1))
