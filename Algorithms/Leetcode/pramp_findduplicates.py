def find_duplicates(arr1, arr2):
  if not arr1 or not arr2:
    return []
  output = []
  for target in arr1:
    if binary_search(target, arr2):
      output.append(target)
  return output

def binary_search(target, arr):
  left, right = 0, len(arr)-1
  while left <= right:
    mid = (left+right) // 2
    if arr[mid] == target:
      return True
    elif arr[mid] > target:
      right = mid - 1
    else:
      left += 1
  return False
    
  
  """
  Figure out which array has a smaller length
    for each element in the array with the smaller length
    Use a binary search to search for that element in the larger array
      -> NLogM
      -> N = length of smaller array
      -> M = legnth of larger array

  """
  
"""
  # Step 1. Initialize 2 pointers on the beginning of each aray
  p1, p2 = 0, 0
  output = []
  
  
  while p1 < len(arr1) and p2 < len(arr2):
  #Step 2. Check if they are equal 
    if arr1[p1] == arr2[p2]:
      output.append(arr1[p1])
      p1 += 1
      p2 += 1
    
    #Step 2.1: If they are not equal, we need to increment pointer that has a smaller value
    elif arr1[p1] > arr2[p2]:
      p2 += 1
      
    #Step 2.2.: If they are equal: just append to output array
    else:
      p1 += 1
      
  return output
"""


"""

Input : 2 arrays 
Ouput : 1 array containing integers found in both arrays

Brute Force:
  -> Nested for loops on each array -> O(n^2)
  
Edge Cases:
  -> If any are empty -> return []

Assumptions:
  -> Array is filled with valid integers
      -> No flats, no negatives 
  -> Array is sorted
  
Toolbox:
  -> binary search
  -> 2 pointers 

2 Cases:
  - Array lengths are equal
    -> 2 pointers
  
      arr1 = [1, 2, 3, 5, 6, 7]
              ^
              
      arr2 = [3, 6, 7, 8, 20]
              ^
              
      output = [3, 6, 7]

  Step 1. Initialize 2 pointers on the beginning of each aray
  
  
  While p1 < len(arr1) and p2 < len(arr2):
  Step 2. Check if they are equal 
    Step 2.1: If they are not equal, we need to increment pointer that has a smaller value
    Step 2.2.: If they are equal: just append to output array
    

  - Array lengths are lopsided
    -> Binary Search
    
    Figure out which array has a smaller length
    for each element in the array with the smaller length
    Use a binary search to search for that element in the larger array
      -> NLogM
      -> N = length of smaller array
      -> M = legnth of larger array
  
      arr1 = [3, 5]

      arr2 = [1, 2, 3, 5, 6, 7]

      output = [3]


"""
