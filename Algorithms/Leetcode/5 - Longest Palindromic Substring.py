class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if type(s) != str:
            return ''
        elif len(s) == 0:
            return ''
        elif len(s) == 1:
            return s

        res = "" 
        for i in range(len(s)):
            odd = self.expand(s, i, i)
            if len(odd) > len(res):
                res = odd

            even = self.expand(s, i, i+1)
            if len(even) > len(res):
                res = even

        return res            

    def expand(self, s, left, right):
        
        while left >= 0 and right < len(s) and s[left] == s[right]:

            left -= 1
            right += 1
                
        return s[left+1:right]
    

s = Solution()
ans = s.longestPalindrome('addedd')
print(ans)
