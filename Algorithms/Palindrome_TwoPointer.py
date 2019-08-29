def palindrome(s):
    start, end = 0, len(s)-1

    while start < end:
        if s[start] != s[end]:
            return False
        else:
            start += 1
            end -= 1
    return True



if __name__ == '__main__':
    test_1 = palindrome('racecar')
    test_2 = palindrome('raceacar')
    print(test_1 == True)
    print(test_2 == False)
