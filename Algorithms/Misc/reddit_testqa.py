"""
    Question from a reddit thread initial phone screen for Test SWE:
    Given an array of integers, move all instances of zero to the front
    of the array while preserving the order of all non-zero values
"""

def test(arr):
    
    # initialize an empty array that we will add values too
    new_arr = []

    # iterate through all numbers in array
    for num in arr:
        # if the number is 0
        if num == 0:
            # remove the index of the number (that is zero) from array
            # and append it to new_arr
            new_arr.append(arr.pop(arr.index(num)))

    # for the remaining numbers in arr (not popped)
    # append the remaining numbers (in order) to the new array list
    for num_remaining in arr:
        new_arr.append(num_remaining)
        
    return new_arr

def test2(arr):
    for num in arr:
        if num == 0:
            zero = arr.pop(arr.index(num))
            arr = [zero] + arr[1:]
    return arr
    

print(test([4,3,9,0,9,0,6]))

print(test2([4,3,9,0,9,0,6]))
