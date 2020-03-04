class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        
        
                              r
        [1, 3, -1, -3,  5, 3]
         0  1   2   3   4  5  
                    l       
           
        [5, 1, -2, -3
        
        k = 3
        
         5 : 1
         3 : 1 
        -1 : 0
        -3 : 1
        -2 : 1 
        
        [3, 3, 5
        
        Initialize window 
        
        While right bound is less than len(nums) 
            while count of max_heap element is 0 
                pop from max_heap
                del from dict
                
            add the max_heap element to the answers array 
            decrement the count of left
            add right to the heap 
            increment the count of right 
        """
        if not nums:
            return [] 
        
        count = collections.defaultdict(int) 
        heap = [] 
        answers = []
        left, right = 0, 0
        for index in range(k):
            heapq.heappush(heap, -nums[index])
            count[nums[index]] += 1
            right += 1
            
        while right < len(nums):
            while count[-heap[0]] == 0:
                del count[-heap[0]]
                heapq.heappop(heap)
            answers.append(-heap[0])
            count[nums[left]] -= 1
            heapq.heappush(heap, -nums[right])
            count[nums[right]] += 1
            right += 1
            left += 1
            
        while count[-heap[0]] == 0:
            del count[-heap[0]]
            heapq.heappop(heap)
        answers.append(-heap[0])
        return answers 
