class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        
        Variables needed:
        left, right = 0, 0
        global_max = 4
        current_max = 4
        
        freq = {
                a: 2,
                b: 3
        
        
                              r 
                    l 
        Input: "c c a a b b b"
                0 1 2 3 4 5 6
        
        What is our condition to be met?
            *** if len(freq) > 2 
            
        1. Expand right
            - Add character at index right to freq 
            - Or increment it by += 1
            
        2. Check if len(freq) > 2
            - Process the current subarray
                -> current_max = right - left 
                -> global_max = max(global_max, current_max)
                
            - Remove character at index left from freq
            - if value of s[left] in our freq == 0:
                delete it from our freq
            - increment left
        
        3. - Increment right
        
        When right is done:
            - check that current left:right is not longer
            if len(freq) <= 2:
                global_max = max(global_max, right- left)

        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        left, right = 0, 0
        global_max = float('-inf')
        freq = {}
        
        # Expand Right
        while right < len(s):
            right_char = s[right]
            if right_char not in freq:
                freq[right_char] = 0
            freq[right_char] += 1
            
            # Contract Left
            while len(freq) > 2:
                current_max = right - left
                global_max = max(global_max, current_max)
        
                left_char = s[left]
                freq[left_char] -= 1
                if freq[left_char] == 0:
                    del freq[left_char]
                    
                left += 1
                    
            right += 1
            
        if len(freq) <= 2:
            current_max = right - left
            global_max = max(global_max, current_max)

        return global_max
        
        """
        current_max = 7-3 = 4
        global_max = 3
        len(freq) = 2
        
        freq = {
                b:2,
                a:2} 
        
                 0 1 2 3 4 5 6 7
        input = "e c e b a a b"
                       l
                               r
                 
        right_char = b
        left_char = e
        
        """
        
        
        
        
        
        
        
        
        
