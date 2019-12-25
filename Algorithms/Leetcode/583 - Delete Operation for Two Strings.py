class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        
        sea
          ^
        eat
           ^ 
        
        State: pointer_1, pointer_2
        
        Base Case:
            - Either Pointer is out of bounds
            - Pointers are equal
            
        Decision:
            - Delete from Word 1
            - Delete from Word 2
            
        Recurrence: min(delete_1, delete_2)
        
        """
        self.memo = {}
        return self.dp(word1, word2, 0, 0)
    
    
    def dp(self, word1, word2, p1, p2):
        if (p1, p2) in self.memo:
            return self.memo[(p1, p2)]
        if p1 == len(word1) and p2 == len(word2):
            return 0
        elif p1 == len(word1):
            return len(word2) - p2
        elif p2 == len(word2):
            return len(word1) - p1
        
        if word1[p1] == word2[p2]:
            return self.dp(word1, word2, p1+1, p2+1)
        
        self.memo[(p1, p2)] = min(self.dp(word1, word2, p1+1, p2),
                                  self.dp(word1, word2, p1, p2+1)) + 1
        
        return self.memo[(p1, p2)]
