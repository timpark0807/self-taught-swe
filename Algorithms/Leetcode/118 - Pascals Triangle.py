class Solution(object):
    def generate(self, numRows):
        
        tri = [[] for _ in range(numRows)]
        for i in range(1, numRows + 1):
            tri[i-1] = [0] * i
        
        tri[0] = [1]
        tri[1] = [1, 1]
        for row_index in range(2, len(tri)):
            tri[row_index][0] = 1
            tri[row_index][-1] = 1
            for col_index in range(1, len(tri[row_index])):
                if tri[row_index][col_index] == 0:
                    tri[row_index][col_index] = tri[row_index-1][col_index] + tri[row_index-1][col_index-1]
        return tri



s = Solution()
print(s.generate(5))
