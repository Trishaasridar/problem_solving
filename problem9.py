songs = 'ABCDE' #songs contain string of these letters
button = 0 # initialy 0
while button != 4: # until is not equal to 4
    button = int(input()) # get the input to of the 
    presses = int(input())
    for i in range(presses):
        if button == 1: # moves 1st to last
            songs = songs[1:] + songs[0]
        elif button == 2: # moves last to first
            songs = songs[-1] + songs[:-1]
        elif button == 3: # swaps first two
            songs = songs[1] + songs[0] + songs[2:]
output = ''
for song in songs:
    output = output + song + ' '  #gives each song spaces
print(output[:-1]) # prints form 1st to before last leaving space