class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        reversed_words = [word[::-1] for word in set(words)] 
        
        trie = self.getTrie(reversed_words) 
        answer = [] 
        for word in reversed_words:
            curr = trie 
            for letter in word: 
                curr = curr[letter] 
            if len(curr) == 1:
                answer.append(word) 
        print(answer) 
        return len('#'.join(answer))+1
    
    
    def getTrie(self, words):
        trie = {} 
        
        for word in words:
            curr = trie 
            for letter in word:
                if letter not in curr:
                    curr[letter] = {}
                curr = curr[letter] 
            curr['-'] = word 
        return trie
