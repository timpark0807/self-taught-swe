def rev(string):
    for letter in string:
        last = string.pop()
        string = [last] + string[:]
    return print(string)
        



rev(["h","e","l","l","o"])
