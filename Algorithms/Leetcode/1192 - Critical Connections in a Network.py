class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
         
        connections = [[0,1],[1,2],[2,0],[1,3]]
        
        remove each connection
        Run union find
        If it becomes 2 connected componnets
            return that connection
        
        """

        adj_list = collections.defaultdict(list)
        for x, y in connections:
            adj_list[x].append(y)
            adj_list[y].append(x)
            
        pre = [-1 for i in range(n)]
        low = [-1 for i in range(n)]
        
        res = []
        self.count = 0 
        self.res = []

        self.dfs(None, 0, low, pre, adj_list)
        
        return self.res
     
    def dfs(self, parent, curr, low, pre, adj_list):
        pre[curr] = self.count
        low[curr] = self.count 
        self.count +=1 
        
        for neighbor in adj_list[curr]:
            if pre[neighbor] == -1:
                self.dfs(curr, neighbor, low, pre, adj_list)
                low[curr] = min(low[curr], low[neighbor])
                if low[neighbor] == pre[neighbor]:
                    self.res.append((curr, neighbor))

            elif neighbor != parent:
                low[curr] = min(low[curr], pre[neighbor])
