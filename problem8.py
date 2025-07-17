quarters = int(input()) # get  no of quaters we have
first = int(input()) # no of times 1st machine played
second = int(input()) # no of times 2nd machine played
third = int(input())
plays = 0 # no of slot she played
while quarters >= 1: # if the quaters greater than 1
    machine = plays % 3 # creates the cycle of 0,1,2
    quarters = quarters- 1 # less the 1 quater
    if machine == 0: # when machine 1 works
        first = first + 1
        if first % 35 == 0: # if its divisible by 0 
            quarters = quarters + 30 # give quaters 30 more chances
    elif machine == 1:
        second = second + 1
        if second % 100 == 0: # if its divisible by 100
            quarters = quarters + 60 # give 60 more quaters
    elif machine == 2:
        third = third + 1
        if third % 10 == 0:
            quarters = quarters + 9
    plays = plays + 1 # add the no of times played every time
print('Martha plays', plays, 'times before going broke.')