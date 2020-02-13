class Solution(object):
    def maxRepOpt1(self, text):
        global_freq = collections.Counter(text)
        if len(global_freq) == 1:
            return len(text)
        
        curr_freq = collections.defaultdict(int)
        left, right = 0, 0
        global_max = 0
        
        while right < len(text):
            right_char = text[right]
            curr_freq[right_char] += 1
            
            while len(curr_freq) == 3 or (len(curr_freq) ==2 and min(curr_freq.values()) == 2):
                max_char = self.get_max_char(curr_freq, right_char)
                if global_freq[max_char] - curr_freq[max_char] > 0:
                    global_max = max(global_max, right - left)
                else:
                    global_max = max(global_max, right - left - 1)
                    
                left_char = text[left]
                curr_freq[left_char] -= 1
                
                if curr_freq[left_char] == 0:
                    del curr_freq[left_char]
                left += 1
                
            right += 1
        
        max_char = self.get_max_char(curr_freq, right_char)
        if global_freq[max_char] - curr_freq[max_char] > 0:
            global_max = max(global_max, right - left)
        else:
            global_max = max(global_max, right - left - 1)

        return global_max
    
    def get_max_char(self, freq, right_char):
        freq[right_char] -= 1
        curr, ans = 0, 0
        for key, value in freq.items():
            if value > curr:
                curr = value
                ans = key
        freq[right_char] += 1
        return ans
        
