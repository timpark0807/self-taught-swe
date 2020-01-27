def get_shortest_unique_substring(arr, s):

    """
                 r
    ADOBECODEBANC
             l

    counter = 0
    
    freq = {A:0,
            B:0,
            C:0

    """
    freq = {}
    for letter in arr:
        if letter not in freq:
            freq[letter] = 0
        freq[letter] += 1

    left, right = 0, 0
    counter = len(arr)
    global_min = ''
    
    while right < len(s):
        if s[right] in freq:
            freq[s[right]] -= 1
            if freq[s[right]] >= 0:
                counter -= 1

        right += 1

        while counter == 0:
            curr_min = s[left:right]
            if global_min == '':
                global_min = 'z' * 3000
            global_min = min(global_min, curr_min, key=len)

            if s[left] in freq:
                freq[s[left]] += 1
                if freq[s[left]] > 0:
                    counter += 1

            left += 1
    
    return global_min

print(get_shortest_unique_substring('ABC','ADOBECODEBANC'))
