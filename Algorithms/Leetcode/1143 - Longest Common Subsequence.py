class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        self.memo = {}
        return self.dp(text1, text2, 0, 0)
    
    def dp(self, text1, text2, p1, p2):
        if (p1, p2) in self.memo:
            return self.memo[(p1,p2)]
        if p1 == len(text1) or p2 == len(text2):
            return 0
        
        if text1[p1] == text2[p2]:
            return self.dp(text1, text2, p1+1, p2+1) + 1
        
        self.memo[(p1,p2)] = max(self.dp(text1, text2, p1+1, p2),
                                 self.dp(text1, text2, p1, p2+1))
        return self.memo[(p1,p2)]
