
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        self.moves = [(0,1), (0,-1), (1,0), (-1,0)]
        global_max = 0
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                path = self.dfs(matrix, row, col, set())
                global_max = max(global_max, path)
                
        return global_max
    
    
    def dfs(self, matrix, row, col, seen):
        stack = [(row, col, 1)]
        curr_max_length = 1
        seen.add((row,col))
        
        while stack:
            x, y, length = stack.pop()
            curr_max_length = max(curr_max_length, length)
            
            for r, c in self.moves:
                if not self.is_invalid(matrix, seen, x+r, y+c) and matrix[x+r][y+c] > matrix[x][y]:
                    seen.add((x+r, y+c))
                    stack.append((x+r, y+c, length+1))
        
        return curr_max_length
    
    def is_invalid(self, matrix, seen, row, col):
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or (row, col) in seen:
            return True
        return False

s = Solution()
print(s.longestIncreasingPath([[1,2]]))
