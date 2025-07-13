swaps = input().upper() # get input in upper case
ball_location = 1 # set initially 1
for swap_type in swaps: # if a swap 1st two
    if swap_type == 'A' and ball_location == 1:
        ball_location = 2
    elif swap_type == 'A' and ball_location == 2:
        ball_location = 1
    elif swap_type == 'B' and ball_location == 2: # if b swap last two
        ball_location = 3
    elif swap_type == 'B' and ball_location == 3:
        ball_location = 2
    elif swap_type == 'C' and ball_location == 1: # if c swap 1st and last
       ball_location = 3
    elif swap_type == 'C' and ball_location == 3:
        ball_location = 1
print(ball_location) # print the location