# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

class Solution:
    def reverseList(self, head):
        head = head
        prev = None
        while head is not None:
            pointer = head
            head = head.next
            pointer.next = prev
            prev = pointer

        return prev
            
