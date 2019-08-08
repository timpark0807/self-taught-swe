def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

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
            rp+= 1

    new_list.extend(left[lp:])
    new_list.extend(right[rp:])

    return new_list


def binary_search(arr, num):
    high = len(arr) - 1
    low = 0
    mid = (high + low) // 2

    while arr[mid] != num:
        mid = (high + low) // 2
        if arr[mid] < num:
            low = arr[mid]
        else:
            high = arr[mid]

    return arr[mid]

def rec_binary_search(arr, num):
    

arr = [10, 1, 5, 7, 3, 2, 4, 9, 8]
print(merge_sort(arr))


