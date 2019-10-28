import collections
import unittest

def top_sort(edge_list):
    """
    Function that returns a topologically sorted arr
    Input is an edge list

    https://courses.cs.washington.edu/courses/cse326/03wi/lectures/RaoLect20.pdf

    Runtime: O(V + E)

    """

    # Create the adjacency list
    # O(E)
    graph = collections.defaultdict(list)
    
    for x, y in edge_list:
        graph[x].append(y)

    # Create indegrees
    # O(E)  
    indegrees = {}
    
    for x,y in edge_list:
        if x not in indegrees:
            indegrees[x] = 0

        if y not in indegrees:
            indegrees[y] = 1
        else:
            indegrees[y] += 1

    # Intialize a queue with nodes that have no indegrees
    # O(V)
    q_nodes_with_no_indegrees = []
    
    for node, indegree in indegrees.items():
        if indegree == 0:
            q_nodes_with_no_indegrees.append(node)
            
    top = []

    # Iterate through V verticies
    # Dequeue in O(1) time
    # O(V)
    while len(q_nodes_with_no_indegrees) > 0:
        current = q_nodes_with_no_indegrees.pop(0)
        top.append(current)
        
        for neighbor in graph.get(current, []):
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                q_nodes_with_no_indegrees.append(neighbor)

    return top


class Test(unittest.TestCase):
    def test_valid(self):
        edge_list = [
                    [5, 6],
                    [1, 2],
                    [1, 3],
                    [2, 3],
                    [2, 4],
                    [3, 4],
                    [3, 5]
                    ]
        answer = top_sort(edge_list)
        self.assertEqual(answer, [1,2,3,4,5,6])


if __name__ == '__main__':
    unittest.main()
