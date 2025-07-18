n = int(input()) # get the no of villages
positions = [] # create a empty list
for i in range(n): # to get each vilages position
    positions.append(int(input())) # append the village position to position
positions.sort() # sort the position
sizes = [] # create empty list to store size of village except for 1st and last index village
for i in range(1, n- 1): #calculate distance  
    left = (positions[i]- positions[i- 1]) / 2
    right = (positions[i + 1]- positions[i]) / 2
    size = left + right
    sizes.append(size) # append all sizes to sizes
min_size = min(sizes) # find the min value
print(min_size) # print the min value