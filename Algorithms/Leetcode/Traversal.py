class ListNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:

    def inorder(self, root):
        stack = []
        current = root

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.data)
                current = current.right

    def preorder(self, root):
        stack = []
        stack.append(root)
        while stack:
            current = stack.pop()
            print(current.data)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    def postorder(self, root):
        stack = []
        current = root
        stack.append(current)
        while stack:
            if current:
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)
                current = current.left  
            else:
                temp = stack.pop()
                print(temp.data)
                current = temp.right 

    def bfs(self, root):
        queue = [root]
        
        while queue:
            current = queue.pop(0)
            print(current.data)
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)

    def symmetric(self, root):
        current = root
        queue = [current.left, current.right]
        
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            
            if left.left and right.right:
                queue.append(left.left)
                queue.append(right.right)
            elif (not left.left and right.right) or (left.left and not right.right):
                return False
            
            if left.right and right.left:
                queue.append(left.right)
                queue.append(right.left)
            elif (not left.right and right.left) or (left.right and not right.left):
                return False
            
        return True

if __name__ == '__main__':
    root = ListNode(10)
    root.left = ListNode(5)
    root.right = ListNode(15)
    root.left.left = ListNode(2)
    root.left.right = ListNode(6)
    root.right.right = ListNode(20)
    root.right.left = ListNode(11)

    s = Solution()
    
    ans = s.symmetric(root)
    print(ans)

#           (10)
#        /        \
#      (5)        (15)
#     /   \     /     \
#    (2)  (6)  (11)   (20)
#   /     /       \     
#  queue = [, 3, 12
#  left = 1
#  right = 25
#  










