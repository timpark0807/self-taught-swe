class Solution:
    
    def solve(self, s, words):
        answer = []
        self.root = self.buildTrie(words) 
        self.backtrack(s, words, answer, [], self.root, 0)
        return answer 

    def backtrack(self, s, words, answer, currSentence, currTrie, index):
        if index == len(s):
            if currTrie == self.root:
                answer.append(' '.join(currSentence))  
            elif '-' in currTrie:
                answer.append(' '.join(currSentence) + ' ' + currTrie['-'])
            return 
        
        currChar = s[index] 
        if currChar.isalpha() and currChar in currTrie:
            self.backtrack(s, words, answer, currSentence, currTrie[currChar], index+1) 
            
        if currChar == ' ' and '-' in currTrie:            
            currSentence.append(currTrie['-'])
            self.backtrack(s, words, answer, currSentence, self.root, index+1) 
            currSentence.pop() 
            
        if currChar == ' ' and 'e' in currTrie:
            self.backtrack(s, words, answer, currSentence, currTrie['e'], index+1)
            
    
    def buildTrie(self, words):
        root = {}
        
        for word in words:
            curr = root
            for letter in word:
                if letter not in curr:
                    curr[letter] = {}
                curr = curr[letter]
            curr['-'] = word 
            
        return root 
    
s = "can s r n "   
words = ["can", "canes", "serene", "rene", "sam"]

sol = Solution()   
ans = sol.solve(s, words)    
print(ans)
