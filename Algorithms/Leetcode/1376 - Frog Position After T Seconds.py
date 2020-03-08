class Solution(object):
    def frogPosition(self, n, edges, t, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """
        if n == 1:
            return 1
         
        adj_list = collections.defaultdict(set)
        adj_list[1].add(1) 
        
        for x, y in edges:
            adj_list[x].add(y)
            adj_list[y].add(x)
    
            
        queue = collections.deque([(1,1)])
        seen = set([1])
        print(adj_list)
        while queue and t >= 0: 
            for _ in range(len(queue)):
                curr_node, curr_prob = queue.popleft()
                print(curr_node, adj_list[curr_node])
                if curr_node == target and (len(adj_list[curr_node]) == 1 or t==0):
                    return curr_prob
                for neighbor in adj_list[curr_node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        new_prob = curr_prob / float(len(adj_list[curr_node])-1)
                        queue.append((neighbor, new_prob))
            t -= 1 
            
        return 0.0
    
            

            
