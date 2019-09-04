class Solution:
    def findMaxConsecutiveOnes(self, nums):
        longest = 0
        count = 0

        for num in nums:
            if num == 1:
                count += 1
                if count > longest:
                    longest = count
            else:
                count = 0 

        return longest



s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))




        
