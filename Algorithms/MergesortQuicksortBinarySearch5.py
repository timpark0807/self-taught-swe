def mergesort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    left, right = mergesort(arr[:mid]), mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    new_arr = []
    lp, rp = 0, 0

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
        p = partition(arr,low,high)
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

arr = [10, 4, 7, 3, 2, 1, 8, 9]


print(mergesort(arr))
print(quicksort(arr, 0, len(arr)-1))


