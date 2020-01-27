import unittest

class Knapsack:
    def target_sum(self, subset, target):
        index = len(subset)-1
        return self.dp(subset, target, index, 0)

    def dp(self, subset, target, index, remain):
        if index < 0 and remain == target:
            return 1
        
        if index < 0:
            return 0

        positive = self.dp(subset, target, index-1, remain + subset[index])
        negative = self.dp(subset, target, index-1, remain - subset[index])

        return positive + negative
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Knapsack()

    def tearDown(self):
        self.s = None
        
    def test_valid(self):
        self.assertEqual(self.s.target_sum([1, 1, 2, 3], 1), 3)
        self.assertEqual(self.s.target_sum([1, 2, 7, 1], 9), 2)

if __name__ == '__main__':
    unittest.main()
