# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        
        bruteforce
            Time  O(n^2) -> Nested for loops 
            Space O(n) -> return array 
            
            Double for loops 
            
            (2) -> (7) -> (4) -> (3) -> (5)
                                         c 
            
            5
            
    stack = [(7, 1), (4,2),
    
    answers = [7, 0, 4, 5, 0]
               0  1  2  3  4 
        edgecases
        assumptions
            Is this doubly linked ? 
            
        test cases
        toolbox
        
        input/output
            @param1  head : ListNode
            @return  ans  : arr[int]
            
        highlevel
        docstrings
        
        Keep answers array
        Keep stack 
        Iterate over the linked list
            while current node > stack[-1]:
                append current node value to stack
            add the current node to the stack 
            
           (2) -> (7) -> (4) -> (3) -> (5)
                                        c
                                            
    stack = [(7, 1), 
                
    index =  4 

    arr   = [7, 0, 5, 5, 0]
             0  1  2  3  4 
        """
        if not head:
            return [] 
        
        arr = self.get_arr(head)
        
        stack = [] 
        curr = head
        index = 0
        
        while curr:
            while stack and curr.val > stack[-1][0]:
                val, r_index = stack.pop()
                arr[r_index] = curr.val
                
            stack.append((curr.val, index))
            index += 1
            curr = curr.next
            
        return arr 
        
    
    def get_arr(self ,head):
        arr = []
        while head:
            arr.append(0)
            head = head.next
        return arr
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
