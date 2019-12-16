import unittest

def find_busiest_period(data):
    if not data:
      return 0
    if len(data) == 1 and data[0][2] == 1:
      return data[0][0]
    
    time_stamp = 0
    count = 1
    en_ex = 2
    
    # Time stamp and count 
    global_max = (0, float('-inf'))
    
    time_mapping = {data[0][time_stamp]:0}
    
    # Iterate through each point in the array
    for index, data_arr in enumerate(data):   
      
      # Define current iteration's values
      curr_time_stamp = data_arr[time_stamp]
      curr_count = data_arr[count]
      curr_en_ex = data_arr[en_ex]
      
      # If we encounter a timestamp that is not in the hashtable
      if curr_time_stamp not in time_mapping:
        prev_time_stamp = data[index-1][time_stamp]
        time_mapping[curr_time_stamp] = time_mapping[prev_time_stamp]
        
        if time_mapping[prev_time_stamp] > global_max[1]:
          global_max = (prev_time_stamp, time_mapping[prev_time_stamp])
        
      # Check if they are entering or exiting
      if curr_en_ex == 1:
        # They are entering the mall 
        time_mapping[curr_time_stamp] += curr_count
      else:
        # They are leaving the mall
        time_mapping[curr_time_stamp] -= curr_count
    
    if time_mapping[data[-1][0]] > global_max[1]:
      global_max = (data[-1][0], time_mapping[prev_time_stamp])

    return global_max[0]
