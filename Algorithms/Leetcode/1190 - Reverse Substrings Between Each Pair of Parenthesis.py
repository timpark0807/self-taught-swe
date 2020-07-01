class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        
        "(u(love)i)
         (uevoli)
         (iloveu)
         
         (ed(et(oc))el)
         (ed(etco)el)
         (edocteel)
         (leetcode)
         
         a(bcdefghijkl(mno)p)q
           ^ 
         stack = [a ( 
                        ^
                                    
        queue = [i, l, o, v, e, u 
        
        iterate over the input with char
            - if the char is not ')': push to stack
            - if char is ')': perform reversal 
                - pop characters off stack and push into a temp queue until we reach an open parenthesis 
                - push temp queue onto the stack 
                
        join the charactersi n the stack 
        
        (u(love)i)
                 ^
        """
        if not s:
            return ''
        
        stack = [] 
        for char in s:
            if char == '(' or char.isalpha():
                stack.append(char) 
            else:
                temp = collections.deque()
                
                while stack[-1] != '(':
                    val = stack.pop()
                    temp.append(val) 
                
                stack.pop() 

                while temp:
                    newVal = temp.popleft()
                    stack.append(newVal)
                    
                
        return ''.join(stack) 
    










    
    
    
    
    
    
    
    
    
    
