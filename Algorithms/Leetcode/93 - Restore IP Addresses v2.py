class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12:
            return []
        ans = []
        self.backtrack(s, ans, [], 0)
        return ans
    
    
    def backtrack(self, string, answer, curr, start):
        
        if start == len(string) and len(curr) == 4:
            answer.append('.'.join(curr))
            return 
        if start >= len(string):
            return 
        
        for index in range(1, 4): 
            num = string[start:start+index]
            if index != 1 and num[0] == '0':
                return 

            if 0 <= int(num) <= 255:
                self.backtrack(string, answer, curr+[num], start+index)
            
