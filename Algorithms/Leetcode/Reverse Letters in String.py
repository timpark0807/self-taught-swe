import string

def reverse(str_input):
    """
    Reverse Only Alphabet Characters in a String
              
    Input: "abcd-EF-ga"
    Output: "agFE-dc-ba"
                                        time/space
    Complexity:  O(n^2)  ->  O(nlogn)  ->  O(n)  ->  O(logn)  ->  O(1)

    Clarification: 

    1. Input is a string, output is a string
    2. Inplace or out of place?
    3. 2 pointers vs. hash table
    4. if string is "" -> return ""
    5. if len(string) == 1 -> return string

    2 pointer approach
    The low pointer will check if that position of the string is alphabetical
        -> If not alphabetical, we add the non-alphabetical character to the string
        -> Increment low by 1 
    The high pointer will reference the letter we want to add into the output
        -> If high pointer is not alphabetical, decrement high by 1 
    If both low and high pointers are alphabetical
        -> Add letter of high pointer into the index of the low pointer
        -> Increment low by 1
        -> Decrement high by 1

    """

    low, high = 0, len(str_input) - 1
    answer = ""
    
    while low < len(str_input):
        if str_input[low].isalpha() is False:
            answer += str_input[low]
            low += 1
        elif str_input[high].isalpha() is False:
            high -= 1
        else:  # low in alphabet and high in alphabet
            answer += str_input[high]
            low += 1
            high -= 1

    return answer


def reverse_list(string):

    string = list(string)
    low, high = 0, len(string)-1

    while low < high:
        if string[low].isalpha() is False:
            low += 1
        elif string[high].isalpha() is False:
            high -= 1
        else:
            string[low], string[high] = string[high], string[low]
            low += 1
            high -= 1

    return ''.join(string)


if __name__ == '__main__':
    input_1 = "ab-cd-ef"
    input_2 = "abcd-EF-ga"
    answer_1 = reverse_list(input_1)
    answer_2 = reverse_list(input_2)
    print(answer_1)
    print(answer_2)
