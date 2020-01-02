import collections
import heapq

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        
        freq = {
                e:2
                r:1
                t:1
                }
        """
        if not s:
            return ''
        
        freq = collections.defaultdict(int)
        
        for letter in s:
            freq[letter] += 1
            
        heap = []
        
        for letter, count in freq.items():
            heap.append((-count, letter))
        
        heapq.heapify(heap)
        
        retval = ''
        while heap:
            curr = heapq.heappop(heap)
            for i in range(abs(curr[0])):
                retval += curr[1]
                
        return retval 
            
