class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
    
        # represent the problem as a graph 
        # Being neighbors means the nodes are equal in value
        # iterate over the '==' relationships first to create the graph
        adjList = self.preProcess(equations) 
        
        # map each node to a connected component
        node_to_cc = collections.defaultdict(int) 
        cc = 0
        seen = set() 
        
        for node in adjList.keys():
            if node not in seen:
                self.dfs(node_to_cc, cc, node, adjList, seen)
                cc += 1
            
        # iterate over the '!=' relationships and check if they're in the same connected component 
            # return false 
        for equation in equations:
            node1, node2, symbol = equation[0], equation[-1], equation[1]
            if symbol == '!' and node1 in adjList and node2 in adjList:
                if node_to_cc[node1] == node_to_cc[node2]:
                    return False  
            elif symbol == '!' and node1 == node2:
                return False 
        return True
    
    
    def preProcess(self, equations): 
        adjList = collections.defaultdict(list)
        for equation in equations: 
            if equation[1] != '!':
                adjList[equation[0]].append(equation[-1])
                adjList[equation[-1]].append(equation[0])
        return adjList
    
    def dfs(self, node_to_cc, cc, node, adjList, seen):
    
        stack = [node]
        seen.add(node) 
        
        while stack:
            currNode = stack.pop()
            node_to_cc[currNode] = cc
            
            for neighbor in adjList[currNode]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        return 
    
        
        
        
        
        
        
        
        
        
        
        
        
