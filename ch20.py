words=[]  # assign a empty list
while True:
    word=input() # get input till the word quit
    if word == "quit!":
        break # break the loop
    words.append(word) # append the word


for w in words:
    if len(w) >4 and w[-1]=="r" and w[-2]=="o" : # check if the word if 4 char long and ends with or
        if not w[-3] in "aeiouy": # check whether the vowles present
            w= w[:-2] + "our" # replace or into our
    print(w)

