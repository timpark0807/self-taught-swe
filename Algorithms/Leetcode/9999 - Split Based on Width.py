def solve(text, width):

    textArr = text.split()
    output = [] 
    curr = []
    remain = width
    
    for word in textArr:
        if len(word) <= remain:
            curr.append(word)
            remain -= len(word)
            if remain == 0:
                remain = width
                output.append(curr) 
                curr = []
        else:
            curr.append(word[:remain-1])
            curr.append('-')
            output.append(curr) 
            curr = []
            remain = width
            curr.append(word[remain-1:])
            remain -= len(word[remain-1:])

    output.append(curr)
    answer = ''
    for chunk in output:
        print(chunk)
    return answer

print(solve('timm said hello', 4) )
            
"""
"tim said hello world"
column = 4

['timy', 'said', 'hello', 'world']
                    ^  

h e l l o
0 1 2 3 4

outpuit = [[timy],[hel-]

length = 2
curr = ['lo


2nd iteration
length = 4
curr = ['said



curr = [hel-]

curr = [o, ' ', 'wo-']

curr [rld] 

split the string based on the spaces


iterate over the words
    if the length of current word is less than current space remaining
        add word to curr
        remove length of curr word from curr space remaining
        
    if the length of the current word is greater than current space remaining
        add as much as we can to curr with a hypen
        reinit curr = [] and add the remainder of the word as the first part        
        reinit length 

"""
