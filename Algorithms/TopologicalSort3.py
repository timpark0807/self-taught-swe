import collections
import unittest

def top_sort(edges):
    # Create hashmaps of adjaceny and number of indegrees
    adj_list = collections.defaultdict(list)
    indegrees = {}
    
    for x, y in edges:
        adj_list[x].append(y)
        
        if x not in indegrees:
            indegrees[x] = 0

        if y not in indegrees:
            indegrees[y] = 1
        elif y in indegrees:
            indegrees[y] += 1

    # Find nodes with no indegrees, to start our search
    nodes_with_no_indegrees = []
    
    for node, indegree in indegrees.items():
        if indegree == 0:
            nodes_with_no_indegrees.append(node)

    top = []

    # When nodes have no indegrees, visit their neighbors,
    # Decrement the neighbor by 1
    # If neighbor now has no indegrees, add it to the queue
    while len(nodes_with_no_indegrees) > 0:
        current = nodes_with_no_indegrees.pop(0)
        top.append(current)
        for neighbor in adj_list[current]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                nodes_with_no_indegrees.append(neighbor)
                
    return len(top) == len(adj_list)

"""
#
#   (3)   ->  (4)
#    ^------   |
#           |  v
#   (1)   ->  (2)  
#
#
      adj_list = { 1: [2],
                   2: [3]
                   3: [4],
                   4: [2]   }

    # indegrees = { 1: 0,
                    2: 1,
                    3: 1,
                    4: 1  }
 
    # nodes_with_no_indegrees = [
    # current = 1
    # adj_list[current] = [2]
    # neighbor = 2

    # output = [1,
"""

class Test(unittest.TestCase):
    def test_cycle(self):
        edges = [
                 [1,2],
                 [2,3],
                 [3,4],
                 [4,2],
                 ]
        answer = top_sort(edges)
        self.assertFalse(answer)
    def test_no_cycle(self):
        edges = [
                 [1,2],
                 [2,3],
                 [3,4]
                 ]
        answer = top_sort(edges)
        self.assertTrue(answer)

if __name__ == '__main__':
    unittest.main()
