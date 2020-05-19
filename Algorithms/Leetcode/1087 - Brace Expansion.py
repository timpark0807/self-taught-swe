class Solution(object):
    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        answers = []
        processed = self.processInput(S)
        self.dfs(processed, answers, [], 0) 
        return answers
    
    def dfs(self, arr, answers, curr, outer):
        if len(curr) == len(arr):
            answers.append(''.join(curr)) 
            return 
        
        for index in range(len(arr[outer])):
            self.dfs(arr, answers, curr + [arr[outer][index]], outer+1)
            
    
    def processInput(self, S):
        
        """
        "{a,b}c{d,e}f"
         ^ 
        """
        
        index = 0 
        retval = [] 
        
        while index < len(S):
            if S[index] == '{':
                temp = []
                while S[index] != '}':
                    if S[index] != ',':
                        temp.append(S[index])
                    index += 1
                retval.append(sorted(temp[1:]))
                index += 1
            else:
                retval.append([S[index]])
                index +=1 
        
        return retval
