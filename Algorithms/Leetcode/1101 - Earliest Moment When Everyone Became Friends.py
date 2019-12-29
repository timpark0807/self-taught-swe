class Solution(object):
    def earliestAcq(self, logs, N):
        """
        :type logs: List[List[int]]
        :type N: int
        :rtype: int
        """
        self.parents = [-1] * N
        logs.sort()
        count = N
        for time, personA, personB in logs:
            if self.union(personA, personB):
                count -= 1
            if count == 1:
                return time
            
        return -1    
        
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            self.parents[rootX] = rootY
            return True
        else:
            return False
        
    def find(self, x):
        while self.parents[x] != -1:
            x = self.parents[x]
        return x
    
            
