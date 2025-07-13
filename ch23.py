n = int(input()) # get the no of lines

for _ in range(n): # for each line
    line = input().strip() # get the sequence of string
    lists = [] # create a empty list
    count = 1 # initially count to 1
    for i in range(1, len(line)): # loop from second character
        if line[i] == line[i - 1]: # check same as previous character or not
            count += 1 # add the count
        else:
            lists.append(str(count) + " " + line[i - 1]) # apprnd to list
            count = 1 # reset the count
    lists.append(str(count) + " " + line[-1]) #print the last sequence
    print(" ".join(lists)) # join the list as string
