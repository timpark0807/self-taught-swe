
def reverse_words(message):
    
    reverse_characters(message, 0, len(message)-1)
    current_word_start = 0

    for index in range(len(message)+1):
        if index == len(message) or message[index] == ' ':
            reverse_characters(message, current_word_start, index-1)
            current_word_start = index + 1
            
    return message

def reverse_characters(arr, left, right):
    
    while left<right:
        message[left], message[right] = message[right], message[left]
        left += 1
        right -= 1 
    
    return message

message = [ 'c', 'a', 'k', 'e', ' ','p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l' ]
answer = reverse_words(message)
