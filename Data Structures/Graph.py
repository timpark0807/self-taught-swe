import collections

class Graph:
    """
    Class representation of an unweighted, directed graph.

    We initialize this graph with an edge list.
    An adjacency list will be created upon intialization. 
    We assume that all verticies will be integers.

    This object supports the following:
    +------------------+------+-------+
    |   Operation      | Time | Space |
    +------------------+------+-------+
    | Insert Edge      | O(1) |  O(1) |
    | Delete Edge      | O(n) |  O(1) |
    | Traversal - DFS  | O(n) |  O(n) |
    | Traversal - BFS  | O(n) |  O(n) |
    | Topoligcal Sort  | O(n) |  O(n) |
    | Is Cycle?        | O(n) |  O(n) |  
    +------------------+------+-------+
    """
    
    def __init__(self, edges):
        self.adj_list = self._get_adj_list(edges)

    def __str__(self):
        return f'{self.adj_list}'

    def _get_adj_list(self, edges):
        """
        Input  :  arr[arr]
        Output :  dict
        Description:
            - A helper function that is called when the class is initialized.
            - Converts the input edge list to an adjacency list.
        """
        temp_adj_list = collections.defaultdict(list)
        for x, y in edges:
            temp_adj_list[x].append(y)
        return temp_adj_list

    def insert_edge(self, vertex, vertex_insert):
        """
        Input  :  int, int
        Output :  None
        Description:
            - Inserts an edge between an exisiting vertex and a new vertex.
            - Modifies the internal state of the object, does not return a value.
            - Raises an LookupError if 'vertex' does not exist in the graph. 
        """
        if vertex in self.adj_list:
            self.adj_list[vertex].append(vertex_insert)
        else:
            raise LookupError(f'Input vertex ({vertex}) does not exist')

    def delete_edge(self, vertex, vertex_delete):
        """
        Input  :  int, int
        Output :  None
        Description:
            - Removes an edge between 2 existing verticies.
            - Does not return, only modifies the internal state of the object.
            - Raises a LookupError is either inputs do not exist in the graph. 
        """
        if vertex not in self.adj_list:
            raise LookupError(f'Input vertex ({vertex}) does not exist')
        elif vertex_delete not in self.adj_list[vertex]:
            raise LookupError(f'Delete vertex ({vertex_delete}) does not exist')

        index_delete = self.adj_list[vertex].index(vertex_delete)
        del self.adj_list[vertex][index_delete]

    def dfs(self, vertex_start):
        """
        Input  :  int
        Output :  arr

        Description: 
            - Returns the depth first search traversal from the specified start vertex.
            - Uses an array to act as a stack. 
            - Raises a LookupError is the start vertex does not exist in the graph. 
        """
        if vertex_start not in self.adj_list:
            raise LookupError(f'Start vertex ({vertex_start}) does not exist')

        stack = [vertex_start]
        seen = set([vertex_start])
        answer = []
        while stack:
            current = stack.pop()
            answer.append(current)
            for neighbor in self.adj_list[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        return answer 
    
    def bfs(self, vertex_start):
        """
        Input  :  int
        Output :  arr

        Description: 
            - Returns the breadth first search traversal from the specified start vertex.
            - Uses an array to act as a queue. 
            - Raises a LookupError is the start vertex does not exist in the graph. 
        """
        if vertex_start not in self.adj_list:
            raise LookupError(f'Start vertex ({vertex_start}) does not exist')

        queue = collections.deque([vertex_start])
        seen = set([vertex_start])
        answer = []
        while queue:
            current = queue.popleft()
            answer.append(current)
            for neighbor in self.adj_list[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        return answer
    
    def is_path(self, vertex_start, vertex_finish):
        """
        Input  :  int, int 
        Output :  boolean  

        Description:
            - Checks whether there is or is not a path between 2 input verticies.
            - Raises a LookupError is the start vertex does not exist in the graph.
            - If vertex finish does not exsist in the graph, our method will return False
        """
        if vertex_start not in self.adj_list:
            raise LookupError(f'Start vertex ({vertex_start}) does not exist')

        stack = [vertex_start]
        seen = set([vertex_start])
        while stack:
            current = stack.pop()
            if current == vertex_finish:
                return True
            for neighbor in self.adj_list[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        return False 
    
    def get_path(self, vertex_start, vertex_finish):
        """
        Input  :  int, int
        Output :  arr

        Description:
            - Introduces a parent dictionary {child : parent} 
            - Returns the path between 2 input verticies as an array of integers.
            - Returns an empty array if a path does not exist.
            - Raises a LookupError is the start vertex does not exist in the graph.
        """
        queue = [vertex_start]
        seen = set([vertex_start])
        parent = {vertex_start:None}
        while queue:
            current = queue.pop(0)
            if current == vertex_finish:
                temp = []
                while current != None:
                    temp.append(current)
                    current = parent[current]
                return temp[::-1]
            for neighbor in self.adj_list[current]:
                if neighbor not in seen:
                    parent[neighbor] = current
                    seen.add(neighbor)
                    queue.append(neighbor)
        return []
    
    def topological_sort(self, vertex_start):
        """
        Input  :  int
        Output :  arr

        Description:
            - Returns the topological sort from the given start vertex
            - Raises a LookupError is the start vertex does not exist in the graph.
        """
        
        indegrees = self._get_indegrees()
        nodes_with_zero_indegrees = []
        for vertex, count in indegrees.items():
            if count == 0:
                nodes_with_zero_indegrees.append(vertex)
        answer = []
        while nodes_with_zero_indegrees:
            current = nodes_with_zero_indegrees.pop()
            answer.append(current)
            for neighbor in self.adj_list[current]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    nodes_with_zero_indegrees.append(neighbor)
        return answer

    def is_cycle(self, vertex_start):
        """
        Input  :  int
        Output :  boolean

        Description:
            - Returns whether there is or is not a cycle in the graph.
            - Calls the topological sort method.
            - If the number of verticies in the topological sort is equal to
              the number of verticies in the adjacency list, there is no cycle.
              -> Return False if these lengths are equal.
                  - Thus we place the not operator during our return check.
        """
        tmp = self.topological_sort(vertex_start)
        return not len(tmp) == len(self.adj_list)

    def _get_indegrees(self):
        """
        Input  :  None
        Output :  None

        Description:
            - Internal helper function for topological sort.
            - Returns a dictionary with the count of indegrees of each verticies.
        """
        indegrees = {}
        for node, values in self.adj_list.items():
            if node not in indegrees:
                indegrees[node] = 0
            for value in values:
                if value not in indegrees:
                    indegrees[value] = 0
                indegrees[value] += 1
        return indegrees
