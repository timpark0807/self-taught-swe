import collections 

class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        left = 0 
        right = 0
        max_subarray = 0
        count = collections.defaultdict(int)
        
        while right < len(tree):
            count[tree[right]] += 1    
            if len(count) > 2:
                max_subarray = max(max_subarray, right - left)
                while len(count) > 2:
                    count[tree[left]] -= 1
                    if count[tree[left]] == 0:
                        del count[tree[left]]
                    left += 1
            right += 1
            
        max_subarray = max(max_subarray, right - left)

        return max_subarray
