class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        self.memo = {} 
        ans = self.dp(nums1, nums2, 0, 0)
        if ans == 0:
            return self.findSmallest(nums1, nums2)
        return ans 
    
    def findSmallest(self, nums1, nums2):
        globalMin = float('-inf')
        for num1 in nums1:
            for num2 in nums2:
                globalMin = max(globalMin, num1 * num2)
        return globalMin
    
    def dp(self, nums1, nums2, p1, p2):
        if (p1, p2) in self.memo:
            return self.memo[(p1, p2)]
        if p1 == len(nums1) or p2 == len(nums2):
            return 0

        one = self.dp(nums1, nums2, p1+1, p2+1) + (nums1[p1] * nums2[p2])
        two = self.dp(nums1, nums2, p1+1, p2)
        three = self.dp(nums1, nums2, p1, p2+1)            
        self.memo[(p1, p2)] = max(one, two, three)
        return max(one, two, three)
        
