class Solution(object):
    def __init__(self):
        self.answer = []
        
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root:
            for child in root.children:
                self.postorder(child)
            self.answer.append(root.val)
            
        return self.answer

    def preorder(self, root):
        """
        :xtype root: Node
        :rtype: List[int]
        """
        if root:
            self.answer.append(root.val)
            for child in root.children:
                self.preorder(child)
        
        return self.answer


    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        queue = [(root, 0)]
        levels = collections.defaultdict(list)
        
        
        while queue:
            current = queue.pop(0)
            current_node = current[0]
            current_depth = current[1]
            
            levels[current_depth].append(current_node.val)
            
            for child in current_node.children:
                queue.append((child, current_depth + 1))
                
        return list(levels.values())
