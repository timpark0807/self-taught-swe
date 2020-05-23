class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        counts = collections.defaultdict(int) 
        
        for letter in s:
            counts[letter] += 1
            
        arr = [list() for _ in range((max(counts.values()) +1))]
        for letter, count in counts.items():
            arr[count].append(letter*count)
        retval = []
        for letters in reversed(arr):
            if letters:
                retval.append(''.join(letters))
        return ''.join(retval)
