def bubble_sort(arr):
    
    """
        O(n^2)
        Moves to the rightand swaps the lower value to the left
        Outer loop controls number of times to run through the array
        Inner loop controls right movement and swaps
    """ 

    for i in range(len(arr)):
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def selection_sort(arr):
    
    """
        O(n^2)
        Holds a boundary, finds the lowest number to the right of the boundary, and swaps
        Outer loop controls the boundary
        Inner loop controls comparison of numbers to the right of the boundary and swaps
    """
        
    for boundary in range(0,len(arr)):
        min_index = boundary
        for j in range(boundary, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[boundary] = arr[boundary], arr[min_index]
    return arr

                
def insertion_sort(arr):
    
    """
        O(n^2)
        Compares number to the left and swaps if lower
        Outer loop controls number of iterations
        Inner Loop controls leftward movement 

    """
    
    for index in range(1, len(arr)):
        current_value = arr[index]
        compare_index = index - 1
        
        while compare_index >= 0 and current_value < arr[compare_index]:
            arr[compare_index + 1] = arr[compare_index]
            arr[compare_index] = current_value
            compare_index -= 1
            
    return arr


# O(n log n)

def merge_sort(arr):
    
    if len(arr) == 1:
        return arr 
    
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    return merge(left, right) 
    

def merge(left, right):
    
    sorted_arr = []
    left_pointer, right_pointer = 0, 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            sorted_arr.append(left[left_pointer])
            left_pointer += 1
        else:
            sorted_arr.append(right[right_pointer])
            right_pointer += 1

    while right_pointer < len(right):
        sorted_arr.append(right[right_pointer])
        right_pointer += 1
        
    while left_pointer < len(left):
        sorted_arr.append(left[left_pointer])
        left_pointer += 1

    return sorted_arr


arr = [10, 3, 5, 7, 1, 2]
bs = bubble_sort(arr)
arr = [10, 3, 5, 7, 1, 2]
ins = insertion_sort(arr)
arr = [10, 3, 5, 7, 1, 2]
ms = merge_sort(arr)
arr = [10, 3, 5, 7, 1, 2]
ss = selection_sort(arr)
print('bubble:', bs)
print('insert:', ins)
print('select:', ss)
print('merge:', ms)
