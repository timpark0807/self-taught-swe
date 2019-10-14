def is_unique(string):
    if type(string) != str:
        return False
 
    string = string.lower()
    
    freq = {}
    for letter in string:
        if letter in freq:
            return False
        else:
            freq[string] = 1

    return True

def is_unique_followup(string):
    """
    Follow up: What if you cannot use additional data structures?
    """
    string = string.lower()

    sorted_string = sorted(string)

    for index in range(1, len(sorted_string)):
        if sorted_string[index] == sorted_string[index-1]:
            return False

    return True

    

string = 'suBway'
ans = is_unique_followup(string)
print(ans)
