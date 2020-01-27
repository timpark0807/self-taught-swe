import math
 
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return []
        factors = self.get_factors(n)
        answers = []
        curr = []
        curr_prod = 1
        start = 1 
        self.backtrack(factors, n, answers, set(), curr, curr_prod, 0)
        return answers
    
    def backtrack(self, factors, n , answers, seen, curr, curr_prod, start):
        if curr_prod == n:
            answers.append(curr[::])
            return 
        
        for index in range(start, len(factors)):
            if curr_prod * factors[index] <= n:
                self.backtrack(factors, n, answers, seen, curr + [factors[index]], curr_prod * factors[index], index)
                
    def get_factors(self, n):
        res = []
        for i in range(2, n):
            if n % i == 0:
                res.append(i)
        return res

s = Solution()
print(s.getFactors(12))
