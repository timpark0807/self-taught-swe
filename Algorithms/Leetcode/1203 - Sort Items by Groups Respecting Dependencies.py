import collections

class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        
        [[],[6],[5],[6],[3,6],[],[],[]]
          0  1   2   3    4    5  6  7
        
        # Ordering of the groups
        
            # Map each node to it's group
            # Map each group to its nodes

            # Iterate over beforeItems
                # If the dependency is inter-group related
                    # Add 1 to the group indegrees
                        # Group Indegrees : {-1: 1 
                                              0:
                                              1:
                                              2: }
                # Else 
                    # Add to node indegrees
                        # Node Indegrees = {0: 0
                                            1: 1
                                            2: 1
                                            3: 1
                                            4: 1
                                            5: 0
                                            6: 0
                                            7: 0
                                            }
        # Iterate over the groups
            # If the group has 0 indegrees
                # Place all nodes with 0 indegrees from that group
            
        # Top Sort
        # while there are nodes in our group queue
            # Remove current node from queue 
            # if current nodes group was not seen already
                # Create a group top sort
                # Have a second queue to process all nodes in our group 
                # Remove all of current node's outdegrees 
                # Append the neighbor to the queue if indegrees[neighbor] == 0
            # Add group top sort to answer top sort
            
        # Join answer top sort and return it 
        """
        group2nodes = self._get_group2nodes(n, m, group)
        nodes2group = self._get_nodes2group(n, m, group)
        adj_list, node_indegrees, group_indegrees = self._get_adj_list_indegrees(n, m, beforeItems, nodes2group)
        
        outer_queue = self._get_outer_queue(group_indegrees, group2nodes, node_indegrees, nodes2group)                    
        processed_groups = set()
        outer_topsort = [] 
        
        while outer_queue:
            print('**' * 20)
            print(outer_topsort)
            print('outer_queue', outer_queue)
            curr_group, curr_node = outer_queue.popleft()
            print('curr_group:', curr_group)
            if curr_group in processed_groups:
                continue
            
            processed_groups.add(curr_group)
            inner_queue = self._get_inner_queue(curr_group, group2nodes, node_indegrees)
            inner_topsort = []
            print('inner', inner_queue)
            
            while inner_queue:
                inner_node = inner_queue.popleft()
                inner_topsort.append(inner_node)
                inner_group = nodes2group[inner_node]
                print('inner node:', inner_node)

                for neighbor in adj_list[inner_node]:
                    node_indegrees[neighbor] -= 1
                    neighbor_group = nodes2group[neighbor]
                    print('neighbor', neighbor)
                    print('neighbor group', neighbor_group)
                    if neighbor_group != -1 and neighbor_group != curr_group:
                        group_indegrees[neighbor_group] -= 1
                        if group_indegrees[neighbor_group] == 0:
                            outer_queue.append((neighbor_group, neighbor))
                    
                    if node_indegrees[neighbor] == 0 and neighbor_group == curr_group:
                        inner_queue.append(neighbor)
                            
            outer_topsort.append(inner_topsort)

        
        retval = []
        for inner_group in outer_topsort:
            for node in inner_group:
                retval.append(node)
        print(retval)
        return retval if len(retval) == n else []
        
    def _get_inner_queue(self, curr_group, group2node, node_indegrees):
        temp = collections.deque()
        for node in group2node[curr_group]:
            if node_indegrees[node] == 0:
                temp.append(node)
        return temp           
            
    def _get_adj_list_indegrees(self, n, m, beforeItems, nodes2group):
        temp_adj_list = {i:[] for i in range(n)}
        temp_indegrees = {i:0 for i in range(n)}
        temp_group_indegrees = {i:0 for i in range(m)}
        
        for node, before in enumerate(beforeItems):
            for node2 in before:
                temp_adj_list[node2].append(node)
                
                if nodes2group[node] != nodes2group[node2] and nodes2group[node] != -1:
                    temp_group_indegrees[nodes2group[node]] += 1
                
                temp_indegrees[node] += 1
                
        print('group indegrees:', temp_group_indegrees)
        print('node indegrees:', temp_indegrees)
        print('adj_list:', temp_adj_list)

        return temp_adj_list, temp_indegrees, temp_group_indegrees

    def _get_group2nodes(self, n, m, group):
        temp = {i:[] for i in range(m)}
        temp[-1] = []
        
        for node, group in enumerate(group):
            temp[group].append(node)
        return temp

    def _get_nodes2group(self, n, m, group):
        temp = {i:-1 for i in range(n)}
        for node, group in enumerate(group):
            temp[node] = group
        return temp 
        
    def _get_outer_queue(self, group_indegrees, group2nodes, node_indegrees, nodes2group):
        temp = collections.deque()
        for group_id, group_indegree in group_indegrees.items():
            if group_indegree == 0:
                temp.append((group_id, group_id))
        for node, value in node_indegrees.items():
            if nodes2group[node] == -1 and value == 0:
                temp.append((-1, node))
        return temp 
        
        
        
        
s = Solution()
print(s.sortItems(5, 5, [2,0,-1,3,0], [[2,1,3],[2,4],[],[],[]]))
