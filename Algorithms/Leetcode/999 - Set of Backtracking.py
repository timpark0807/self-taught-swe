class Solution(object):
    def wordBreak(self, s, wordDict):
        self.memo = {} 
        return self.dfs(s, set(wordDict), 0, 0)
    
    def dfs(self, s, wordDict, left, right):
        if (left, right) in self.memo:
            return self.memo[(left, right)] 
        if right == len(s) and s[left:right] in wordDict:
            return True 
        if right == len(s):
            return False 
        
        breakThis = False         
        if s[left:right] in wordDict:
            breakThis = self.dfs(s, wordDict, right, right) 
        
        continueThis = self.dfs(s, wordDict, left, right+1) 
        self.memo[(left, right)] = breakThis or continueThis
        return breakThis or continueThis 
                    
    def subsets(self, nums):
        answers = []
        self.backtrack(nums, answers, [], 0)
        return answers 
    
    def backtrack(self, nums, answers, curr, start):
        answers.append(curr[::])
        for index in range(start, len(nums)):
            curr.append(nums[index])
            self.backtrack(nums, answers, curr, index+1) 
            curr.pop()

    def generateParenthesis(self, n):
        if n == 0:
            return [] 
        answers = [] 
        self.backtrack(answers, n, [], 0, 0)
        return answers
    
    def backtrack(self, answers, n, curr, left, right):
        if right > left or left == n + 1: 
            return 
        if left == right and len(curr) == n*2:
            answers.append(''.join(curr)) 
            return 
        placeLeft = self.backtrack(answers, n, curr+['('], left+1, right)
        placeRight = self.backtrack(answers, n, curr+[')'], left, right+1)

    def letterCombinations(self, digits):
        if not digits:
            return []
        
        self.mapping = {
                        '2' : 'abc',
                        '3' : 'def',
                        '4' : 'ghi',
                        '5' : 'jkl',
                        '6' : 'mno',
                        '7' : 'pqrs',
                        '8' : 'tuv',
                        '9' : 'wxyz'} 
        answer = []
        self.backtrack(digits, answer, [], 0)
        return answer
    
    def backtrack(self, digits, answer, curr, digitIndex):
        if len(curr) == len(digits):
            answer.append(''.join(curr))
            return 
        
        currDigit = digits[digitIndex] 
        
        for letter in self.mapping[currDigit]:
            
            self.backtrack(digits, answer, curr+[letter], digitIndex+1)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
             
    
    
    
    
