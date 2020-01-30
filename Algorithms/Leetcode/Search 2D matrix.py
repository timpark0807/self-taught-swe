class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        row_num = self.get_row(matrix, target)
        
        if row_num == -1:
            return False
        
        row = matrix[row_num]
        left = 0
        right = len(row) - 1
        print(row)
        while left <= right:
            mid = (left + right) // 2
            print(mid)
            print(row[mid])
            if row[mid] == target:
                return True
            elif row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return False
        
    def get_row(self, matrix, target):
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2
            if target > matrix[mid][0] and target < matrix[mid][-1]:
                return mid
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                left = mid + 1

        return - 1
                
s = Solution()
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
s.searchMatrix(matrix, 13)
