n= int(input()) # get the number of the dispenser
taken=0 # no of take  
queue=0 # the students in line
while True:
    action=input() # read the action

    if action == "EOF": # stop if the actiom eof is recoganised
        break 
    if action == "TAKE":
        taken+=1
        queue+=1
        n += 1 # move to next number in the machine
        if n > 999: # if 999 numbers completed again start with 1
            n=1
    elif action == "SERVE":
        if queue > 0:
            queue -= 1 # reemove 1 student from line
    elif action == "CLOSE":
        print(taken, queue, n) # print the data
        taken=0 # reset for next day from one
        queue=0
         
