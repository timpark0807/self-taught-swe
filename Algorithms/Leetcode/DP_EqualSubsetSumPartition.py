import unittest

class Knapsack:
    """
    Category
        0/1 Knapsack
           - "Capacity" of the knapsack is the sum of subset // 2
           - "Items" are the numbers in the subset
           - "Weight" of the item is the value of the number itself.
           - Choose to take the item (add number) or not take item from our subset  
               - We can only use numbers once, hence 0/1 
    Subproblem
        Prefix
        
    State
        1. Index
           - Tracks what element of the subset we are on
        2. Remain
           - Tracks the remaining "capacity"

    Decisions
    What decisions do we have at each step?
    We need to modify state in a way that reduces our problem into a smaller subproblem
    and moves towards the base cases.
        
        1. Take Number
            -> Subtract current number from Remain
            -> Increment Index
        2. Don't Take Number
            -> Don't update Remain
            -> Increment Index

    Base Cases
        1. Index is out bounds
            -> We have considered all items in our subset
        2. Remain is less than 0
            -> We have overshot our index
        3. Remain == 0
            -> We have successfully reached our target  
    """

    def equal_subset_sum(self, subset):
        if sum(subset) % 2 != 0:
            return False
        self.memo = {}
        target = sum(subset) // 2    
        return self.dp(subset, len(subset)-1, target)

    def dp(self, subset, index, remain):
        if (index, remain) in self.memo:
            return self.memo[(index, remain)]
        if remain == 0:
            return True
        if index < 0 or remain < 0:
            return False

        take_it = self.dp(subset, index - 1, remain - subset[index])
        leave_it = self.dp(subset, index - 1, remain)
        self.memo[(index, remain)] = take_it or leave_it
        return self.memo[(index, remain)] 

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Knapsack()

    def tearDown(self):
        self.s = None
        
    def test_valid(self):
        self.assertTrue(self.s.equal_subset_sum([1, 2, 3, 4]))
        self.assertTrue(self.s.equal_subset_sum([1, 1, 3, 4, 7]))

    def test_invalid(self):
        self.assertFalse(self.s.equal_subset_sum([2, 3, 4, 6]))

if __name__ == '__main__':
    unittest.main()
