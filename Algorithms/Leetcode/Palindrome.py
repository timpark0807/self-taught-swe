def palindrome(string):
    """
    input: String
    output: Boolean (T/F)

    Edge Cases:
        1. len(string) == 0
        2. len(string) == 1

    Assumptions:
        1. String is immutable data type
        2. Characters are stored in ASCII

    Complexity Reference:

        O(n^2)  ->  O(nlogn)  ->  O(n)  ->  O(logn)  ->  O(1)
                                 time
                                                        space
                    h
                    l   
    string = 'r a c e c a r'
              0 1 2 3 4 5 6 

    len(string) = 7
    
    """

    low = 0
    high = len(string) - 1

    while low < high:
        if string[low] != string[high]:
            return False
        else:
            low += 1
            high -= 1

    return True


ans1 = palindrome('racecar')
ans2 = palindrome('cheese')

print(ans1)
print(ans2)
