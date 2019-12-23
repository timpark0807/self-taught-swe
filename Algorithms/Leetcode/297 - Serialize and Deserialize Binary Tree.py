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
            return []
        
        queue = collections.deque([root])
        retval = ''
        while queue:
            curr = queue.popleft()
            
            if curr == 'null':
                retval += curr + ','
                continue
            else:
                retval += str(curr.val) + ','
                
            if curr.left:
                queue.append(curr.left)
            else:
                queue.append('null')
                
            if curr.right:
                queue.append(curr.right)
            else:
                queue.append('null')
                
        return retval[:-1]
    

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        
          0    1    2      3     4       5      6
        "[1,   2,   3,   null,  null,    4,     5]"
          r   r.l  r.r  r.l.l  r.l.r   r.r.l   r.r.r
        
        parent = index//2 
        
        node left = index * 2 + 1
        node right = index * 2 + 2
        
        d = 
            0 : (5)
            1 : (2)
            2 : (3)
            5 : (2)
            6 : (4)
            7 : (3)
            8 : (1)
            

        [5,2,3,null,null,2,4,3,1]
         0 1 2 3    4    5 6 7 8
         
        """
        if not data:
            return None
        data = data.split(',')
        root = TreeNode((int(data[0])))
        queue = collections.deque([root])
        i = 1
        
        while queue and i < len(data):
            node = queue.popleft()
            if data[i] != 'null':
                left = TreeNode(int(data[i]))
                node.left = left 
                queue.append(left)
                
            i += 1
            if data[i] != 'null':
                right = TreeNode(int(data[i]))
                node.right = right
                queue.append(node.right)
            i += 1
        return root 
        
        
        
        
        
        
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
