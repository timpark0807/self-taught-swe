import unittest


class Solution:
    def build_order(self, projects, dependencies):
        """
        graph = {
                 'a' : ['d'],
                 'b' : ['d'],
                 'c' : []
                 'd' : ['c'],
                 'e' : [],
                 'f' : ['b', 'a']
                 }
        """
        # Returns the graph above.
        graph = self.build_graph(projects, dependencies)

        independent_projects = self.get_independent_projects(projects, dependencies)
        # returns an array -> [e, f]

        # Choose a project to start with from independent projects
        # Check if this project will have a path.
        # We can return if the len of output is length of projects
        # AKA we did every project once

        # O(Z * (V + E))
        # Where Z is independent projects
        # V is verticies 
        
        for project in independent_projects:
            node1 = project
            output = independent_projects

            queue = [node1]
            seen = set(node1)
            
            while queue:
                current = queue.pop(0)
                if current != project:
                    output.append(current)
                
                for child in graph.get(current, []):
                    if child not in seen:
                        seen.add(child)
                        queue.append(child)

            if len(output) == len(projects):
                return output
            
        return 'Error'

    def get_independent_projects(self, projects, dependencies):
        # Time: O(D + V)
        
        # A project with no dependencies with not be found in any of the [1] position in dependencies
        projects_with_dependency = set()
        
        for dependency in dependencies:
            projects_with_dependency.add(dependency[1])

        projects_with_no_dependency = []
        
        for project in projects:
            if project not in projects_with_dependency:
                projects_with_no_dependency.append(project)

        return projects_with_no_dependency
            

    def build_graph(self, projects, dependencies):
        # Time: O(V + D)
        # V is verticies
        # D is dependencies
        
        graph = dict()
        
        for project in projects:
            graph[project] = []

        for dependency in dependencies:
            graph[dependency[0]].append(dependency[1])

        return graph


class TestSolution(unittest.TestCase):
    def test_buildorder(self):
        s = Solution()
        projects = ['a', 'b', 'c', 'd', 'e', 'f']
        dependencies = [('a','d'), ('f','b'), ('b','d'), ('f','a'), ('d','c')]
        answer = s.build_order(projects, dependencies)
        self.assertEqual(answer, ['e', 'f', 'b', 'a', 'd', 'c'])


if __name__ == '__main__':
    unittest.main()
    
