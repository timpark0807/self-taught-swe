import unittest
import collections

def absSort(arr):
  """ 
  Input  : arr[int]
  Output : arr[int] 
  
  Description:
    Sorts the array in respect to the absolute value of the numbers
  
  Note: 
    Negative numbers will come before positive numbers. 
  """
  if len(arr) == 0 or len(arr) == 1:
    return arr 
  
  # Step 1: Preprocess
  # Log all the negative integers we see in a hashtable 
  count_of_negative_integers = get_count_of_negative_integers(arr)

  # Turn the integers in the array positive
  return_arr = [abs(i) for i in arr]
  
  # Sort the array
  return_arr.sort()
  
  # Step 2: Iteration and Sort
  # Iterate over the return array 
  for index, num in enumerate(return_arr):
    # Check if the current number's negative value exists in our hashtable
    # If it does exist
    if -num in count_of_negative_integers:
      
      # Turn the current number negative in return arr
      return_arr[index] = -num
      
      # Decrement the count of the current number negative
      count_of_negative_integers[-num] -= 1
      
      # If the current number's negative count == 0, delete it
      if count_of_negative_integers[-num] == 0:
        del count_of_negative_integers[-num]
        
  return return_arr

  
def get_count_of_negative_integers(arr):
  """
    Returns a hashtable with the count of negative integers 
    
    key = the negative integer 
    value = count of that negative integer
  """
  d = dict()
  for num in arr:
    if num < 0:
      if num not in d:
        d[num] = 0 
      d[num] += 1
  return d


    
    
    
