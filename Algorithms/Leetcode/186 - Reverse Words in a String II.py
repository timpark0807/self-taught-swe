class Solution:
    def reverseWords(self, s):
        """
        Do not return anything, modify s in-place instead.

                                                                            f
['b', 'l', 'u', 'e', ' ', 'i', 's', ' ', 's', 'k', 'y', ' ', 'e', 'h', 't']
                                                               l
                                                                        h        
        """
        s.reverse()
        low = 0 
        fast = 0 
        
        while fast <= len(s):
            if fast == len(s) or s[fast] == ' ':
                high = fast - 1
                while low < high:
                    s[low], s[high] = s[high], s[low]
                    low += 1
                    high -= 1
                low = fast + 1 
            fast += 1
        print(s)

words = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
s = Solution()
s.reverseWords(words)
