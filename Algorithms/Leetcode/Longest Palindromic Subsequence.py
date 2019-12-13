class Solution:
    def lpsubsequence(self, string):
        return self.dfs_reg(string, 0, len(string)-1)

    def dfs_reg(self, string, start, end):        
        if start == end:
            return 1
        if start > end:
            return 0
        a, b = 0, 0
        if string[start] == string[end]:
            a = self.dfs_reg(string, start + 1, end-1) + 2
        else:
            b = max(self.dfs_reg(string, start+1, end),
                    self.dfs_reg(string, start, end-1)) 
        return max(a, b)
    
    def lpsubstring(self, string):
        return self.dfs_substring(string, 0, len(string)-1)

    def dfs_substring(self, string, start, end):        
        if start == end:
            return 1
        if start > end:
            return 0
        a, b = 0, 0
        if string[start] == string[end]:
            a = self.dfs_substring(string, start + 1, end-1) + 2
        else:
            b = max(self.dfs_substring(string, start+1, end),
                    self.dfs_substring(string, start, end-1)) 
        return max(a, b)


    def lps_del(self, string):
        return self.dfs(string, 0, len(string)-1)

    def dfs(self, string, left, right):
        if left >= right:
            return 0
        a, b = float('inf'), float('inf')
        if string[left] == string[right]:
            a = self.dfs(string, left+1, right-1)
        else:
            b = min(self.dfs(string, left+1, right),
                    self.dfs(string, left, right-1)) + 1
        return min(a, b)
    
s = Solution()
print(s.lps_del("abdbca"))
print(s.lps_del("cddpd"))
print(s.lps_del("pqr"))
