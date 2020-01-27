class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        
        " 30-2 * 2 + 1"
                     ^
        temp = 
        sign = 1
        stack = [30, -4, 1
        
        # Step 1: Iterate over the input string
        # Step 2: Check the char 
        
                    # if char == ' ': continue
                    
                    # if char.isdigit(): 
                            -> Get entire digit, multiply by sign and append to stack 
                            -> sign = 1 
                            
                    # if char == '-':
                            -> sign = -1
                            
                    # if char == '+': 
                            -> sign = 1
                            
                    # if char == * or / 
                        # get stack[-1] and next char and do the operation
                        # append answer to the stack 
                        
        # Return the sum of the stack
        """
        if not s:
            return 0
        
        sign = 1
        index = 0 
        stack = []
        
        while index < len(s):
            print(stack)
            if s[index] == ' ': 
                index += 1
                continue
            
            elif s[index].isdigit():
                num, index = self.get_next_num(s, index)
                stack.append(num * sign)
                sign = 1
                
            elif s[index] == '-':
                sign = -1
                index += 1

            elif s[index] == '+':
                sign = 1
                index += 1

            else:
                symbol = s[index]
                prev = stack.pop()
                temp = 1 
                if prev < 0: temp = -1 
                index += 1
                
                while not s[index].isdigit():
                    index += 1
                    
                num, index = self.get_next_num(s, index)
                
                if symbol == '*':
                    stack.append(prev * num)
                else:
                    stack.append(temp * (abs(prev) // num)) 
        print(stack)
        return sum(stack)
    
    
    def get_next_num(self, s, index):
        num = ''
        while index < len(s) and s[index].isdigit():
            num += s[index]
            index += 1
        return int(num), index

s = Solution()
print(s.calculate("14-3/2"))
