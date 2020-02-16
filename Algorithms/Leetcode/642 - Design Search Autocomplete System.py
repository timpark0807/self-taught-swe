import heapq

class Trie:
    
    def __init__(self, words=[]):
        self.neighbors = {}
        self.words = [] 
        

class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.hotness = collections.defaultdict(int)
        self.trie = Trie()
        self.curr_word = []
        self.curr_tries = [self.trie] 
        
        for word in sentences:
            self.insert(word)

        for index in range(len(sentences)):
            self.hotness[sentences[index]] = times[index] 
        
    def insert(self, word):
        curr = self.trie 
        for letter in word:
            if letter not in curr.neighbors:
                curr.neighbors[letter] = Trie()
            curr = curr.neighbors[letter]
            curr.words.append(word)     
            
            
    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        curr_trie = self.curr_tries[-1]
        
        if c == '#': 
            word = ''.join(self.curr_word)
            self.insert(word)
            self.hotness[word] += 1            
            for trie in self.curr_tries[1:]:
                trie.words.append(word)
            self.curr_word = []
            self.curr_tries = [self.trie]
            return [] 
        elif c not in curr_trie.neighbors:
            self.curr_word.append(c)
            curr_trie.neighbors[c] = Trie()
            self.curr_tries.append(curr_trie.neighbors[c])
            return []
        
        elif c in curr_trie.neighbors:
            self.curr_word.append(c)
            self.curr_tries.append(curr_trie.neighbors[c])
            return self.get_hottest()

        
    def get_hottest(self):
        curr_trie = self.curr_tries[-1]
        heap = []
        for word in set(curr_trie.words):
            heapq.heappush(heap, (-self.hotness[word], word))            
        return [word for hot, word in sorted(heap)[:3]]
                
                
                
                
                
                
                


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
