class Solution(object):
    def largestNumber(self, cost, target):
        """
        :type cost: List[int]
        :type target: int
        :rtype: str
        
        [4,3,2,5,6,7,2,5,5]
        
        target = 9 
        
        type 
            - optimization 
            - unbounded knapsack
            
        state 
            - index
            - remain 
            - number 
        
        base cases
            - if target < 0: return float('-inf') 
            - target == 0: return 0 
        
        decisions
            - take this number -> dfs(index+1, remain-cost[index-1]) + str(index) 
            - continue to the next number -> dfs(index+1, remain) 
            
        return max(decision1, decision2) 
        """
        self.memo = {} 
        
        ans = self.dfs(cost, 1, target)
        
        return str(ans) if ans != float('-inf') else '0'
    
    def dfs(self, cost, index, remain):
        if (index, remain) in self.memo:
            return self.memo[(index, remain)]
        
        if remain == 0:
            return 0
        elif remain < 0 or index == len(cost)+1:
            return float('-inf')
        
        take = self.dfs(cost, 1, remain-cost[index-1]) * 10 + index
        skip = self.dfs(cost, index+1, remain) 
        self.memo[(index, remain)] = max(take, skip)
        return self.memo[(index, remain)] 
    
    def getBigger(self, num1, num2):
        if '0' in num2:
            return num1
        elif '0' in num1:
            return num2
        elif len(num1) > len(num2):
            return num1
        elif len(num2) > len(num1):
            return num2
        elif int(num1)>int(num2):
            return num1 
        else:
            return num2
        
        
        
    
    
    
    
    
    
    
    
