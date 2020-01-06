def get_different_number(arr):
  if not arr:
    return 0
  
  max_in_arr = max(arr)
  seen = set(arr)

  for curr_integer in range(0, max_in_arr+2):    
    if curr_integer not in seen:
      return curr_integer
  

