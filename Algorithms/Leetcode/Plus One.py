class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        
         0  1  2  3  4  5
        [0, 0] 
         i

        i = 2
        
        """
        i = len(digits) - 1
        
        while True:
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
                i -= 1
                if i < 0:
                    return [1] + digits
            else:
                break
            
        return digits

s = Solution()
print(s.plusOne([9,9]))
