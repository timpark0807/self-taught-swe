class Solution:
    def spiralOrder(self, matrix):
        answer = []
        
        rows = len(matrix) 
        cols = len(matrix[0])
        
        for x in range((rows//2)+1):
            
            # Iterate top
            for y in range(x, cols-x-1):
                answer.append(matrix[x][y])
            
            # Iterate right
            for y in range(x, rows-x-1):
                answer.append(matrix[y][cols-x-1])
                
            # Iterate bottom
            for y in range(x, cols-x-1):
                answer.append(matrix[rows-x-1][cols-y-1])      
                
            # Iterate Left
            for y in range(x, rows-x-1):
                answer.append(matrix[rows-y-1][x])
                
        return answer

s = Solution()
answer = s.spiralOrder([ [1,   2,  3,  4],
                         [5,   6,  7,  8],
                         [9,  10, 11, 12],
                         [13, 14, 15, 16]])
print(answer)
