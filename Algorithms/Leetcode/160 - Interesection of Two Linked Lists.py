# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        1. Check that there is an intersection
            -> If both linked lists have the same tail node
            
        2. Check length of list A and length of list B

        3. Readjust headA or headB so that they have the same length

        4. Iterate through both lists 1 at a time until they reach an equal node
        
        """
        if headA:   
            headA_length = 1
        else:
            return None
        if headB:
            headB_length = 1
        else:
            return None

        # Step 1 and 2
        currA = headA
        while currA.next not None:
            currA = currA.next
            headA_length += 1

        currB = headB
        while currB.next not None:
            currB = currB.next
            headB_length += 1

        if currA != currB:
            return None

        # Step 3
        diff = headA_length - headB_length
        if diff > 0:
            while diff > 0:
                headA = headA.next
                diff -= 1
        else:
            while diff < 0:
                headB = headB.next
                diff += 1

        # Step 4
        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
                
            
