class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        for row in range(len(matrix)):
            if self._binary_search(matrix[row], target):
                return True
            
        return False
        
    def _binary_search(self, row, target):
        if target > row[-1]:
            return False
        
        left = 0 
        right = len(row)-1
        
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                right -= 1
            else:
                left += 1
        return False
