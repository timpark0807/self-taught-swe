def min_window(string, substring):

    # Freq represents how many times the letter appears in the substring
    # Count ensures that letters that appear more times in string than in the substring are properly accounted
    count, freq = get_count_freq(substring)
    start = 0
    end = 0
    overall_min = string
    
    for end in range(len(string)):

    # 1. Expanding the window portion

        # If current letter is in frequency table
        # it means the string's current letter appears in the substring
        if string[end] in freq:
            
            # If string's current letter has appeared in the string as many times as it appears in the substring
            # freq[string[end]] will be 0

            # If string's current letter has appeared in the string more than it appears in the substring
            # freq[string[end]] will be negative

            # Only if string's current letter freq is greater than zero(means we needed that letter in the string still)
            # Then we decrement count, otherwise, it's already in the current window 
            if freq[string[end]] > 0:
                count -= 1

            # Actually decrement the freq to show that we have the character
            freq[string[end]] -= 1

        # If count == 0 -> that means current window contains all the letters in the substring
        while count == 0:

            # Check if current window is smaller than overall minimum window
            current_max = string[start:end+1]
            if len(current_max) < len(overall_min):
                overall_min = current_max


    # 2. Shrink the window portion

            # Before we move the start pointer to the right, check if the current start index is a letter of our substring
            if string[start] in freq:

                # If it is, we need to tell the freq dictionary that we need one more of that letter (since we are excluding it from our window)
                freq[string[start]] += 1

                # Only if this makes the freq of that letter over 0, do we increment count
                # If freq was -1, and we move off the letter freq becomes 0.
                #   -> This means there were two of the letters within our window
                if freq[string[start]] > 0:
                    count += 1

            # Move start to the right
            start += 1
            
    return overall_min

def get_count_freq(substring):
    count = 0
    freq = {}

    for letter in substring:
        count += 1
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1

    return count, freq

print(min_window('ADOBECODEBANC', 'ABC'))



            
            






