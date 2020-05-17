"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        
        stack = [head] 
        before = None 
        
        while stack:
            curr = stack.pop() 
            
            if before:
                before.next = curr
                curr.prev = before
               
                
            if curr.next:
                stack.append(curr.next)

            if curr.child:
                stack.append(curr.child)
                curr.child = None 
                
            before = curr 
            
        return head 
