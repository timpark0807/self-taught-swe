class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 0, num 
        
        while left <= right: 
            mid = (left + right)  // 2
            curr = mid * mid 
            
            if curr == num:
                return True
            
            elif curr > num:
                right = mid - 1
            
            else:
                left = mid + 1 
            
            
        return False
