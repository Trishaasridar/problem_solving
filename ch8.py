sen=input() # get the sentence
happy = sen.count(":-)") # calculate the count of happy faces
sad= sen.count(":-(") # calculate the count of sad faces

if happy == 0 and sad ==0 : # if no happy and sad face in sentence
    print("none")
elif happy>sad:
    print("happy")
elif sad>happy:
    print("sad")
elif happy == sad: # if happy and sad faces are equal
    print("unsure")