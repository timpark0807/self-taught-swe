class Solution:
    
    def frog(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        
        dp = [False for _ in range(stones[-1]+1)]
        
        for stone in stones:
            dp[stone] = True
        print(dp)
        return self.backtrack(dp, 0, 0)
        

    def backtrack(self, dp, curr_position, curr_jump):
        if curr_position == len(dp)-1:
            return True 
        
        for direction in [-1, 0, 1]:
            move = curr_jump + direction
            if curr_position < curr_position + move < len(dp) and dp[curr_position + move]:
                print(curr_position, move, curr_position + move)
                if self.backtrack(dp, curr_position + move, move):
                    return True
                
        return False

s = Solution()
stones1 = [0,1,2,3,4,5,6,50]
stones = [0,2]
print(s.frog(stones1))
            
