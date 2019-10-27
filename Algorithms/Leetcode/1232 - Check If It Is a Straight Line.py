import unittest

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        x_distance = coordinates[1][0] - coordinates[0][0]
        y_distance = coordinates[1][1] - coordinates[0][1]

        for index in range(2, len(coordinates)):
            if coordinates[index][0] - coordinates[index-1][0] != x_distance:
                return False
            elif coordinates[index][1] - coordinates[index-1][1] != y_distance:
                return False

        return True
    


class TestSolution(unittest.TestCase):

    def test_valid(self):
#                        0     1     2     3     4     5 
        coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
        s = Solution()
        answer = s.checkStraightLine(coordinates)
        self.assertTrue(answer)

    def test_false(self):
        coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
        s = Solution()
        answer = s.checkStraightLine(coordinates)
        self.assertFalse(answer)
       

if __name__ == '__main__':
    unittest.main()
