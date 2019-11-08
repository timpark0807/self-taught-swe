class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
                    l r
                      i  
        string = 'b a a b b'
                  0 1 2 3 4
                 0 1 2 3 4 5 
        iterate over string
        from each letter, expand outwards
            -> intialize left as index - 1
            -> intialize right as index + 1
            if left > 0 and right < len(string) and s[left] == s[right]:
                -> Get current palindrome
                -> Check against current_max

                left -=1 
                right += 1
        """
        if len(s) == 1:
            return s
        elif len(s) == 0:
            return ''

        overall_max = ''
        
        for index in range(len(s)): 
            left = index - 1
            right = index + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_palindrome = s[left:right+1]
                overall_max = max(overall_max, current_palindrome, key=len)
                left -= 1
                right += 1
                
            left = index - 1
            right = index 
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_palindrome = s[left:right+1]
                overall_max = max(overall_max, current_palindrome, key=len)
                left -= 1
                right += 1
                        
        return overall_max
