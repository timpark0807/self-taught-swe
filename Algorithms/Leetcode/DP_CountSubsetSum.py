import unittest

class Knapsack:
    """
    Category
        0/1 Knapsack
        - Need to reach taget sum exactly 

    Subproblem

    State
        - Index
            - Which number we are currently considering
        - Remaining
            - How much more is left to be filled

    Decisions
        - Add current value 
        - Add leave current value

    Base Cases
        - Index < 0
            -> We've added all values inside the original subset
            -> Return 0 -> Don't consider this option
        - remain == 0
            -> We've hit our target
            -> Return 1 ->
    """
    def count_subset_sum(self, subset, target):
        return self.dp(subset, len(subset)-1, target)

    def dp(self, subset, index, remain):
        if remain == 0:
            return 1
        if index < 0 or remain < 0:
            return 0

        take_it = self.dp(subset, index-1, remain - subset[index])
        leave_it = self.dp(subset, index-1, remain)

        return take_it + leave_it

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Knapsack()

    def tearDown(self):
        self.s = None
        
    def test_valid(self):
        self.assertEqual(self.s.count_subset_sum([1, 1, 2, 3], 4), 3)
        self.assertEqual(self.s.count_subset_sum([1, 2, 7, 1, 5], 9), 3)

if __name__ == '__main__':
    unittest.main()
