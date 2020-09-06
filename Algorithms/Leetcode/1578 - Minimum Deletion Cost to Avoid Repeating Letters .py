class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        
        left, right = 0, 1
        answer = 0
        while right < len(s):
            while right < len(s) and s[right] == s[left]:
                right += 1 
            
            answer += sum(cost[left:right]) - max(cost[left:right])
            
            left = right
            right += 1
        
        return answer 
