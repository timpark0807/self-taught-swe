import unittest
import collections

class Solution:

    def ladderLength(self, beginWord, endWord, wordList):
        wordList.append(beginWord)
        adjList = self.getAdjList(wordList)
        seen = set([beginWord])
        queue = collections.deque([(beginWord, 1)])

        while queue:
            
            currWord, currSteps = queue.popleft()
            if currWord == endWord:
                return currSteps
            
            for neighbor in adjList[currWord]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, currSteps+1)) 

        return 0 
        
    def getAdjList(self, wordList):
        adjList = collections.defaultdict(list)
        wordSet = set(wordList)
        
        for word1 in wordList:
            for index in range(len(word1)):
                for letter in 'abcdefghijklmnopqrstuvwxyz':
                    check = word1[:index] + letter + word1[index+1:]
                    if word1 != check and check in wordSet:
                        adjList[word1].append(check)
        return adjList

        

        
class TestSolution(unittest.TestCase):
    def test_one(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        answer = Solution().ladderLength(beginWord, endWord, wordList)
        self.assertEqual(answer, 5) 



if __name__ == '__main__':
    unittest.main()
    
