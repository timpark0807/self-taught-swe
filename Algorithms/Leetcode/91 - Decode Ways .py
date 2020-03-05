class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        
        
        "226"
          ^ 
        
        
        last = 2 
        
        num = 22 
        """
        
        self.memo = {} 
        return self.dp(s, 0)
    
    
    def dp(self, string, index):
        if index in self.memo:
            return self.memo[index]
        
        if index == len(string):
            return 1
        if string[index] == '0':
            return 0
        
        go_one, go_two = 0, 0

        go_one = self.dp(string, index+1)
        
        if index + 2 <= len(string) and 1 <= int(string[index:index+2]) <= 26:
            go_two = self.dp(string, index+2) 
        
        self.memo[index] = go_one + go_two
        return go_one + go_two 
    

    
    
    
    
s = Solution()
print(s.numDecodings('01'))
'''
'12'
   ^



 
'''


print(s.numDecodings('226'))

    
    
    
    
    
    
    
    
    
    
    
