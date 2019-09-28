class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0 
        end = 0 
        max_substring = 0
        current_substring = 0 
        s_set = set()
        
        while end < len(s):
            # If our right pointer is not in set, add it to the set and increment right pointer
            
            if s[end] not in s_set:
                s_set.add(s[end])
                end += 1

            else:
                
                # once right pointer is in set, we have a valid substring 
                while s[end] in s_set:
                    
                    # check if current substring length > max substring length
                    current_substring = end - start
                    
                    if current_substring > max_substring:
                        max_substring = current_substring
                    
                    # bring begin pointer to the right by removing from the set and incrementing
                    s_set.remove(s[start])
                    start += 1
            
        return max_substring 


s = Solution()
ans = s.lengthOfLongestSubstring("abcabcbb")
print(ans)
