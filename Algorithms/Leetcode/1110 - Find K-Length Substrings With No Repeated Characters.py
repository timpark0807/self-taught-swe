import collections

def numKLenSubstrNoRepeats(S, K):
    freq = collections.defaultdict(int)
    count = 0
    left, right = 0, 0

    while right < len(S):
        freq[S[right]] += 1

        while freq[S[right]] == 2:
            freq[S[left]] -= 1
            left += 1

        if right - left + 1 == K:
            count += 1
            freq[S[left]] -= 1
            left += 1

        right += 1
        
    return count 



word = 'racecar'
K = 3
print(numKLenSubstrNoRepeats(word, K))





