class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
         2 pointers 
        """
        s = self.check(S)
        t = self.check(T)
        return s == t 
    
    
    def check(self, string):
        
        stack = [] 
        
        for letter in string:
            if letter == '#' :
                if stack:
                    stack.pop()
            else:
                stack.append(letter)
                
        return stack 
                
