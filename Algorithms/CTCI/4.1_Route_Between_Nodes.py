import unittest

def path_bfs(node1, node2, graph):
    queue = [node1]
    visited = [node1]

    while queue:
        current_node = queue.pop(0)
        for child in graph.get(current_node, []):
            if child == node2:
                return True
            
            if child not in visited:
                queue.append(child)
                visited.append(child)
                
    return False

def path_dfs(node1, node2, graph):
    stack = [node1]
    visited = [node1]
    
    while stack:git co
        current_node = stack.pop()
        for child in graph.get(current_node, []):
            if child == node2:
                return True
            if child not in visited:
                stack.append(child)
                stack.append(child)
                
    return False

    

class Test(unittest.TestCase):
     
    def test_bfs(self):
        
        graph = {
            'A':['B', 'C', 'D'],
            'B':['E', 'F'],
            'C':['G'],
            'G':['H'],
            'I':['Z']
        }
        self.assertTrue(path_bfs('A', 'H', graph))
        self.assertTrue(path_bfs('A', 'H', graph))
        self.assertTrue(path_dfs('A', 'H', graph))
        self.assertFalse(path_dfs('A', 'Z', graph))
        self.assertFalse(path_dfs('B', 'G', graph))

if __name__ == '__main__':
    unittest.main()

