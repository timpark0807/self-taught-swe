
def sliding_window(string, substring):
    begin = 0
    end = 0
    freq, count = get_count(substring)
    min_substring = ''
    current_substring = '' 

    while end < len(string):
        if string[end] in freq:
            freq[string[end]] -= 1
            count -= 1
        end += 1
        
        while count == 0:
            current_substring = string[begin:end+1]
            
            if min_substring == '':
                min_substring = current_substring
            else:
                if len(current_substring) < len(min_substring):
                    min_substring = current_substring
                    
            if string[begin] in freq:
                freq[string[begin]] += 1
                count += 1

            begin += 1
            

    return min_substring

def get_count(string):
    freq = dict()
    count = 0 
    for letter in string:
        count += 1
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1
    return freq, count     


if __name__ == '__main__':
    string = 'ADOBECODEBANC'
    substring = 'ABC'
    print(sliding_window(string, substring))
