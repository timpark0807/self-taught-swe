def sliding_bruteforce(arr, k):
    """
    O(n^2)
    
    Run a nested loop of all windows of length k in the given array

            0    1    2    3
    arr = [100, 200, 300, 400]
    k = 2        
    len(arr) = 4
     
    for i in range(0, 3) -> [0, 1, 2]

    0   for j in range(0,2) -> [0, 1]
            current_sum -> arr[0] + arr[1] = 300
            
    1   for j in range(1,3) -> [1, 2]
            current_sum -> arr[1] + arr[2] = 500

    2   for j in range(2,4) -> [2, 3]
            current_sum -> arr[2] + arr[3] = 700
    """
    
    for i in range(0, len(arr) - k + 1):
        current_sum = 0
        for j in range(i, i+k):
            current_sum += arr[j]
        print(current_sum)
        

def sliding_optimized(arr, k):
    """
            0    1    2    3
    arr = [100, 200, 300, 400]
    k = 2        
    len(arr) = 4

    for i in range(0, 2) -> [0, 1]
        current_sum = arr[0] + arr[1] = 100 + 200 = 300

    for i in range(2,4) -> [2, 3]
        >> i = 2
        >> current_sum = 300 + arr[2] - arr[0] = 300 + 300 - 100 = 500

        >> i = 3
        >> current_sum = 500 + arr[3] - arr[1] = 500 + 400 - 200 = 700 
    """
    
    current_sum = 0
    max_sum = 0
    
    # Calculate sum of first window 
    for i in range(0, k):
        current_sum += arr[i]

    # Slide window from start to end in array
    for i in range(k, len(arr)):
        current_sum = current_sum + arr[i] - arr[i-k]
        if current_sum > max_sum:
            max_sum = current_sum
            
    return print(max_sum)

#       0    1    2    3    4    5   6
# arr = [100, 200, 100, 400, 500,  2, 600]

#       0    1    2    3   
arr = [100, 200, 300, 400]
k = 2
sliding_optimized(arr, k)
