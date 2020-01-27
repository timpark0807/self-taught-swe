class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return [""]
        
        min_removals = self.get_min_removals(s)
        answers = set()
        self.backtrack(s, 0, 0, 0, min_removals, answers, '')
        
        return list(answers) 
    
    def backtrack(self, string, index, left, right, k, answers, curr):
        if index == len(string) and k == 0 and left == right and curr not in answers:
            answers.add(curr[::])
            return
        
        elif index == len(string) or k < 0 or right > left:
            return
        
        elif string[index].isalpha():
            add_alpha = self.backtrack(string, index+1, left, right, k, answers, curr + string[index])
        else:
            if string[index] == ')':
                add_left = self.backtrack(string, index+1, left, right+1, k, answers, curr + string[index])
            else:
                add_right = self.backtrack(string, index+1, left + 1, right, k, answers, curr + string[index])
                
            skip = self.backtrack(string, index+1, left, right, k-1, answers, curr)
    
    
    def get_min_removals(self, string):
        count = 0 
        stack = []
        for char in string:
            if not char.isalpha():
                if char == ')':
                    if stack:
                        stack.pop()
                    else:
                        count += 1
                else:
                    stack.append(char)
                    
        return count + len(stack)
