"""
    Initial mistake: mistaking an anagram for a palindrone.

    Can use mergesort to sort the strings and see if they produce an equal result

    This solution counted each letter's occurence in a dictionary and compared the two
"""


class Solution:
    def isAnagram(self, s, t):

        s_dict = {}
        t_dict = {}

        for s_char in s:
            if s_char in s_dict:
                s_dict[s_char] += 1
            else:
                s_dict[s_char] = 1

        for t_char in t:
            if t_char in t_dict:
                t_dict[t_char] += 1
            else:
                t_dict[t_char] = 1        

        return s_dict == t_dict






    
s = Solution()
print(s.isAnagram('anagram', 'nagaram'))
