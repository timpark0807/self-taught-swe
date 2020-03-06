import unittest


"""
Checklist:
    Brute Force/Big O
    Edge Cases
    Assumptions
    Test Cases
    Input
    Output
    Highlevel
    Docstrings


Things needed:
    moves
    is_valid()
    seen set?
    count of time elapsed
    queue 

# Step 1: Preprocess
    - Iterate the over the grid
    - If the grid value is 1 
    - Add that coordinate to the queue 
    
# Step 2: Process
    - While there are coordinates in the queue
        - Remove all current coordinates from the queue
            - get current coordinate
            - try moving in all 4 directions
                - Only make the move if it is_valid()
                    - AKA move coordinate not in seen, == 0 and in bounds
        - Increment count
        
    return count 

       0  1  2  3  4
    0 [0, 1, 1, 0, 1]
    1 [0, 1, 0, 1, 0]
    2 [0, 0, 0, 0, 1]
    3 [0, 1, 0, 0, 0]
"""

import collections

def time_to_infection(grid):
    """
    Description: Returns how many hours it takes for the entire grid to be infected

    @param  grid   : arr[arr[int]]
    @return answer : int 
    """
    if not grid:
        return 0
    
    count = 0
    queue = collections.deque()
    seen = set()
    
    # Preprocess
    # Time  : O(nm)
    # Space : O(nm)
    # where n == rows and m == cols 
    for row in range(len(grid)):
        for col in range(len(grid[row])):
           if grid[row][col] == 1:
              queue.append((row, col))
              seen.add((row, col))

    # Postprocess
    # Time  : O(nm)
    # Space : O(nm)
    moves = [(0,1),(0,-1),(1,0),(-1,0)]
    while queue:
        for _ in range(len(queue)):
            curr_row, curr_col = queue.popleft()
            for move in moves:
                new_row, new_col = curr_row + move[0], curr_col + move[1]
                if is_valid(grid, seen, new_row, new_col):
                    queue.append((new_row, new_col))
                    seen.add((new_row, new_col))
        count += 1

    return count - 1

def is_valid(grid, seen, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[row]) and (row, col) not in seen and grid[row][col] == 0

class TestSolution(unittest.TestCase):
    def test_one(self):
        grid = [[0, 1, 1, 0, 1],
                 [0, 1, 0, 1, 0],
                 [0, 0, 0, 0, 1],
                 [0, 1, 0, 0, 0]]
        self.assertEqual(time_to_infection(grid), 2)

if __name__ == '__main__':
    unittest.main()
