class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set() 
        self.answer = 0
        self.dfs(s, seen, 0) 
        return self.answer
    
    
    def dfs(self, string, seen, left):
        if left == len(string):
            self.answer = max(self.answer, len(seen)) 
            return 
        
        for right in range(left+1, len(string)+1):
            curr = string[left:right]
            if curr not in seen:
                seen.add(curr)
                self.dfs(string, seen, right) 
                seen.remove(curr)
        
        return 
                
            
    
