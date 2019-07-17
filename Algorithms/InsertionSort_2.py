def insert_sort(arr):

    for index in range(1,len(arr)):
        current_value = arr[index]
        compare_index = index-1
        
        while compare_index >= 0 and current_value < arr[compare_index]:
            arr[compare_index + 1] = arr[compare_index]
            arr[compare_index] = current_value
            compare_index -= 1

    return arr


print(insert_sort([6, 7, 4, 3, 5, 2]))
