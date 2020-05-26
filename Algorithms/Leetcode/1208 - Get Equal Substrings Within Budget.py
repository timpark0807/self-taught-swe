class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        
           l    r
        "a b c d"
         0 1 2 3
         
         
        "b c d f"
         0 1 2 3 
        """
        
        left, right = 0, 0 
        currCost, maxLength = 0, 0
        
        while right < len(s):
            
            currCost += abs(ord(s[right]) - ord(t[right]))
            
            while currCost > maxCost:
                maxLength = max(maxLength, right - left) # to do: check off by one
                currCost -= abs(ord(s[left]) - ord(t[left])) 
                left += 1    
                
            right += 1
            
        maxLength = max(maxLength, right - left) 
        
        return maxLength 
