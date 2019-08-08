def qs(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        qs(arr, low, p-1)
        qs(arr, p+1, high)
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

def ms(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left, right = ms(arr[:mid]), ms(arr[mid:])
    return merge(left, right)

def merge(left, right):
    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    result.extend(right[right_pointer:])
    result.extend(left[left_pointer:])

    return result


arr = [100, 2, 54, 76, 3, 43, 65]
print(ms(arr))
print(qs(arr, 0, len(arr)-1))
