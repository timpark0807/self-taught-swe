"""
    Quick Sort
    O(n log n)
    
    Quick Sort is a recursive divide and conquer algorithm.
    
    We can break the algorithm into two functions
    1. The quicksort function
        - Contains the base case, partition function, and the recursive quicksort calls around the partition element
    2. The partition function 
        - Places numbers less than the pivot to the left
        - Places numbers greater than the pivot to the right
        - Now the pivot element is in its sorted position

    The quicksort function follows: 
    1. Set base case to if low < high:
        - Recursion will continue until there is 1 element in the recursive call
    2. Call the partition function on the arr
        - p = partition(arr, low, high)
    3. Recursively call quicksort on the left side of the partition
        - quicksort(arr, low, p-1)
    4. Recurisvely call quicksort on the right side of the partition
        - quicksort(arr, p+1, high)
    5. Return array when base case executes

    The partition function follows: 
    1. Choose a pivot element
        - This case will be right most element
        - pivot = arr[high]
    2. Initialize a boundary to track position of elements less than the pivot
        - boundary = low
    3. Iterate through the array and compare the current iteration to the pivot
        - if current iteration is less than the pivot, we must move it to the left side of the pivot
            - swap value of the current iteration with the value at the boundary
            - increment boundary by 1
        - else, the current iteration is greater than the pivot, leave it
    4. Once all iterations have been completed, we know all values less than the pivot are to the left of the boundary
        - Move pivot to its correct position
        - swap value of pivot with the value of the boundary
    5. Return the boundary so that we can recursively partition elements around the new partition point
        
    Pros:
        In Place

    Cons:
        Can be inefficient in worst case scenarios
         - Improved by taking median(of first, last, and middle) or a random pivot points
        
"""



def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)
        
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

    
arr = [10, 3, 15, 5, 6]
n = len(arr)
answer = quick_sort(arr, 0, n-1)

print(answer)
