def quicksort(arr):

    # base case -> if length of array is 1 then return the array
    if len(arr) < 2:
        return arr

    else:
        
        # set pivot equal to first value in array
        pivot = arr[0]
        
        # create list for numbers less than and greater than pivot
        less = []
        greater = []

        # loop through array, excluding pivot which was arr[0]
        for i in arr[1:]:
            
            # if the value is less than pivot, append to less list 
            if i < pivot:
                less.append(i)
                
            # if value is greater than pivot, append to greater list
            else:
                greater.append(i)
 
        # quick sort the less list and greater list until the length is 1,
        # when length of less or greater list == 1,
        # stack calls will be returned and solved
        
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([15,30,10,55,31,2,6]))
