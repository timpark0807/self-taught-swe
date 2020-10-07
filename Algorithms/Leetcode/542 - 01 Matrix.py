class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        queue = collections.deque()
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    queue.append((row, col, 0))
                    
        answer = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        seen = set() 
        
        while queue:
            row, col, step = queue.popleft() 
            
            answer[row][col] = step 
            
            
            for move in [(0,1),(0,-1),(1,0),(-1,0)]:
                newRow, newCol = row+move[0], col+move[1]
                if 0<=newRow<len(matrix) and 0<=newCol<len(matrix[0]) and (newRow, newCol) not in seen and matrix[newRow][newCol] == 1:
                    seen.add((newRow, newCol))
                    queue.append((newRow, newCol, step+1))
                    
        return answer 
