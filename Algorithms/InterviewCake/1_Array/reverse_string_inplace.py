def reverse_list_inplace(arr):
    start, end = 0, len(arr)-1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

arr = ['d', 'e', 'n', 'v', 'a']
reverse_list_inplace(arr)
