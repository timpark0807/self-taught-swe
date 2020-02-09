import collections

class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        if N <= 2:
            return True
        
        colors = {}
        adj_list = {i:[] for i in range(1, N+1)}
        
        for a, b in dislikes:
            adj_list[a].append(b)
            adj_list[b].append(a)
            
        
        for node in range(1, N+1):
            if node not in colors and not self.dfs_can_color(node, adj_list, colors):
                return False                
                
        return True 
    
    
    def dfs_can_color(self, node, adj_list, colors):
        queue = collections.deque([node])
        colors[node] = 1 
        
        while queue:
            curr_node = queue.popleft()
            
            for neighbor in adj_list[curr_node]:
                if neighbor in colors and colors[neighbor] == colors[curr_node]:
                    return False
                elif neighbor not in colors:
                    colors[neighbor] = -colors[curr_node]
                    queue.append(neighbor)
                    
        return True
        
    
            
