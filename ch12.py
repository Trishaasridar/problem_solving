n = input().upper() # get input of string
# searching the format of HONI
target = "HONI"  # setting target to find
index = 0
count = 0  

for c in n:  # cheching each integers one by one
    if c == target[index]: # if the integer matches with the 1st target
        index += 1 # to check next integer
        if index == 4:  # if the index is found completely
            count += 1  # count is added
            index = 0   

print(count)