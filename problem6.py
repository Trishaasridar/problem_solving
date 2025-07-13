n = int(input()) # get the input no of parking space
yesterday = input().upper() # enter yesterday utilised space
today = input().upper() # enter today utilised space
occupied = 0
for i in range(len(yesterday)):
    if yesterday[i] == 'C' and today[i] == 'C': # check if yesterday and today they use same spots
        occupied = occupied + 1
    
print(occupied) # print no of spaces occupied