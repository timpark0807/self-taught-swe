class Solution:
    def firstUniqChar(self, s: str) -> int:
        d_dict = {}

        # Create hashtable with number of times each character appears.
        # dict = { character : count } 
        for char in s:
            if char in d_dict:
                d_dict[char] += 1
            else:
                d_dict[char] = 1

        # Iterate through each character of string,
        # If that character appears once, return its index.
        for index, char in enumerate(s):
            if d_dict[char] == 1:
                return index

    
        return -1


    
