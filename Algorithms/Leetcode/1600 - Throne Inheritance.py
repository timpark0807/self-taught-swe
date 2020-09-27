class Node:
    def __init__(self, name):
        self.name = name 
        self.children = [] 
        self.alive = True
        
    def isAlive(self):
        return self.alive 
    
    def kill(self):
        self.alive = False
        return 
    
class ThroneInheritance(object):

    def __init__(self, kingName):
        """
        :type kingName: str
        
        Create a n-ary tree 
        
        nameToNode maps a name to it's node so that we can append children upon births 
        
        """
        self.root = Node(kingName)
        self.nameToNode = {kingName:self.root}

    def birth(self, parentName, childName):
        """
        :type parentName: str
        :type childName: str
        :rtype: None
        """
        childNode = Node(childName) 
        self.nameToNode[childName] = childNode 
        
        parentNode = self.nameToNode[parentName]
        parentNode.children.append(childNode) 
        return 

    def death(self, name):
        """
        :type name: str
        :rtype: None
        """
        personNode = self.nameToNode[name] 
        personNode.kill()
        return 

    def getInheritanceOrder(self):
        """
        :rtype: List[str]
        
        do a preorder dfs 
        
        """
        stack = [self.root] 
        order = [] 
        while stack:
            currNode = stack.pop()
            
            if currNode.isAlive():
                order.append(currNode.name) 
            
            for childNode in currNode.children[::-1]: 
                stack.append(childNode) 
        
        return order
        

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
