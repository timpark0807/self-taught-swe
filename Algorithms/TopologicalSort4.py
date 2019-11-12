import collections

def topsort(edges, n):
    adj_list = collections.defaultdict(list)
    indegrees = {node:0 for node in range(n)}
    
    for x, y in edges:
        adj_list[x].append(y)
        indegrees[y] += 1
        
    nodes_with_no_indegrees = []
    
    for node, value in indegrees.items():
        if value == 0:
            nodes_with_no_indegrees.append(node)
            
    output = []
    
    while nodes_with_no_indegrees != []:
        current = nodes_with_no_indegrees.pop()
        output.append(current)
        for neighbor in adj_list[current]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                nodes_with_no_indegrees.append(neighbor)
                
    return len(output) == len(adj_list) 

edges = [
        [0, 1],
        [0, 2],
        [0, 3],
        [1, 4],
        [4, 5],
        ]
        
answer = topsort(edges, 6)
print(answer)
