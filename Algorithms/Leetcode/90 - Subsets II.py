class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)

        answers = []
        seen = set()
        self.backtrack(nums, answers, seen, [], 0)
        return answers
    
    
    def backtrack(self, nums, answers, seen, curr, start):        
        if curr not in answers:
            answers.append(list(curr))
        for i in range(start, len(nums)):
            if i not in seen:
                seen.add(i)
                self.backtrack(nums, answers, seen, curr+[nums[i]], i+1)
                seen.remove(i)
        
