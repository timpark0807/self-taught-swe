import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        my_dict = collections.defaultdict(list)
        for word in strs:
            key_value = ''.join(sorted(word))
            my_dict[key_value].append(word)
            
            
        return list(my_dict.values())
