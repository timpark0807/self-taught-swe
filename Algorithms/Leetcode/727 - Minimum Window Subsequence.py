class Solution(object):
    def minWindow(self, S, T):        
        left = 0 
        global_min = S + '.'
        
        while left < len(S):
            if S[left] == T[0]:
                valid, sub_string, new = self.is_valid(S, T, left)
                if valid:
                    global_min = min(global_min, sub_string, key=len) 
                    left = new + 1
                    continue
            left += 1
            
        return global_min if global_min != S +'.' else ''
        
    def is_valid(self, S, T, left):
        right = left
        pointer = 0 
        while right < len(S) and pointer < len(T):
            if S[right] == T[pointer]:
                right += 1
                pointer += 1
            else:
                right += 1
                
        if pointer == len(T):
            end = right -1 
            temp = len(T)-1 
            while temp >= 0 and end > left:
                if T[temp] == S[end]:
                    temp -= 1
                    end -= 1
                else:
                    end -= 1
                if temp == -1:
                    end += 1
            return True, S[end:right], right 

        return False, S, -1
    
"""
"cnhczmccqouqadqtmjjzl"
"cm"

"""
S= "cnhczmccqouqadqtmjjzl"
    
T= "cm"
s = Solution()
print(s.minWindow(S, T))

        
