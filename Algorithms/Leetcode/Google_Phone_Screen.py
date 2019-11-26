import unittest

def largest_plot_under_budget(land, budget):
    left, right = 0, 0
    global_max = 0
    cost = 0
    
    while right < len(land):
        cost += land[right]

        while cost > budget:
            current_max = right - left
            global_max = max(global_max, current_max)
            cost -= land[left]
            left += 1

        right += 1

    if cost <= budget: 
        current_max = right - left
        global_max = max(global_max, current_max)

    return global_max

"""
land -> arr of [integers]
budget -> int
global_max -> int
left -> int
right -> int
cost -> int
while right < len(land) -> int < int
cost += land[right] -> int += int
while cost > budget -> int > int
current_max = right - left -> int - int -> int
global_max = max(global_max, current_max) -> max(int, int) -> int
cost -= land[left] -> int -= arr[int] -> int -= int
left += 1 -> int += int


"""

"""

Variables Needed:
left, right = 0, 0
global_max = 0


Sliding Window:
1. Expand window
    Add right pointers value to cost

2. Meet condition
    If cost > budget:
        
    3. Process window
        current_max = right - left
        global_max = max(global_max, current_max)
        
    4. Shrink Window
        Remove left pointers value from cost
        Increment Left
        
1b. Increment right

5. Check if ending subarray is valid

global_max = 4
current_max = 4

        0  1  2  3  4  5  6  7  8  9  10 11 
land = [1, 1, 3, 2, 4, 1, 1, 1, 1, 1, 1, 1]
                       l
                                            r
                 
cost = 7
budget = 7
"""
class Solution(unittest.TestCase):
    def test_one(self):
        land = [1, 1, 3, 2, 4, 3, 2]
        budget = 7
        answer = largest_plot_under_budget(land, budget)
        self.assertEqual(answer, 4)

    def test_two(self):
        land = [1, 1, 1, 1, 1, 1, 1]
        budget = 7 
        answer = largest_plot_under_budget(land, budget)
        self.assertEqual(answer, 7)

if __name__ == '__main__':
    unittest.main()
