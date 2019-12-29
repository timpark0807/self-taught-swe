def number_of_components(edges, n):
    parents = [-1] * n
    
    def find(x):
        if parents[x] == -1:
            return x
        return find(parents[x])
    
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parents[rootX] = rootY

    for x, y in edges:
        union(x, y)

    return len([1 for n in range(n) if parents[n] == -1])
        

edges = [[0,1],[1,2],[2,3],[4,5],[5,6],[2,6]]
print(number_of_components(edges, 7)) 
