import unittest

class Solution:

    def merge(self, intervals):
        """
        input: nested lists
        output: nested lists
        """
        intervals.sort()
        output = [intervals[0]]
        x = 0
        for index in range(1, len(intervals)):
            i1 = output[x]
            i2 = intervals[index]
            if min(i1[1], i2[1]) - max(i1[0], i2[0]) > 0:
                output[x] = [min(i1[0], i2[0]), max(i1[1], i2[1])]
            else:
                output.append(intervals[index])
                x += 1
        return output


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        self.s = None
        
    def test_valid(self):
        arr = [[1,3], [2,6], [8,10], [15,18]]
        answer = self.s.merge(arr)
        self.assertEqual(answer, [[1, 6],
                                  [8, 10],
                                  [15, 18]])
        
    def test_valid_second(self):
        arr = [[1,7], [2,6], [8,17], [15,18]]
        answer = self.s.merge(arr)
        self.assertEqual(answer, [[1, 7],
                                  [8, 18]])




if __name__ == '__main__':
    unittest.main()
