import collections
import unittest


class Solution(object):
    
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        
        Find list of coordinates that can be reached from
            1. Pacific 
            2. Atlantic
            
        placce pacfici coordinates in a queue 
            - traverse upwards until valid 
            
        place atlantic coordinates in a queue
            - traverse upwards until valid 
        
        traverse over the entire grid
            - return coordinates that are in both pacific and atlantic paths 
            
        """
        if not matrix or not matrix[0]:
            return [] 
        
        pacific, atlantic = [], [] 
        
        for row in range(len(matrix)):
            atlantic.append((row, len(matrix[row])-1))
            pacific.append((row, 0))
            
        for col in range(len(matrix[0])):
            atlantic.append((len(matrix)-1, col))
            pacific.append((0, col))

        pacificPath = self.flowWater(matrix, pacific)
        atlanticPath = self.flowWater(matrix, atlantic) # returns a set of coordinates that can be reached 
        answer = [] 
        
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if (row, col) in pacificPath and (row, col) in atlanticPath:
                    answer.append([row,col]) 
        return answer 
    
    
    def flowWater(self, matrix, coordinates): 
        
        queue = collections.deque(coordinates)
        seen = set(coordinates) 
        path = set(coordinates) 
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while queue:
            currRow, currCol = queue.popleft()
            for move in moves:
                newRow, newCol = currRow + move[0], currCol + move[1] 
                if self._isValid(matrix, seen, currRow, currCol, newRow, newCol):
                    seen.add((newRow, newCol))
                    path.add((newRow, newCol))
                    queue.append((newRow, newCol))
        return path 
    
    
    def _isValid(self, matrix, seen, currRow, currCol, newRow, newCol):
        return 0<=newRow<len(matrix) and 0<=newCol<len(matrix[0]) and (newRow, newCol) not in seen and matrix[newRow][newCol] >= matrix[currRow][currCol]


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        self.s = None 
        
    def test_empty(self):
        matrix = []
        answer = self.s.pacificAtlantic(matrix)
        expected = [] 
        self.assertEqual(answer, expected)
    
    def test_lengthOne(self):
        matrix = [[3, 2, 1]]
        answer = self.s.pacificAtlantic(matrix)
        expected = [[0,0],[0,1],[0,2]]
        self.assertEqual(answer, expected)

    def test_normalcase(self):
        matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        answer = self.s.pacificAtlantic(matrix)
        expected = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        self.assertEqual(answer, expected)
        
if __name__ == '__main__':
    unittest.main() 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
