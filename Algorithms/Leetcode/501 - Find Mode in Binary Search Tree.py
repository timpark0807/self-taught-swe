class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not root:
            return []
        
        if root.left == None and root.right == None:
            return [root.val]
        
        stack = []
        output = []
        current = root
        
        # Traverse the BST and append all values to output list
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                output.append(current.val)
                current = current.right
        
        # Count number of occurences  
        count = {}
        for num in output:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
    
        # Find Max Value
        max_value = 0
        for value in count.values():
            if value > max_value:
                max_value = value 
        
        # If key == max_value, append to list
        answer = []
        for key, value in count.items():
            if count[key] == max_value:
                answer.append(key)
                
        return answer 
                
