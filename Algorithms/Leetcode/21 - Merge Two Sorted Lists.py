class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return repr(self.val)

class Solution:
    def mergeTwoList(self, l1, l2):
        if l1.val < l2.val:
            l3 = ListNode(l1.val)
            l1 = l1.next 
        elif l2.val < l1.val:
            l3 = ListNode(l2.val)
            l2 = l2.next

        pointer = l3

        while l1 and l2:
            if l1.val < l2.val:
                pointer.next = ListNode(l1.val)
                l1 = l1.next
            elif l2.val < l1.val:
                pointer.next = ListNode(l2.val)
                l2 = l2.next
            pointer = pointer.next

        while l1 is None and l2 is not None:
            pointer.next = ListNode(l2.val)
            l2 = l2.next
            pointer = pointer.next
        while l2 is None and l1 is not None:
            pointer.next = ListNode(l1.val)
            l1 = l1.next
            pointer = pointer.next

        return l3

l1 = ListNode(0)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

print(l1, l1.next, l1.next.next)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(5)
l2.next.next.next = ListNode(7)

print(l2, l2.next, l2.next.next, l2.next.next.next)

s = Solution()
l3 = s.mergeTwoList(l1, l2)
print(l3)
print(l3.next)
print(l3.next.next)
print(l3.next.next.next)
print(l3.next.next.next.next)
print(l3.next.next.next.next.next)
print(l3.next.next.next.next.next.next)
