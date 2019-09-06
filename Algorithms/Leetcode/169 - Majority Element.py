class Solution:
    def majorityElement(self, nums) -> int:
        
        majority = len(nums) // 2

        answer_dict = {}

        for num in nums:
            if num in answer_dict:
                answer_dict[num] += 1
            else:
                answer_dict[num] = 1

        for key, item in answer_dict.items():
            if item > majority:
                return key


s = Solution()
print(s.majorityElement([2,2,1,1,1,2,2]))
