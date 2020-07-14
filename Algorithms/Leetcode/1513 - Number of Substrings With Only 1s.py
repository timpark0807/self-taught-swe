class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        answer = 0
        while left < len(s):
            if s[left] == '0':
                left += 1
            else:
                right = left 
                while right < len(s) and s[right] == '1':
                    right += 1
                n = right - left
                answer += ((n+1) * n) // 2
                left = right + 1
            
        return answer % 1000000007
