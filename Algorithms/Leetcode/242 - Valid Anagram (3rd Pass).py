def anagram(s, t):

    freq = dict()

    for letter in s:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1

    for letter in t:
        if letter in freq:
            freq[letter] -= 1
            if freq[letter] < 0:
                return False
        else:
            return False

    for value in freq.values():
        if value != 0:
            return False

    return True

s = "anagram"
t = "nagaram"

print(anagram(s,t))
