class Solution:
    def romanToInt(self, s):
        translate = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        special = {'I':{'V', 'X'}, 'X':{'L', 'C'}, 'C':{'D', 'M'}}
        
        index = 0 
        ans = 0 
        
        while index < len(s):
            char = s[index] 
            
            if index == len(s) - 1 or char not in special or s[index+1] not in special[char]:
                ans += translate[char]
                index += 1
            else: 
                next_char = s[index+1]
                ans += translate[next_char] - translate[char]
                index += 2 
        
        
        return ans 
