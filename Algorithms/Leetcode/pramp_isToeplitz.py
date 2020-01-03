import unittest

def isToeplitz(grid):
  # Step 0. Check Edge Cases 
  if not grid:
    return True
    
  # Step 1. Traverse the matrix Bottom Left, Left Hand side,
  for index in reversed(range(1, len(grid))):
      if not valid_diagonal(grid, index, 0, grid[index][0]):
        return False

  # Step 1.1 Traverse the matrix Top going right 
  for index in range(len(grid[0])):
      if not valid_diagonal(grid, 0, index, grid[0][index]):
        return False

  return True 

def valid_diagonal(grid, row, col, num):
  
  while row < len(grid) and col < len(grid[0]):
    if grid[row][col] != num:
      return False
    row += 1
    col += 1
    
  return True 
      
   
