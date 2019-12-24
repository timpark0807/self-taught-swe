class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        self.memo = {}
        return self.dp(d, f, target, 1) % (10 ** 9 + 7)
    
    
    def dp(self, d, f, remain, curr_roll):
        if (d, remain) in self.memo:
            return self.memo[(d, remain)]
        elif remain == 0 and d == 0:            
            return 1
        elif (d == 0 and remain != 0) or curr_roll > f:
            return 0 
        else:
            throw = self.dp(d-1, f, remain - curr_roll, 1)
            leave = self.dp(d, f, remain, curr_roll+1)
            self.memo[(d, remain)] = throw + leave
            return self.memo[(d, remain)]


s = Solution()
print(s.numRollsToTarget(2, 5, 10))
print(s.numRollsToTarget(2, 6, 7))
print(s.numRollsToTarget(30, 30, 500))
