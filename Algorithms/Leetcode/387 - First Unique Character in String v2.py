
def first_unique(string):
    if string == '':
        return -1
    elif len(string) == 1:
        return 0
    
    freq = {}
    for letter in string:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1

    for index, letter in enumerate(string):
        if freq[letter] == 1:
            return index

    return -1



s = "loveleetcode"
ans = first_unique(s)
print(ans)
