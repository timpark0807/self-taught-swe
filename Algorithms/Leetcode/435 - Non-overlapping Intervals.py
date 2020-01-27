class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int

        Variables Needed:
            - Processed arr 
            
        1. Iterate over the intevals array
        2. Store 'Processed' intervals in an auxillary array
        3. Check current interval versus last interval in seen  
            - If they overlap, replace last processed with the interval with smaller end time 
        
        return len(intervals) - len(processed)
                      
        """
        if len(intervals) <= 1:
            return 0 
        
        intervals.sort() 
        processed = [intervals[0]]
        
        for curr_interval in intervals[1:]:
            last_checked = processed[-1]
            if self.overlap(last_checked, curr_interval):
                processed[-1] = self.get_smaller(last_checked, curr_interval)
            else:
                processed.append(curr_interval)
                
        return len(intervals) - len(processed)
    
    def overlap(self, interval1, interval2):
        back = min(interval1[1], interval2[1])
        front = max(interval1[0], interval2[0])
        return back - front > 0
    
    def get_smaller(self, interval1, interval2):
        if interval1[1] < interval2[1]:
            return interval1
        else:
            return interval2 
        
        
            
            
            
            
            
            
