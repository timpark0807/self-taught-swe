import collections

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    """
    Class representation of a Binary Tree.

    We initialize this binary tree object with a root node.
    Each node will store a value and have a reference to its left and right child. 
    DFS traversals are done iteratively because recursive traversals are trivial.
    
    This object supports the following:
    +----------------+------+-------+
    |   Operation    | Time | Space |
    +----------------+------+-------+
    | Get Root       | O(1) |  O(1) |
    | Search         | O(n) |  O(n) |
    | Insert         | O(n) |  O(n) |
    | Preorder       | O(n) |  O(n) |
    | Postorder      | O(n) |  O(n) |
    | Inorder        | O(n) |  O(n) |
    | Level Order    | O(n) |  O(n) |
    | Get Height     | O(n) |  O(n) |
    | Get Path       | O(n) |  O(n) |
    +----------------+------+-------+
    """
    def __init__(self, root):
        self.root = root

    def get_root(self):
        """
        Input  : None 
        Output : Node

        Description:
            - Follows OOP Encapsulation principle by providing a getter to access root variable.
        """
        return self.root

    def search(self, search_val):
        """
        Input  : int 
        Output : boolean

        Description:
            - Returns True if the value we are searching for exists in the tree.
            - If value does not exist, return False.
        """
        temp = self.preorder()
        return search_val in temp

    def insert(self, new_val):
        """
        Input  : int 
        Output : None

        Description:
            - Inserts a node at the first position available.
            - Method uses BFS to ensure insertion at the minimum depth and left most position.
            - Maintains Binary Tree's balance.
        """     
        queue = collections.deque([self.root])
        while queue:
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            else:
                curr.left = Node(new_val)
                return 
            if curr.right:
                queue.append(curr.right)
            else:
                curr.right = Node(new_val)
                return
        
    def preorder(self):
        """        
        Input  : None 
        Output : arr

        Description:
            - Returns an array of the binary tree's preorder traversal.
            - Root -> Left -> Right
        """
        answer = []
        stack = [self.root]
        while stack:
            curr = stack.pop()
            answer.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return answer

    def postorder(self):
        """        
        Input  : None 
        Output : arr

        Description:
            - Returns an array of the binary tree's postorder traversal.
            - Left -> Right -> Root
        """
        stack = [self.root]
        answer = [] 
        while stack:
            curr = stack.pop()
            answer.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return answer[::-1]

    def inorder(self):
        """        
        Input  : None 
        Output : arr

        Description:
            - Returns an array of the binary tree's inorder traversal.
            - Left -> Root -> Right
        """
        curr = self.root
        stack = []
        answer = [] 
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                answer.append(curr.val)
                curr = curr.right
        return answer

    def levelorder(self):
        """        
        Input  : None 
        Output : arr

        Description:
            - Returns an array of the binary tree's level traversal.
            - Left -> Right
        """
        queue = collections.deque([self.root])
        answer = [] 
        while queue:
            curr = queue.popleft()
            answer.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return answer
    
    def get_height(self):
        """        
        Input  : None 
        Output : int

        Description:
            - Returns the height of the binary tree.
            - Height is defined as the number of edges between the root and the deepest leaf.
        """
        queue = collections.deque([(self.root, 0)])
        max_height = 0
        answer = [] 
        while queue:
            curr, height = queue.popleft()
            max_height = max(max_height, height)
            if curr.left:
                queue.append((curr.left, height+1))
            if curr.right:
                queue.append((curr.right, height+1))
        return max_height

    def get_path(self, end):
        """        
        Input  : int 
        Output : arr

        Description:
            - Returns the path from the root node to the specified end value.
            - If there is no path, return an empty arr.
        """
        parent = {self.root:None}
        queue = collections.deque([self.root])
        answer = [] 
        while queue:
            curr = queue.popleft()
            if curr.val == end:
                while curr:
                    answer.append(curr.val)
                    curr = parent[curr]
                return answer[::-1]
        
            if curr.left:
                parent[curr.left] = curr
                queue.append(curr.left)
            if curr.right:
                parent[curr.right] = curr
                queue.append(curr.right)
        return answer

