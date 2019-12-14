import unittest
def shortestCellPath(grid, sr, sc, tr, tc):
  if not grid:
    return -1 
  
  # Initailize BFS variables
  queue = [(sr, sc)]
  count = 0 
  seen = set()
  # While Queue
  while queue:
    current = queue.pop(0)
    curr_row, curr_col = current[0], current[1]
    
    if (curr_row, curr_col) not in seen and 0 <= curr_row < len(grid) and 0 <= curr_col < len(grid[0]) and grid[curr_row][curr_col] == 1:
      seen.add((curr_row, curr_col))
      # Go up 
      queue.append((sr-1, sc))
      # Go Down
      queue.append((sr+1, sc))
      # Go right
      queue.append((sr, sc+1))
      # Go Left
      queue.append((sr, sc-1))

      count += 1
      print(curr_row, curr_col, count)
      if (curr_row, curr_col) == (tr, tc):
        return count
      
  return -1 

  """
      grid = [[1, 1, 1, 1], 
              [0, 1, 0, 1], 
              [1, 1, 1, 1]]


    queue = [(0, 1)

    curr = (0,1)

    seen = {(0,0), (0,1)
    count = 3
  """
   
grid = [[1,1,1,1],[0,0,0,1],[1,1,1,1]]

print(shortestCellPath(grid, 0, 0, 2, 0))
