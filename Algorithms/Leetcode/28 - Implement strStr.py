class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0 
        if needle == haystack:
            return 0
        
        check = len(needle)
        h_pointer = 0
        
        for h_pointer in range(len(haystack)):            
            if haystack[h_pointer] == needle[0]:
                 if haystack[h_pointer:h_pointer+check] == needle:
                    return h_pointer

        return -1


s = Solution()
ans = s.strStr('haystack', 'kwijg')
print(ans)
