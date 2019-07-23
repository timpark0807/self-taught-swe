# mistake called merge sort on the quick sort recursive function

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
            arr[boundary], arr[index] = arr[index], arr[boundary]
            boundary += 1

    arr[boundary], arr[high] = arr[high], arr[boundary]

    return boundary


arr = [12, 3, 7, 32, 44, 1, 67]
n = len(arr) 
result = quick_sort(arr, 0, n-1)
print(result)
    
    
