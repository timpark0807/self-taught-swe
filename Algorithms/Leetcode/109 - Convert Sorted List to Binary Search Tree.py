# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        
        -10 -> -3 -> 0 -> 5 -> 9
          ^          ^
        
        # Main
        # find mid element
        # make the value of mid the root
        # root.left = mid of left side of list
        # root.right = mid of right side of list
        # return root
        
        # find_mid
        # slow, fast = head, head
        # keep track of prev to split the list in half
        
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        mid = self.get_mid(head)
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root 
    
    def get_mid(self, slow):
        if not slow:
            return None
    
        prev = None
        fast = slow
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        if prev:
            prev.next = None
            
        return slow
            
