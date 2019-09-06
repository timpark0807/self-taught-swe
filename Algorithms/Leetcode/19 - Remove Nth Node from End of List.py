class Solution:
    def removeNthFromEnd(self, head, n):
        """
        My original solution to remove Nth from end.

        Correct:
        1. Identifying the usage of multiple pointers
        2. Using range n to keep a nth pointer n steps ahead of current node
        3. Iterating through linked list, until nth pointer was none
        4. Removing Node by setting prev.next to current.next

        Incorrect:
        This solution passed 187/208 test cases.
        Need to work on edge cases. 
        """
        prev = None 
        current = head
        nth = current
        
        for i in range(n):
            nth = nth.next
            
        while nth is not None:
            prev = current
            current = current.next
            nth = nth.next
        
        if prev == None:                 # Line to pass edge cases
            return None
        if prev == head:                 # Line to pass edge cases
            return head.next
        else:                           
            prev.next = current.next    # If not worried about passing edge cases, just use else.
        return head
        
#          
#       n = 1
#       for i in [0, 1]
#                      
#    nth                       
#    prev
#    current
#    head
#    Node(1)   ->    Node(2)   ->   Node(3)   ->    Node(4)    ->   Node(5)    ->   None
#     1               2               3                4               5 

    def removeNthFromEnd(self, head, n):
        current = head
        dummy = current = ListNode(0) 
        dummy.next  = nth = head
        
        for i in range(n):
            nth = nth.next
            
        while nth is not None:
            current = current.next
            nth = nth.next

        current.next = current.next.next
            
        return dummy.next

#
#          
#    n = 2
#    for i in [0, 1]
#                      
#                                                                                                          
# current                                    
#                                                   nth
# dummy             head
# Node(0)   ->     Node(1)   ->    Node(2)    ->    None
#                    1               2                     





#    n = 2
#    for i in [0, 1, 2]
#                      
#    nth                       
#    current
#    
#    head
#    Node(1)   ->    Node(2)   ->   Node(3)   ->    Node(4)    ->   Node(5)    ->   None
#     1               2               3                4               5 
