def valid_binary_tree(arr):
    """
    beatiohd



    input
        @param1 arr : arr[set(int)]
        @return ans : bool 
    output

    highlevel
        tuple = (parent, child)

        Iterate through the array
            Create a mapping of
                1. parent : children 
                2. indegrees of all nodes

        Check if all nodes have 0, 1, 2 children
        Check if any nodes have indegrees > 2
        Check if there is a node with 0 parent
        Do a topsort to check if there is a cycle

        return True

        Time  : O(m + n) where m is the length of the arr 
        Space : O(n) where n is the number of nodes 
        
    bruteforce
        -
    edge cases
        - Empty list
    assumptions
        - All entries in arr have len(2) ?
        - Binary Tree
            - All nodes have 0, 1 or 2 children
            - There can be no cycles
            - Every node can have at max 1 parent
            - There needs to be one node with 0 parents
            - 1 root node
            - 1 Connected component 
            
    testcase
    toolbox
    
    """
    adj_list = {}
    indegrees = {}

    for parent, child in arr:
        if parent not in adj_list:
            adj_list[parent] = []
        if child not in adj_list:
            adj_list[child] = []
        if parent not in indegrees:
            indegrees[parent] = 0 
        if child not in indegrees:
            indegrees[child] = 0

        adj_list[parent].append(child)
        indegrees[child] += 1 
        indegrees[parent] += 1

        if len(adj_list[parent]) == 3 or indegrees[child] == 2:
            return False

    root = [node for node, value in indegrees.items() if value == 1]
    
    if len(root) > 1:
        return False
    print(root)
    return not is_cycle(adj_list, indegrees)  

def is_cycle(adj_list, indegrees):

    zero_nodes = [node for node, value in indegrees.items() if value == 1]
    topsort = []
    
    while zero_nodes:
        curr = zero_nodes.pop()
        topsort.append(curr)
        for neighbor in adj_list[curr]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0 :
                zero_nodes.append(curr)
                
    return len(zero_nodes) == len(indegrees)


##arr = [(1,2),(2,3),(3,4)]
##print(valid_binary_tree(arr))
##
##arr = [(1,2), (1,3), (1,4)]
##print(valid_binary_tree(arr))
##
##arr = [{1,2},{2,3},{2,4},{1,5}]
##print(valid_binary_tree(arr))
##
##arr = [{1,2},{2,3},{4,5}]
##print(valid_binary_tree(arr))
##
##arr = [{1,2},{2,1}]
##print(valid_binary_tree(arr))

arr = [{1,2},{2,4},{2,3}]
print(valid_binary_tree(arr))
