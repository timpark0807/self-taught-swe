def is_pali(word):
    
    stack = []
    mid = len(word) // 2
    
    for index in range(0, mid):
        stack.append(word[index])
        
    for index2 in range(mid+1, len(word)):
        a = stack.pop()
        if not a == word[index2]:
            return False

    return stack == []

print(is_pali('racecar'))
