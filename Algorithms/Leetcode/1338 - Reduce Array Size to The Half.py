import collections
import heapq

class Solution(object):
    def minSetSize(self, arr):
        if not arr:
            return 0 
        
        curr_size = len(arr)
        target = len(arr) // 2
        
        freq = collections.Counter(arr) 
        counts = list(freq.values())
        counts.sort()

        ans = 0 
        for count in counts[::-1]:
            curr_size -= count
            ans += 1
            if curr_size <= target:
                return ans 
        """
        :type arr: List[int]
        :rtype: int
        
        BEATIO HD
        
        Brute Force
        Edge Cases
        Assumptions
        Test Case
        Toolbox
            - Hashtables
            - Minimum ? -> opitmization aka dp or greedy 
            
        
        Input/output
        @param1 arr : arr()
        @return int : int 
        
        Highlevel 
        
        Get a count of each element in the array 
        Add all these to a heap (count, element)
        pop off from heap 
        decrement count by the number of count 
        if curr size < len(arr) // 2 return how many we've odne 
        
        
        Docstrings
        arr = [3,3,3,3,5,5,5,2,2,7]
        
        3 : 4 
        5 : 3 
        2 : 2 
        7 : 1
        
        [1,2,3,4,5,6,7,8,9,10]
        
        
        """
    def minSetSize(self, arr):
        if not arr:
            return 0 
        
        freq = collections.Counter(arr) 
        
        heap = [] 
        
        arr = list(freq.values()).sort()
               
        curr_size = len(arr)
        target = len(arr) // 2
        ans = 0 
        
        while curr_size > target: 
            curr_count, curr_num = heapq.heappop(heap)
            curr_size += curr_count
            ans += 1

            
        return ans 
            
            
            
            

s = Solution()
print(s.minSetSize([1,2,3,4,5,6,7,8,9,10]))

