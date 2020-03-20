class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        @description longest susbstring without repeating characters
        @param1 s : str
        @return a : int 
        
               r
        "a b c a b c b b"
         l 

        
         
         
         
        BEATIO HD
        
        brute force
            generate all substrings
            find longest one without repeating characters
            time : o(n^2)
            space : O(n^2)
            
            or 
            time : O(n^3)
            space : O(1)
            
        Optimized?
            
            
        edgecases
        assumptions
        testcases
        toolbox
            - sliding window
        
        inputoutput
            
            
        highlevel
        docstrings
        
                 
        set left and right edges to your window
        
        while right is less than length of s
            add the right character to the count 
            
            while count of right == 2 
                process current window
                shrink window
                
                
            expand window
            
        process edge case
        
        return 
        """
        
        left, right = 0 ,0 
        global_max = 0 
        freq = collections.defaultdict(int)
        
        while right < len(s):
            right_char = s[right]
            freq[right_char] += 1
            
            while freq[right_char] == 2:
                global_max=  max(global_max, right - left) 
                left_char= s[left]
                freq[left_char] -= 1
                left += 1
                
            right += 1
            
            
        global_max = max(global_max, right-left)
        return global_max
        
        
        """
                  r
        p w w k e 
        0 1 2 3 4 
            l
        
        global_max = 2
        freq = {p : 0, w : 1, k:1, e:1
        
        
        """
        
        
        
        
        
        
        
        
        
        
        
        
