import collections

class Solution(object):
    def countComponents(self, n, edges):

        # Create adjacency list 
        graph = {}
        for x, y in edges:
            if x in graph:
                graph[x].append(y)
            else:
                graph[x] = [y]
                
            if y in graph:
                graph[y].append(x)
            else:
                graph[y] = [x]

        def dfs(node, seen):
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(neighbor, seen)
                       
        seen = set()
        count = 0 

        for node in range(n):
            if node not in seen:
                dfs(node, seen)
                count += 1
                
        return count 



edges = [[0, 1], [1, 2], [3, 4]]
s = Solution()
ans = s.countComponents(5, edges)
print(ans)
