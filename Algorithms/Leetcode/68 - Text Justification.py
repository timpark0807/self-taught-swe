class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        
        words = ["This", "is", "an", "example", "of", "text", "justification."]
                   ^
                   
        lines = []
        line_index = 0
        remain = {0 : 8}
        
        # Step 1: Figure out which words belong in which line 
        
        Iterate over the words -> current word
            Check what line we are at and the current_remain  
            if the current word fits in the current line
                -> Append the current word to the current line
                -> Update current_remain
            else:
                Update remain hashtable 
                    -> curr_line_index : remain + (len(line) - 1)
                reset current_remain to maxWidth
                start a new line -> append [] to lines and line_index += 1
                add the current word to that line and update the current_remain
                
            
        # Step 2: Add spaces to lines
        Iterate over the lines
            Check how many spaces need to be in that line
            Set spaces_first and spaces_rest  
            
            Iterate over the words in that line 
                Add word to temp
                add number of spaces to temp
            Add join temp and add to retval 
                
        return retval 
        
        remain = maxWidth - word_len - (len(line) - 1)         
        """
        if len(words) == 1:
            return [self.get_last_line([words], maxWidth)]
        
        lines, remain = self.get_lines_and_remain(words, maxWidth)
        retval = self.get_text_justification(lines, remain, maxWidth)
        return retval 
    
    
    def get_lines_and_remain(self, words, maxWidth):
        lines = [[]] 
        line_index = 0 
        remain = {}
        curr_remain = maxWidth
        
        for word in words:
            if len(word) <= curr_remain:
                lines[line_index].append(word)
                curr_remain -= (len(word) + 1)
            else:
                remain[line_index] = curr_remain + (len(lines[line_index]))
                curr_remain = maxWidth - (len(word) + 1)
                lines.append([word])
                line_index += 1

        return lines, remain
    
    def get_text_justification(self, lines, remain, maxWidth):
        retval = []
        
        for line_index, line in enumerate(lines[:-1]):
            curr_spaces = self.divide_spaces(line, maxWidth, remain[line_index])
            temp = []
            for index, word in enumerate(line):
                temp.append(word)
                temp.append(curr_spaces[index])
            retval.append(''.join(temp))
        
        retval.append(self.get_last_line(lines, maxWidth))
        
        return retval
                
    def get_last_line(self, lines, maxWidth):
        last_line = lines[-1]
        
        last_line_length = sum([len(word) for word in last_line])
        
        end_padding = maxWidth - last_line_length - len(last_line)
        if end_padding < 0:
            return ' '.join(lines[-1])
        else:
            return ' '.join(lines[-1] + [end_padding * ' '])
            
    
    def divide_spaces(self, line, maxWidth, remain):
        num_of_spaces = max(1, len(line) - 1)
        spaces_per = [' ' * (remain // num_of_spaces)] * num_of_spaces

        total_spaces = 0 
        for space in spaces_per:
            total_spaces += len(space)
            
        if total_spaces < remain:
            for i in range(remain-total_spaces):
                spaces_per[i] += ' '
        
        spaces_per.append('')
        
        return spaces_per 
    
    
    
    
    

s = Solution()
print(s.fullJustify(["Here","is","an","example","of","text","justification."],15))

    
print(s.fullJustify(["Here","is","an","example","of","text","justification."],16))
print(s.fullJustify(["a"],2))

    
    
            
