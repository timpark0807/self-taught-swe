class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        Input: ["dog","racecar","cat"]
        Output: "fl"
                       0 1 2 3 4
        curr_prefix = 'd o g'
                      0 1 2 3 4
                       ^  
        curr_word =  'racecar'
                      ^
        loop over strs, variable curr_word
            if curr_prefix != curr_word: 
                set 2 pointers on cur_prefix, curr_word
                    0, 0
                while both pointers are both in bound and 2 pointers letters equal:
                    Increment both pointers
                If they are not equal, update curr_prefix
                    curr_prefix = curr_word[:pointer]

        """

        curr_prefix = self.get_shortest_word(strs)

        for curr_word in strs:
            if curr_prefix != curr_word:
                p1, p2 = 0, 0
                while p1 < len(curr_prefix) and p2 < len(curr_word):
                    if curr_prefix[p1] == curr_word[p2]:
                        p1 += 1
                        p2 += 1
                    else:
                        break
                curr_prefix = curr_prefix[:p1]
                
                if curr_prefix == '':
                    return ''
                
        return curr_prefix

    def get_shortest_word(self, strs):
        s = strs[0]
        for word in strs:
            s = min(s, word, key=len)
        return s

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","cat"]))
