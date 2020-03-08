class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        
                   v  
        s = "a b c a b c"
             0 1 2 3 4 5 
             ^  
          
         a : 1 
         b : 1 
         c : 1
        Everytime we meet a valid window 
            - Add current window + to the end of the string
            - Contract window 
            
        """
        if len(s) < 3:
            return 0 
        
        left, right = 0, 0 
        answer =  0 
        freq = collections.defaultdict(int) 
        
        while right < len(s):
            right_char = s[right] 
            
            if right_char in 'abc':
                freq[right_char] += 1
                
            while len(freq) == 3:
                answer += len(s) - right 
                left_char = s[left]
                if left_char in 'abc':
                    freq[left_char] -= 1
                    if freq[left_char] == 0:
                        del freq[left_char]
                left += 1
            right += 1
            
        return answer  
    
