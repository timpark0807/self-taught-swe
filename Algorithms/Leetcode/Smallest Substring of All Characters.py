def get_shortest_unique_substring(arr, s):
  """
  BigO
  
  time               goal time
  O(n^2) -> O(nlogn) -> O(n) -> O(logn) -> O(1)
  space              goal space
  
  
  arr = ['x','y','z'] 
          
  len(s) == 8
      0 1 2 3 4 5 6 7 8
       0 1 2 3 4 5 6 7
  s = "x y y z y z y x"
      l    
             r 
    
  freq = {'x' : 0,
          'y' : 0,
          'z' : 0
                  }
                  
 current_min = arr[5:8] -> 'zyx'
 overall_min = 'zyx'
   """
  
  #edge cases
  if len(arr) == 0:
    return ''
  
  # Initialize variables
  left, right = 0,0 
  freq = dict()
  overall_min = s
  

  #Fill up dictionary of frequency of strings in arr
  for letter in arr:
    if letter in freq:
      freq[letter] += 1
    else:
      freq[letter] = 1
  
  # Sliding Window 
  
  # Pushing sliding window to right 
  while right < len(s):
    if s[right] in freq:
        freq[s[right]] -= 1
    right += 1

    # Pushing sliding window to the left (minimizing sliding window)
    while all_values_in_freq_are_zero(freq):
      current_min = s[left:right]
      overall_min = min(overall_min, current_min, key=len)
      if s[left] in freq:
          freq[s[left]] += 1
      left += 1
      
  return overall_min 
      
      
def all_values_in_freq_are_zero(freq):
  for value in freq.values():
    if value > 0:
      return False
    
  return True


arr, s = ['A', 'B', 'C'], "ABOBECODEBANC"
print(get_shortest_unique_substring(arr, s))
    
      
      
      
  
  
