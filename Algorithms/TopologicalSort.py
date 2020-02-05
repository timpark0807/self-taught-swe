import collections

class TopologicalSort:
    """
    Topological Sort Implementation

    Time  : O(V+E)
    Space : O(V+E)
    """

    def top_sort(self, edges, n):
        adj_list, indegrees = self.get_adj_list_indegrees(n, edges)    
        nodes_with_no_indegrees = self.get_nodes_with_no_indegrees(indegrees)
        output = []
        while nodes_with_no_indegrees:
            current = nodes_with_no_indegrees.pop()
            output.append(current)
            for neighbor in adj_list[current]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    nodes_with_no_indegrees.append(neighbor)
        return output

    def get_adj_list_indegrees(self, n, edges):
        adj_list = collections.defaultdict(list)
        indegrees = {i:0 for i in range(n)}
        for x, y in edges:
            adj_list[x].append(y)
            indegrees[y] += 1
        return adj_list, indegrees
    
    def get_nodes_with_no_indegrees(self, indegrees):
        temp = []
        for node, value in indegrees.items():
            if value == 0:
                temp.append(node)
        return temp
    
edges = [
        [0, 1],
        [0, 2],
        [0, 3],
        [1, 4],
        [4, 5],
        ]

s = TopologicalSort()
answer = s.top_sort(edges, 6)
print(answer)
