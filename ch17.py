initially_obeys=input().upper() # get the input of whom it behaves

no_of_match=int(input()) # no of matches played
matches=[]

for i in range(no_of_match): # getting the input of the winners and lossers of each match
    match=input().strip().split(" ") # split and append the winners and loosers seperately
    matches.append(match)

wizzard=[initially_obeys]
for match in matches:
    winner=match[0] # the first index is winners
    loser=match[1] # the second index is loosers

    if initially_obeys == loser: 
        initially_obeys = winner
        wizzard.append(winner)

print(initially_obeys)
print(len(set(wizzard))) # need to change it to set for avoiding counting the duplicates

