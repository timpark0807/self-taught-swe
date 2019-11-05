class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return []
        elif len(intervals) == 1:
            return intervals
        
        intervals.sort()
        output = [intervals[0]]
        x = 0

        for interval in intervals:
            front = max(output[-1][0], interval[0])
            back = min(output[-1][1], interval[1])

            if back - front >= 0:
                output[-1] = [min(output[-1][0], interval[0]),
                              max(output[-1][1], interval[1])]
            else:
                output.append(interval)

        return output 

            
