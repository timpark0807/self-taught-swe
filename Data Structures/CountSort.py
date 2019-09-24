arr =  [10, 10, 3, 4, 5,6, 6, 8, 7,3,2,1]


def count_sort(arr, highest):
    """
    highest = 5
    arr = [1, 5, 5, 5, 4, 3, 1]
    
    1. Create an array of 0's with the len == highest + 1 
        -> The index of the array will represent the score
        -> The value at the index of the array will represent number of times score appears
        -> len = highest + 1 to account for the zero'th index

                 0  1  2  3  4  5 
        count = [0, 0, 0, 0, 0, 0]


    2. Increment the index of each score for everytime it appears
    
                 0  1  2  3  4  5     
        count = [0, 2, 0, 1, 1, 3]

    3. a. Create output arr.
       b. Iterate through the index (scores), backwards.
       c. Find how many times that score appears in array 
       d. Append the index (score) to the output array, the number of times it appears

       output = [5, 5, 5, 4, 3, 1, 1]

       a.  output = [] 
       b.  for score in range(len(count)-1, 0, -1):    ->    [5, 4, 3, 2, 1, 0] 
       c.      count = arr[score]                      ->    arr[5] = 3 
       d.      for times in range(count):              ->    [0, 1, 2]
       d.          output.append(score)                ->    [5, 5, 5]
       
        
    """
    count_arr = [0] * (highest + 1)

    for num in arr:
        count_arr[num] += 1

    output = []
    
    for score in range(len(count_arr)-1, 0, -1):
        count = count_arr[score]
        for times in range(count):
            output.append(score)
            
    return output



print(count_sort(arr, 10))
