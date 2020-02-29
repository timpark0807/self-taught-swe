# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None 
        
        heap = [(head.val, head) for head in lists if head]
        heapq.heapify(heap)
        
        dummy = ListNode(-1)
        curr = dummy 
        while heap:
            _, next_node = heapq.heappop(heap)
            curr.next = next_node
            curr = curr.next 
            if next_node.next:
                heapq.heappush(heap, (next_node.next.val, next_node.next))
            
        return dummy.next
         
