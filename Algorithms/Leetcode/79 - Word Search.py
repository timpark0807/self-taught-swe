class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """        
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    if self.dfs(board, word, set(), '', row, col, 0):
                        return True
        return False
        
        
    def dfs(self, board, word, seen, curr, row, col, index):
        if curr == word:
            return True
        
        if row < len(board) and row >=0 and col < len(board[row]) and col >= 0:
            if (row, col) not in seen and board[row][col] == word[index]:
                seen.add((row, col))
                if self.dfs(board, word, seen, curr + board[row][col], row+1, col, index+1):
                    return True
                if self.dfs(board, word, seen, curr + board[row][col], row-1, col, index+1):
                    return True
                if self.dfs(board, word, seen, curr + board[row][col], row, col+1, index+1):
                    return True
                if self.dfs(board, word, seen, curr + board[row][col], row, col-1, index+1):
                    return True
                seen.remove((row, col))


s = Solution()
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]

word = "ABCCED"
print(s.exist(board, word))
