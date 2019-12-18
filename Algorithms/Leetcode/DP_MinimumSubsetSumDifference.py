import unittest

class Knapsack:
    """
    Category
        0/1 Knapsack
        - Need to add each number in original subset to either subset 1 or 2
        
    Subproblem
        
    State
        - Index
            - Which number we are currently considering
        - Subset 1 
        - Subset 2
        
    Decisions
        - Add value to Subset 1
        - Add Value to Subset 2
        
    Base Cases
        - Index < 0
            -> We've added all values inside the original subset
        
    """

    def mindiff_subset_sum(self, subset):
        return self.dp(subset, [], [], len(subset) - 1)

    def dp(self, subset, s1, s2, index):
        if index < 0 :
            return abs(sum(s1) - sum(s2))

        add_s1 = self.dp(subset, s1+[subset[index]], s2, index -1)
        add_s2 = self.dp(subset, s1, s2 + [subset[index]], index-1)

        return min(add_s1, add_s2)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Knapsack()

    def tearDown(self):
        self.s = None
        
    def test_valid(self):
        self.assertEqual(self.s.mindiff_subset_sum([1, 2, 3, 9]), 3)
        self.assertEqual(self.s.mindiff_subset_sum([1, 2, 7, 1, 5]), 0)
        self.assertEqual(self.s.mindiff_subset_sum([1, 3, 100, 4]), 92)

if __name__ == '__main__':
    unittest.main()
