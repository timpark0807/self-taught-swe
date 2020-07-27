class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        seen = collections.defaultdict(int)
        seen[0] = 1 
        
        ps = 0 
        answer = 0 
        
        for num in A:
            ps += num 
            answer += seen[ps-S] 
            seen[ps] += 1
        return answer
