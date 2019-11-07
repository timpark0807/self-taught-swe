class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        seen = set()
        answer = []
        self.backtrack(nums, seen, [], answer)
        return answer

    def backtrack(self, nums, seen, subset, answer):
        if len(nums) == len(subset):
            answer.append(subset[:])
            return

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                self.backtrack(nums, seen, subset + [nums[i]], answer)
                seen.remove(nums[i])


s=Solution()
answer = s.permute([1,2,3])
print(answer)
