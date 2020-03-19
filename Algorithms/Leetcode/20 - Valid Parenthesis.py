class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True 
        
        stack = [] 
        match = {')':'(', '}':'{', ']':'['}
        
        for char in s:
            if char in '({[':
                stack.append(char)
                 
            elif char in ')}]':
                if not stack or stack[-1] != match[char]:
                    return False
                else:
                    stack.pop()
                    
        return not stack 
