class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return [] 
        
        queue = collections.deque([(1, beginWord, [beginWord])])
        seen = set([beginWord]) 
        answers = [] 
        
        while queue:
            temp = set() 
            for _ in range(len(queue)):
                curr_dist, curr_word, curr_path = queue.popleft() 
                if curr_word == endWord:
                    answers.append(curr_path)
                for neighbor in self._get_neighbors(curr_word, wordList):
                    if neighbor not in seen:
                        temp.add(neighbor)
                        queue.append((curr_dist+1, neighbor, curr_path + [neighbor]))
            
            for word in temp:
                seen.add(word)
            
                        
        return answers
    
        
    def _get_neighbors(self, word1, words):
        valid = []
        words = set(words) 
        
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            for index in range(len(word1)):
                test_word = word1[:index] + letter + word1[index+1:] 
                if test_word in words:
                    valid.append(test_word)
     
        return valid
    
