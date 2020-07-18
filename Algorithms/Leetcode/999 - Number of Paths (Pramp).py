import unittest 

def num_of_paths_to_dest(n):
  
  return dfs(n, {}, 0, 0)


def dfs(n, memo, row, col): # state variables 
  if (row, col) in memo:
    return memo[(row, col)]
  # base case 
  # success
  if row == n-1 and col == n-1:
    return 1
  
  # failure
  if row == n or col == n or row < col:
    return 0 
  
  # decisions 
  go_right = dfs(n, memo, row, col+1) 
  go_down = dfs(n, memo, row+1, col) 
  
  # build answer
  memo[(row, col)] = go_right + go_down
  return go_right + go_down 

  
"""
class TestSolution(unittest.TestCase):
  def test_giveninpuit(self):
    answer = num_of_paths_to_dest(4) 
    expected = 5 
    self.assertEqual(answer, expected) 
    
  def test_one(self):
    answer = num_of_paths_to_dest(1) 
    expected = 1 
    self.assertEqual(answer, expected) 
    
   
if __name__ == '__main__':
  unittest.main() 


“EENENN”, “ENEENN”, “ENENEN”, “EENNEN”


STATE 
  - what row are we on 
  - what col are we on 

base case 
  1. success -> we reached n-1, n-1 
    -> return 1
  
  2. failure -> if we go outside the bounds of the axis OR we cross our magic diagonol line 
    -> return 0

decisions
  go right = 

  go down 
  

  return go_right + go_down 
  
 
N = the input n aka size of the axis 
time : O(2^n)
space: O(n^2) ?? lets revisit 


RULES
 1. Can't cross diagnoal line 
 2. We can only move right or down 
 3. n x n matrix

Goal: 
  Figure out the TOTAL NUMBER OF WAYS we can reach top left corner to top right corner 
  following the rules listed above
  

[0, 0, 0, 0, E] N
[0, 0, 0, 0, 0] N 
[0, 0, 0, 0, 0] N
[0, 0, 0, 0, 0] N 
[S, 0, 0, 0, 0] N   
 E  E  E  E  E 
  
  
  
  stack = [E, E, E, E, E,]
 “EEEEENNNNN”

ANSWER = 0 -> 1

path 2 

"EEEENNENN"
"""
