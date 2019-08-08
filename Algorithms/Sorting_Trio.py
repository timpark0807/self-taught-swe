def bs(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr

ans = bs([10, 15, 5, 9, 1])
print(ans)

def select_sort(arr):
    
    for boundary in range(len(arr)):
        min_index = boundary
        
        for num in range(boundary, len(arr)):
            if arr[num] < arr[min_index]:
                min_index = num


        arr[boundary], arr[min_index] = arr[min_index], arr[boundary]

    return arr

ans2 = select_sort([10, 15, 5, 9, 1])
print(ans2)


def insertion_sort(arr):
    
    for key in range(1, len(arr)):
        current_value = arr[key]
        compare_index = key -1

        while compare_index > 0:
            if arr[compare_index] > current_value:
                arr[compare_index], arr[compare_index + 1] = arr[compare_index + 1], arr[compare_index]
                compare_index -= 1
    return arr


ans3 = select_sort([10, 15, 5, 9, 1])
print(ans3)

