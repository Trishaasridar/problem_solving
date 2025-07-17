sentence = input() # get the sentence
result = '' # give the empty string
i = 0
while i < len(sentence): # executes until the len of sentence
    result = result + sentence[i] # ads the index to the already prepared string
    if sentence[i] in 'aeiou': # checks whather the index is vowels 
        i = i + 3 # adds 3 to index to romove the unwanted pattern
    else:
        i = i + 1 # goes to the next string
print(result) # prints the decoded string