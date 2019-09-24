def rotation(arr):
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
