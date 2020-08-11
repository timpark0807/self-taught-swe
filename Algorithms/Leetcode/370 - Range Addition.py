class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        
        
        [0, 0, 0, 0, 0]
        
         0   1   2  3  4 
    s = [-2, 2,  3, 0, 0]
    
    e = [ 0, 0, 2, -2,-3] 
                
        [-2, 0,]
        """
        start = [0] * length
        end = [0] * length
        
        for s, e, k in updates:
            start[s] += k
            end[e] -= k
            
        ps = 0 
        answer = [0] * length 
        for index in range(length):
            ps += start[index]
            answer[index] = ps
            ps += end[index]
            
        return answer 
