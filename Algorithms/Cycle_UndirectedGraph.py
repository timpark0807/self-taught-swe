import collections

def detect_cycle(edges, start):
    adj_list = collections.defaultdict(list)
    
    for x, y in edges:
        adj_list[x].append(y)
        adj_list[y].append(x)

    stack = [start]
    parent = {start:None}
    seen = set([start])

    while stack:
        current = stack.pop()

        for neighbor in adj_list[current]:
            if neighbor not in seen:
                seen.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)
                
            elif parent[current] != neighbor:
                return True

    return False


edges = [[0,1], [0,2], [1,2], [2,3]]
print(detect_cycle(edges, 0))

edges = [[0,1], [2, 3], [0,2]]
print(detect_cycle(edges, 0))
