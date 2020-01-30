import heapq
import collections
class Solution(object):
    def rearrangeString(self, s, k):
        if k == 0:
            return s
        
        freq = self.get_freq(s)
        heap = self.get_heap(freq)
        ans = []
        
        while heap:
            temp = []
            for _ in range(k):
                if heap:
                    curr_count , curr_letter = heapq.heappop(heap)
                    ans.append(curr_letter)
                    temp.append((curr_count+1, curr_letter))
                elif not heap and len(ans) != len(s):
                    return ''
            for item in temp:
                if item[0] < 0:
                    heapq.heappush(heap, item)

                    
        return ''.join(ans) 

    
    
    def get_freq(self, word):
        temp = collections.defaultdict(int)
        for letter in word:
            temp[letter] += 1
        return temp
    
    def get_heap(self, freq):
        heap = []
        for key, value in freq.items():
            heapq.heappush(heap, (-value, key))
        return heap
    
