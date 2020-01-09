# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        Case 1: Node has 0 children 
        Case 2: Node has 1 child 
        Case 3: Node has 2 children
            -> Reduce Case 3 to Case 1 or 2 by
                1. Swapping target value with left most node of right subtree
                2. Delete left most node of right subtree
        """
        
        if not root:
            return None

        node_to_delete = self.find_node(root, key)
        if node_to_delete == -1:
            return root
        
        dummy = TreeNode(-1)
        dummy.right = root
        self.parents = {root:dummy}

        # Case 1 Node has 0 children 
        if self.node_has_zero_children(node_to_delete):
            if node_to_delete == root:
                return None
            self.delete_this_node(node_to_delete)

        # Case 2 Node has 2 children 
        elif self.node_has_two_children(node_to_delete):
            new_node = self.get_min_of_right_subtree(node_to_delete.right) 
            node_to_delete.val = new_node.val
            self.delete_this_node(new_node)

        # Case 3 Node has left child but no right child
        else:
            self.delete_this_node(node_to_delete)
    
        return root

    def find_node(self, root, key):
        curr = root

        while curr:
            if curr.val == key:
                return curr
            elif curr.val > key:
                self.parents[curr.left] = curr
                curr = curr.left
            else:
                self.parents[curr.right] = curr
                curr = curr.right
        
        return -1 
        
    def delete_this_node(self, node_to_delete):
        # Delete node with zero or two children 
        if self.node_has_zero_children(node_to_delete):
            if self.is_left_child(node_to_delete):
                self.parents[node_to_delete].left = None
            else:
                self.parents[node_to_delete].right = None

        elif node_to_delete.right:
            if self.is_left_child(node_to_delete):
                self.parents[node_to_delete].left = node_to_delete.right
            else:
                self.parents[node_to_delete].right = node_to_delete.right
            
        elif node_to_delete.left:
            if self.is_left_child(node_to_delete):
                self.parents[node_to_delete].left = node_to_delete.left
            else:
                self.parents[node_to_delete].right = node_to_delete.left

            
    def get_min_of_right_subtree(self, node_to_delete):
        if not node.left:
            return node
        self.parents[node.left] = node
        return self.get_min_of_right_subtree(node.left)

    def is_left_child(self, node_to_delete):
        return self.parents[node_to_delete].left = node_to_delete

    def node_has_zero_children(node_to_delete):
        return not node_to_delete.left and not node_to_delete.right
    
    def node_has_two_children(node_to_delete):
        return node_to_delete.left and node_to_delete.right










                
            
