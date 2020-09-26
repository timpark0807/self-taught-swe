class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if not intervals:
            return [] 
        
        intervals.sort() 
        answer = [intervals[0]] 

        for interval in intervals[1:]:
            if self.overlap(interval, answer[-1]):
                answer[-1] = self.combine(interval, answer[-1])
            else:
                answer.append(interval) 

        return answer
    
    def overlap(self, interval1, interval2):
        front = max(interval1[0], interval2[0])
        back = min(interval1[1], interval2[1])
        return back-front>=0 
    
    def combine(self, interval1, interval2):
        front = min(interval1[0], interval2[0])
        back = max(interval1[1], interval2[1])
        return [front, back]
    
    
