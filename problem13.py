for dataset in range(10): # for 10 test case
    lst = input().split() # get two inputs 
    franchisees = int(lst[0]) # 1st is for no of franchisees
    days = int(lst[1]) # 2nd for no of days and change both to integer
    grid = [] # assign a empty grid
    for i in range(days): # loop for the no of days
        row = input().split() # enter the sales for each feanchisees
        for j in range(franchisees): # loop the rows 
            row[j] = int(row[j]) # change each element in row to int
        grid.append(row) # append the row list to grid
    bonuses = 0 
    for row in grid: # to loop the rows
        total = sum(row)   # get the sum of  each rows
        if total % 13 == 0: # check the conditon
            bonuses = bonuses + total // 13 # udate the bonus
    for col_index in range(franchisees): # to calculate bonus in column wise
        total = 0 
        for row_index in range(days): # loop till the days 
            total = total + grid[row_index][col_index] # total it according to index
            if total % 13 == 0: # check the condition
                bonuses = bonuses + total // 13 # update the bonus
    print(bonuses) # print the bonus