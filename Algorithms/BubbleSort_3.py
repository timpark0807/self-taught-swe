def bs(arr):
    # runs iteration for n number of times
    for i in range(len(arr)):

        # runs the comparison between current index and right index
        for j in range(0, len(arr)-1):
            # if current index is greater than right index
            if arr[j] > arr[j+1]:
                # swap the value of current index and right index
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
    return arr


print(bs([5, 2, 1, 6, 3]))
