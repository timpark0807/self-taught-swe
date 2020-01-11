def array_of_array_products(arr):
  if len(arr) <= 1:
    return []

  # Initialize a return array = [1] * len(arr) 
  # left_multiplier = 1
  # right_multiplier = 1
  retval = [1] * len(arr)
  left_multiplier, right_multiplier = 1, 1

  # iterate over all indicies of input array
  for index in range(len(arr)):
    # multiply return arr's current iteration index by the left_multiplier 
    retval[index] *= left_multiplier
    left_multiplier *= arr[index]
    
  # iterate over all indicies of input array (backwards)
  for index in reversed(range(len(arr))):
    # multiply return arr's current iteration index by the right_multiplier 
    # right_multiplier *= arr[index]
    retval[index] *= right_multiplier
    right_multiplier *= arr[index]
    
  return retval
   
   
