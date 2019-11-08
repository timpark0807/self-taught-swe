class Solution:
    def numTilePossibilities(self, tiles):
        letters = list(tiles)
        seen = set()
        answers = []
        self.backtrack(letters, seen, answers, [])
        return len(answers)

    def backtrack(self, letters, seen, answers, curr):
        if curr != [] and ''.join(list(curr)) not in answers:
            answers.append(''.join(list(curr)))
            
        for i in range(len(letters)):
            if i not in seen:
                seen.add(i)
                self.backtrack(letters, seen, answers, curr + [letters[i]])
                seen.remove(i)
                
s = Solution()
answer = s.numTilePossibilities("IMSLHTX")
print(answer)
