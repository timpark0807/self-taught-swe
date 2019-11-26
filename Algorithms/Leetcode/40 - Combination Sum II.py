class Solution:
    def combinationSum2(self, candidates, target):
        answers = []
        candidates.sort()
        self.dfs(candidates, target, answers, [], 0, 0)
        return answers
    
    
    def dfs(self, candidates, target, answers, curr_arr, curr_sum, start):
        if curr_sum == target:
            answers.append(list(curr_arr))
            return 
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] + curr_sum <= target:
                curr_arr.append(candidates[i])
                self.dfs(candidates, target, answers, curr_arr, curr_sum + candidates[i], i+1)
                del curr_arr[-1]

s= Solution()
answer = s.combinationSum2( [10,1,2,7,6,1,5], 8)
print(answer)
