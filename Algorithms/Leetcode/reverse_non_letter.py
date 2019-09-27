

            
s = "abcd-EF-ga"
      
         

def reverse_alph(s):
    low = 0 
    high = len(s) - 1
    output = ''
    
    while low < len(s):
        
        if s[high].isalpha() is False:
            high -= 1

        elif s[low].isalpha() and s[high].isalpha():
            output += s[high]
            high -= 1
            low += 1
            
        elif s[low].isalpha() is False:
            output += s[low]
            low += 1

    return output

print(reverse_alph(s))
