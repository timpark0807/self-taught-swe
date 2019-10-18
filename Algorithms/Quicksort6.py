def quicksort(arr, low, high):
    if low < high:
        
        p = partition(arr, low, high)
        quicksort(arr, low, p-1)
        quicksort(arr, p+1, high)

    return arr


def partition(arr, low, high):
    pivot = arr[high]
    boundary = low
    while low < high:
        if arr[low] < pivot:
            arr[boundary], arr[low] = arr[low], arr[boundary]
            boundary += 1
        low += 1
            
    arr[boundary], arr[high] = arr[high], arr[boundary]

    return boundary 

def mergesort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    output = []
    lp = 0
    rp = 0

    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            output.append(left[lp])
            lp += 1
        else:
            output.append(right[rp])

    output.extend(left[lp:])
    output.extend(right[rp:])

    return output 


arr = [10, 7, 3, 5, 6, 2, 8, 9]
low = 0
high = len(arr) - 1
answer = quicksort(arr, low, high)
answer2 = mergesort(arr)
print(answer)
print(answer2)

