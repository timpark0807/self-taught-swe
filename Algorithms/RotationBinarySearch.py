def rotation(arr):
    """
    Binary Search -> O(logn)

    Mistake:
        - Not setting left and right to indexes  
        - Comparing arr[mid] > arr[right-1]
            -> We want to compare to a constant, rightmost element

    Solution:
        - Compare arr[mid] > arr[-1]

    
    """
    left = 0
    right = len(arr) - 1 
    
    while left < right:

        mid = (left + right) //2
        
        if arr[mid] > arr[-1]:
            left = mid + 1
        else:
            right = mid 

    return left 

# words = ['p', 'r', 's', 'x', 'b', 'c', 'd', 'f']

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

print(rotation(words))
