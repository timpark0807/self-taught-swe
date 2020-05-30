class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        
        
        state 
        
        base case
        
        decisions
        
        """
        self.memo = {}
        self.mapping = {0:1, 1:7, 2:30}
        return self.dfs(days, costs, 0)
    
    def dfs(self, days, costs, index):
        if index in self.memo:
            return self.memo[index]
        if index == len(days):
            return 0
        
        answer = float('inf')
        for ticket, cost in enumerate(costs):
            maxDay = days[index] + self.mapping[ticket]
            check = index
            while check < len(days) and days[check] < maxDay:
                check += 1
                
            answer = min(answer, self.dfs(days, costs, check) + cost)
        self.memo[index] = answer
        return answer
