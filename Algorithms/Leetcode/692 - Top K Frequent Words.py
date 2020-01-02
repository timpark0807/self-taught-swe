import collections
import heapq

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq = collections.defaultdict(int)
        words.sort() 
        
        for word in words:
            freq[word] += 1
            
        heap = []
        
        for word, count in freq.items():
            heap.append((-count, word))
            
        heapq.heapify(heap)
        retval = []
        
        for i in range(k):
            retval.append(heapq.heappop(heap)[1])
            
        return retval
