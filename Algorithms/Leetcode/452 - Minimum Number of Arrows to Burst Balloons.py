class Solution(object):
    def findMinArrowShots(self, points):
        if len(points) <= 1:
            return len(points)
        
        points.sort()
        print(points)
        processed = [[points[0], points[0][1]]]
        
        for interval in points[1:]:

            if self.overlap(processed[-1][0], processed[-1][1], interval):
                processed[-1] = self.get_merge(processed[-1][0], processed[-1][1], interval)
            else:
                processed.append((interval, interval[1]))
                
        return len(processed)
        
        
    def overlap(self, interval1, earliest_end, interval2):
        front = max(interval1[0], interval2[0])
        back = min(interval1[1], interval2[1])
        return back - front >= 0 and interval2[0] <= earliest_end 
        
        
    def get_merge(self, interval1, earliest_end, interval2):
        front = min(interval1[0], interval2[0])
        back = max(interval1[1], interval2[1])
        earliest_end = min(earliest_end, interval2[1])
        return [[front, back], earliest_end]
    
arr = [[7,15],[6,14],[8,12],[3,4],[4,13],[6,14],[9,11],[6,12],[4,13]]

"""
[[3, 4], [4, 13], [4, 13], [6, 12], [6, 14], [6, 14], [7, 15], [8, 12], [9, 11]]

[[3, 4]
    [4,             13],
    [4,             13],
      [6,        12],
      [6,           14]
      [6,           14]
        [7             15],
          [8     12],
            [9,11]]
           
"""
s = Solution()
print(s.findMinArrowShots(arr))
