def findSmallest(arr):
    # store smallest value
    smallest = arr[0]

    # Stores index of smallest value
    smallest_index = 0

    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
            
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr        

print(selectionSort([10,80, 450, 6, 20,12,300]))
