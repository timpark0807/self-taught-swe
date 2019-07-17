def commonChars(arr):
    total = set("".join(arr))
    print(total)

    for word in arr:
        for letter in total:
            if letter in word:
                
    

commonChars(["bella","label","roller"])
