def rec_reverse_string(s):
    if len(s) == 0:
        return ''
    return s[-1] + rec_reverse(s[:len(s)-1])

def rec_list_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[-1] + rec_list_sum(arr[:len(arr)-1])

def rec_palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False
    return rec_palindrome(s[1:len(s)-1])

def rec_print_list_backwards(arr):
    if len(arr) == 0:
        return
    rec_print_list_backwards(arr[1:])
    print(arr[0])
    
def rec_reverse_list(arr):
    answer = []
    return helper(arr, answer)

def helper(arr, answer):
    if len(arr) == 0:
        return None
    helper(arr[1:], answer)
    answer.append(arr[0])
    return answer


arr = [1, 2, 3, 4, 5]
s = 'hello'
print(rec_reverse_string(s))
print(rec_list_sum(arr))
rec_print_list_backwards(arr)
print(rec_reverse_list(arr))
print(rec_palindrome('racecar'))
print(rec_palindrome('hello'))

