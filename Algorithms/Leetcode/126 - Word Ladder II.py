import collections

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        (hit) -> (hot) -> (dot)
                   |        |
                   v        v
                 (lot)    (dog)
                   |        /
                   v       /
                 (log)  <--
                   |      /
                   v     /
                 (cog)  <


        # Step 1. Build an adjacency list
                    hit : [hot]
                    hot : [dot, lot]
                    lot : [log]
                    dot : [dog]
                    dog : [log, cog]
                    log : [cog]
                    cog : []

        # Step 2. Perform a Breadth First Search
                  -> Start Node = beginWord
                  -> End Node = endWord
                  -> Use a queue (initialize with start word)
                  -> Deque
                  -> If current word == End word, add current path to answers
                  -> 
                  -> For neighbors of curr: check if we've seen and add them to queue
                  -> 
        """
        if endWord not in wordList:
            return []
        if beginWord not in wordList:
            wordList.append(beginWord)
            
        adj_list = self.get_adj_list(beginWord, wordList)
        queue = collections.deque([(beginWord, [beginWord])])
        global_seen = set([beginWord])
        answers = []
        
        while queue:
            
            local_seen = set()
            
            for _ in range(len(queue)):
                curr_word, curr_path = queue.popleft()
                    
                if curr_word == endWord:
                    answers.append(curr_path)
                    continue
                
                for neighbor in adj_list[curr_word]:
                    if neighbor not in global_seen:
                        local_seen.add(neighbor)
                        queue.append((neighbor, curr_path + [neighbor]))

            if answers:
                return answers
                                    
            for word in local_seen:
                global_seen.add(word)
                
        return []
    
    def get_adj_list(self, beginWord, wordList):
        temp = collections.defaultdict(list)
        wordSet = set(wordList)
        for word in wordList:
            for transformed_word in self.get_potential_words(word, beginWord, wordList):
                if transformed_word != word and transformed_word in wordSet:
                    temp[word].append(transformed_word)
        return temp

    def get_potential_words(self, word, beginWord, wordList):
        potential_words = []
        for index in range(len(beginWord)):
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                potential_words.append(word[:index] + letter + word[index+1:])
        return potential_words

beginWord = "game"
endWord = "thee"
wordList = ["frye","heat","tree","thee","game","free","hell","fame","faye"]

s = Solution()
print(s.findLadders(beginWord, endWord, wordList))

