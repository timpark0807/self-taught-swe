def min_window(string, substring):

    table = {}

    # Frequency table for substring t 
    for letter in substring:
        if letter in table:
            table[letter] += 1
        else:
            table[letter] = 1

    print(table)

    # Initialize sliding window
    count = len(table)
    begin, end = 0, 0
    
    while end < len(substring):
        if string[end] in table:
            table[end] -= 1    
        end += 1 

min_window('ADOBECODEBANC', 'ABC')
