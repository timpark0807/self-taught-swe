# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        
        queue = collections.deque([root])
        retval = ''
        
        while queue:
            current = queue.popleft()
            
            if current != 'null':
                retval += str(current.val) + ','
            else:
                retval += 'null' + ','
                continue 
                
            if current.left:
                queue.append(current.left)
            else:
                queue.append('null')
            if current.right:
                queue.append(current.right)
            else:
                queue.append('null')   

        return retval[:-1] 
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        i = 1
        data = data.split(',')
        root = TreeNode(data[0])
        queue = collections.deque([root])

        while queue and i < len(data): 
            curr = queue.popleft()
            
            if curr != 'null':
                left = TreeNode(data[i])
                curr.left = left
                queue.append(left)
            
            i += 1
            
            if curr != 'null':
                right = TreeNode(data[i])
                curr.right = right
                queue.append(right)

        
            i += 1
            
        return root 


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
