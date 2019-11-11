class Solution(object):
    
    def subsetsWithDup(self, nums):
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
        

    def subsets(self, nums):
        answer = []
        self.backtrack(nums, answer, [], 0)
        return answer
    
    def backtrack(self, nums, answer, subset, i):
        answer.append(list(subset))
        
        for index in range(i, len(nums)):
            subset.append(nums[index])
            self.backtrack(nums, answer, subset, index+1)
            subset.pop()



            
            
            
