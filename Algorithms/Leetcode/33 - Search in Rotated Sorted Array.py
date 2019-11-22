import unittest

def search_rotated(arr,target):
"""
    target = 1

               r 
            l
    arr = [ 3, 1]
            0  1  
            m
"""

    left = 0
    right = len(arr) - 1
    
    while left <= right:
        
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] >= arr[left]:
            if target >= arr[left] and target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target <= arr[right] and target > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

    """
    target = 3
    
                   r 
           l    
    arr = [4, 5, 0, 1, 2, 3]
           0  1  2  3  4  5  
                 m

    set left, right
    set mid = left+right // 2

    if arr[mid] == target -> return mid
    
    elif arr[mid] > arr[left] -> means left half is sorted
        if target >= arr[left] and target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    else: -> Means right half is sorted
        if target <= arr[right] and target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    
    """



class Test(unittest.TestCase):
    def test_valid(self): 
        target = 5
        arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
        answer = search_rotated(arr,target)
        self.assertEqual(answer, 1)
        
    def test_left(self): 
        target = 4
        arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
        answer = search_rotated(arr,target)
        self.assertEqual(answer, 0)
        
    def test_right(self): 
        target = 3
        arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
        answer = search_rotated(arr,target)
        self.assertEqual(answer, 8)
