class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d_dict = {}
        
        for i in nums:
            if i in d_dict:
                d_dict[i] += 1
            else:
                d_dict[i] = 1
                
        for i in d_dict.values():
            if i > 1:
                return True
        
        return False
