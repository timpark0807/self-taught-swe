class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        odds = 0
        evens = 1
        ans = 0 
        ps = 0 
        
        for num in arr:
            ps += num 
            if ps % 2 == 0:
                ans += odds
                evens += 1 
            else:
                ans += evens
                odds += 1
        
        return ans % (10**9 + 7)
