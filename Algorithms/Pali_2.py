def pali(s):
    low, high = 0, len(s) - 1

    while low < high:
        if s[low] == s[high]:
            low += 1
            high -= 1
        else:
            return False

    return True


print(pali('xanxnax'))
