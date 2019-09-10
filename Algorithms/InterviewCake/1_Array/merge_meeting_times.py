def merge_ranges(arr):
    result = []
    arr = sorted(arr)
    for index in range(1, len(arr)):
        if arr[index-1][0] < arr[index][0] and arr[index-1][1] >= arr[index][0]:
            merged = merge(arr[index-1], arr[index])
            result.append(merged)
    return result

def merge(arr1, arr2):

    meeting2 = arr2[1]
    
    if arr1[1] > arr2[1]:
        meeting2 = arr1[1]
    
    new_arr = (arr1[0], meeting2)

    return new_arr

arr = [(1, 5), (2, 3)]
arr_2 = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

print(merge_ranges(arr))
print(merge_ranges(arr_2))
