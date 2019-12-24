class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        self.memo = {}
        return self.dp(strs, m, n, 0)
    
    
    def dp(self, strs, m, n, index):
        if (m, n, index) in self.memo:
            return self.memo[(m, n, index)]
        
        elif m < 0 or n < 0:
            return float('-inf')

        elif index == len(strs):
            return 0
        
        need_m, need_n = self.count_m_n(strs[index])
                
        self.memo[(m, n, index)] = max(self.dp(strs, m-need_m, n-need_n, index+1) + 1, 
                                       self.dp(strs, m, n, index+1))
        
        return self.memo[(m, n, index)] 
    
    
    def count_m_n(self, word):
        count_zeroes = 0
        count_ones = 0 

        for digit in word:
            if digit == '1':
                count_ones += 1
            elif digit == '0':
                count_zeroes += 1
                
        return count_zeroes, count_ones 
