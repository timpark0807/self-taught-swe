class Solution:
    def containsDuplicate(self, nums):
        d_dict = {}
        for num in nums:
            if num in d_dict:
                d_dict[num] += 1
            else:
                d_dict[num] = 1

        for values in d_dict.values():
            if values > 1:
                return True

        return False
