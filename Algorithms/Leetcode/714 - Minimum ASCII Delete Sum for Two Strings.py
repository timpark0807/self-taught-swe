 Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        
        s1 = sea
                ^
             
        s2 = eat
               ^
             
        Type: Optimization (min)
        
        State: p1, p2 
        
        Base Case: 
        
            p1 out of bounds: return sum of remaining p2 letters 
            p2 out of bounds: return sum of remaining p1 letters
            
            s1[p1] == s2[p2]: return dp(p1+1, p2+1) 
        
        Decision: 
            
            Delete_1:  dp(p1+1, p2) + ord(s1[p1])
            Delete_2: dp(p1, p2+1) + ord(s2[p2])
        
        Recurrence:
        
            dp(p1, p2) = min(delete_1, delete_2)

        """
        self.memo = {}
        return self.dp(s1, s2, 0, 0)
    
    def dp(self, s1, s2, p1, p2):
        if (p1, p2) in self.memo:
            return self.memo[(p1, p2)]
        if p1 == len(s1) and p2 == len(s2):
            return 0
        elif p1 == len(s1):
            return self.get_remain(s2, p2)
        elif p2 == len(s2): 
            return self.get_remain(s1, p1)
        elif s1[p1] == s2[p2]:
            return self.dp(s1, s2, p1+1, p2+1)
    
        self.memo[(p1, p2)] = min(self.dp(s1, s2, p1+1, p2) + ord(s1[p1]), 
                                  self.dp(s1, s2, p1, p2+1) + ord(s2[p2]))
        
        return self.memo[(p1, p2)] 
        
        
    def get_remain(self, word, pointer):
        total = 0
        for index in range(pointer, len(word)):
            total += ord(word[index])
        return total
