class Solution(object):
    def longestPalindrome(self, s):
        """
        Description: Returns the longest palindromic substring 
                    - A paldindrome is a string that reads forward and backwards the same
                    
        @param1 s   : str 
        @return ans : str
        
        Highlevel
        
        main()
        - Iterate over the input string with curr
            - Do this until we reach an invalid palindrome 
                - Be careful of index out of range errors
                - Expand outwards from curr-1 and curr+1 
                - Expand outwards from curr-1 and curr 
        
                           r 
               l         
            "a b b c c b b d"
             0 1 2 3 4 5 6 
                   ^
                  
                return string[left+1:right]
                  
                left = curr -1 
                right = curr + 1
                6 - 0 = 6 - 2 + 1 = 5
                
                5 -- 1 = 6 - 2 + 1 = 5 
                
             
        helper()
        - Pass in left and right index
        - while left and right are in range
            - Expand until not a valid palindrome 
            - 
        
            
        Checklist:            
        Brute Force 
            1. Generate all substrings, store it 
                - Iterate over all them and check if they are palindrome / find longest 
                - Time O(n^2) and space O(n^2)
                
            2. Generate all subtsring, don't store it and check if it's a palindrome
                - Time O(n^3) -> O(n^2) to generate multiplied by O(n) to check
                - Space O(1)
            
        Edge Cases
            - Null input 
            - All letters are the same?
            - Input has [1, 2] letters 
        Assumptions
            - 
        TestCases
        Toolbox
            - 2 pointers
            - Hashtable
            - Maximization problem
        
        Input -> str 
        Output -> str 
            - Goal is to maximize the substring
            
        
        Docstrings
        """
        if not s:
            return ''
        
        global_max = s[0]

        for index in range(len(s)):
            local_max = max(self.get_local_max(s, index-1, index+1), self.get_local_max(s, index, index+1), key=len)
            global_max = max(global_max, local_max, key=len)
            
        return global_max 
    
    
    
    def get_local_max(self, string, left, right):
        """
        Description: Helper function that expands outwards until it's no longer a palindrome
        
        @param1 string : str
        @param2 left   : int
        @param3 right  : int
        @return local  : str 
        """
        if left < 0 or right >= len(string):
            return ''
        
        while self.is_valid(string, left, right):
            left -= 1
            right += 1
            
        return string[left+1:right]
            
    def is_valid(self, string, left, right):
        return left >= 0 and right < len(string) and string[left] == string[right] 
    
        
        
        
        
        
        
        
    
