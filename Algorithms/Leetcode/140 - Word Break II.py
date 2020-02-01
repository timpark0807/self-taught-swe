class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        
        
        wordSet = set(wordDict) 
        
        
        s = "catsanddog"
                 ^ 
        BaseCase:
            if not s:
                append current to answer 
            
            
        Decision:
            if begin to current index is a valid word:
                Split Here : helper(s[index:], wordSet, index, curr)
                
            Keep Going : helper(s, wordSet, index+1, curr)
        
        """
        if not self.can_break(s, wordDict):
            return [] 
        
        answers = []
        wordSet = set(wordDict)
        self.helper(s, wordSet, answers, [], 0)
        return answers
    
    def helper(self, s, wordSet, answers, curr, index):
        if not s:
            answers.append(' '.join(curr))
            return

        elif s[:index] in wordSet:
            split_here = self.helper(s[index:], wordSet, answers, curr + [s[:index]], 0)
            
        if index == len(s):
            return 
        
        keep_going = self.helper(s, wordSet, answers, curr, index+1)
        
        
    def can_break(self, s, wordDict):
        self.memo = {}
        return self.dp(s, set(wordDict), 0, 0)
        
        
    def dp(self, s, wordDict, left, right):
        if (left, right) in self.memo:
            return self.memo[(left, right)]
        if right == len(s):
            return s[left:right] in wordDict
        
        break_word = False
        
        if s[left:right] in wordDict:
            break_word = self.dp(s, wordDict, right, right)
        
        continue_word = self.dp(s, wordDict, left, right+1)
        
        self.memo[(left, right)] = break_word or continue_word
        
        return self.memo[(left, right)] 
        
        
        
        
        
        
        
        
        
        
        
        
        
