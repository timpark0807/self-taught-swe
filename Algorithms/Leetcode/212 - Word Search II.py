class Trie:
    def __init__(self):
        self.root = {}

    def build_trie(self, words):
        for word in words:
            self._insert(word)
            
    def _insert(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr:
                curr[letter] = {} 
            curr = curr[letter]
        curr['-'] = word
                        
    def get_root_dict(self):
        return self.root
    
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not words:
            return []
        
        trie = Trie()
        trie.build_trie(words)
            
        answers = [] 
        self.moves = [(0,1),(0,-1),(1,0),(-1,0)]

        base_letters = trie.get_root_dict()
        for row in range(len(board)):
            for col in range(len(board[row])):
                temp = [] 
                if board[row][col] in base_letters:
                    self.search(board, base_letters[board[row][col]], set([(row, col)]), temp, row, col)
                    answers.extend(temp)                 
        return answers
    
    
    def search(self, board, curr, seen, temp, row, col):
        if '-' in curr:
            temp.append(curr['-'])
            del curr['-']
            return 
        for move in self.moves:
            new_row, new_col = row + move[0], col + move[1]
            
            if self.is_valid(board, curr, new_row, new_col, seen):
                seen.add((new_row, new_col))
                self.search(board, curr[board[new_row][new_col]], seen, temp, new_row, new_col)
                seen.remove((new_row, new_col))
        
    
    
    def is_valid(self, board, curr, row, col, seen):
        return 0 <= row < len(board) and 0 <= col < len(board[row]) and (row, col) not in seen and board[row][col] in curr


s = Solution()

board = [["a","a","a","a"],
         ["a","a","a","a"],
         ["a","a","a","a"],
         ["a","a","a","a"],
         ["b","c","d","e"],
         ["f","g","h","i"],
         ["j","k","l","m"],
         ["n","o","p","q"],
         ["r","s","t","u"],
         ["v","w","x","y"],
         ["z","z","z","z"]]

words = ["aaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaab","aaaaaaaaaaaaaaac","aaaaaaaaaaaaaaad",
         "aaaaaaaaaaaaaaae","aaaaaaaaaaaaaaaf","aaaaaaaaaaaaaaag","aaaaaaaaaaaaaaah",
         "aaaaaaaaaaaaaaai","aaaaaaaaaaaaaaaj","aaaaaaaaaaaaaaak","aaaaaaaaaaaaaaal",
         "aaaaaaaaaaaaaaam","aaaaaaaaaaaaaaan","aaaaaaaaaaaaaaao","aaaaaaaaaaaaaaap",
         "aaaaaaaaaaaaaaaq","aaaaaaaaaaaaaaar","aaaaaaaaaaaaaaas","aaaaaaaaaaaaaaat",
         "aaaaaaaaaaaaaaau","aaaaaaaaaaaaaaav","aaaaaaaaaaaaaaaw","aaaaaaaaaaaaaaax",
         "aaaaaaaaaaaaaaay","aaaaaaaaaaaaaaaz","aaaaaaaaaaaaaaba","aaaaaaaaaaaaaabb",
         "aaaaaaaaaaaaaabc","aaaaaaaaaaaaaabd","aaaaaaaaaaaaaabe","aaaaaaaaaaaaaabf",
         "aaaaaaaaaaaaaabg","aaaaaaaaaaaaaabh","aaaaaaaaaaaaaabi","aaaaaaaaaaaaaabj",
         "aaaaaaaaaaaaaabk","aaaaaaaaaaaaaabl","aaaaaaaaaaaaaabm","aaaaaaaaaaaaaabn",
         "aaaaaaaaaaaaaabo","aaaaaaaaaaaaaabp","aaaaaaaaaaaaaabq","aaaaaaaaaaaaaabr",
         "aaaaaaaaaaaaaabs","aaaaaaaaaaaaaabt","aaaaaaaaaaaaaabu","aaaaaaaaaaaaaabv",
         "aaaaaaaaaaaaaabw","aaaaaaaaaaaaaabx","aaaaaaaaaaaaaaby","aaaaaaaaaaaaaabz","aaaaaaaaaa"]

print(s.findWords(board, words))
print(s.findWords([['a']], ['a']))
