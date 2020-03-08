class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        
        n = 6
        headID = 2
        
        manager = [2,2,-1,2,2,2]
        informTime = [0,0,1,0,0,0]
        """
        if n == 1:
            return 0 
        
        adj_list = self.get_adj_list(n, manager, informTime)
        
        heap = [(0, headID)]
        max_value = 0 
        
        while heap:
            curr_time, curr_id = heapq.heappop(heap)
            max_value = max(max_value, curr_time)
            for time_needed, subs in adj_list[curr_id]:
                heapq.heappush(heap, (curr_time + time_needed, subs))
                
        return max_value
    
    
    def get_adj_list(self, n, manager, informTime):
        adj_list = collections.defaultdict(list)
        for index in range(n):
            curr_manager = manager[index]
            curr_time = informTime[curr_manager]
            adj_list[curr_manager].append((curr_time, index))
        return adj_list
    
    
    
    
    
    
    
    
    
    
