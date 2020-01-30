import heapq 

class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        if not edges:
            return n-1
        adj_list = self.get_adj_list(n, edges)
        num_cities = {x:[] for x in range(n)}
        
        global_min = float('inf')
        curr_city = 0
        for curr_city in range(n):
            curr_count = self.bfs(adj_list, distanceThreshold, num_cities, curr_city)
            if curr_count <= global_min:
                global_min = curr_count
                ans = curr_city
        return ans

    def bfs(self, adj_list, K, num_cities, start):
        heap = [(0, start)]
        seen = set()
        count = 0
        while heap:
            curr_dist, curr_node = heapq.heappop(heap)
            if curr_node not in seen:
                seen.add(curr_node)
                count += 1

                for neigh_node, neigh_dist in adj_list[curr_node]:
                    if neigh_node not in seen and curr_dist + neigh_dist <= K:
                        heapq.heappush(heap, (curr_dist + neigh_dist, neigh_node))
        return count

    def get_adj_list(self, n, edges):
        temp = {x:[] for x in range(n)}
        for w, v, weight in edges:
            temp[w].append((v, weight))
            temp[v].append((w, weight))
        return temp 
