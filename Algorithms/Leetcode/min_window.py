def min_window(string, substring):
    low = 0
    current_min = string
    count, freq = get_countfreq(substring)
    
    for high in range(len(string)):
        
        if string[high] in freq:
            if freq[string[high]] > 0:
                count -= 1
            freq[string[high]] -= 1
            
        while count == 0:
            check = string[low:high+1]

            if len(check) < len(current_min):
                current_min = check

            if string[low] in freq:
                
                freq[string[low]] += 1
                
                if freq[string[low]] > 0:
                    count += 1
            low += 1
            
    return current_min

def get_countfreq(substring):
    count = 0
    freq = {}
    for letter in substring:
        count += 1
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1

    return count, freq


if __name__ == '__main__':
    string = 'ADOBECODEBANC'
    substring ='ABC'
    ans = min_window(string, substring)
    print(ans)
