class Solution:
    def isAnagram(self, s, t):
        s_dict = {}
        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1

        for letter in t:
            if letter in s_dict:
                s_dict[letter] -= 1
            else:
                return False

        for value in s_dict.values():
            if value != 0:
                return False

        return True




s = 'rat'
t = 'car'
s = Solution()
s.isAnagram(s, t)
