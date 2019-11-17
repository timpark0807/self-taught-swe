class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        Vertical Scan

        1. Find Minimum Length Word and iterate that many times over strs
        3. Add current index to set -> If set length > 1; return output
        4. Else, every words current index is the same, add it to output list
        
        """
        if len(strs) == 0:
            return ''
        
        seen = set()
        output = []

        min_word = strs[0]

        for index, word in enumerate(strs):
            min_word = min(word, min_word, key=len)

        for i in range(len(min_word)):
            for word in strs:
                seen.add(word[i])

                if len(seen) > 1:
                    return ''.join(output)
   
            output.append(list(seen)[0])
            seen = set()

        return ''.join(output)

