def mostCommonWord(paragraph, banned):
    word_dict = {}
    clean = clean_paragraph(paragraph)

    # now we have values that are valid in the dictionary
    for word in clean:
        # if word is already in the dictionary, we add 1 to the current value
        if word in word_dict:
            count = word_dict[word]
            word_dict[word] = count + 1
        # if word is not in dictionary, we intialize it with a value of 1 
        else: 
            word_dict[word] = 1

    # find max value
    maximum = 0

    # iterate through the dictionary
    for key in word_dict:
        # if the count value of the word is greater than the current maximum
        if word_dict[key] > maximum and key not in banned:
            # the new maximum is the value of the word
            maximum = word_dict[key]
            # the word is the key
            result = key

    return print(result)
            

def clean_paragraph(paragraph):
    punct = [ "!", "?", "'", ";", ".", ","]
    clean_paragraph = paragraph 
    for char in punct:
        clean_paragraph = clean_paragraph.replace(char, "")

    return clean_paragraph.lower().split(" ")



paragraph = "Bob. hIt, baLl"
banned = ["bob", "hit"]
mostCommonWord(paragraph, banned)
