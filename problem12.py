YEAR_COSTS = [12, 10, 7, 5] # each college yeat std cost
for dataset in range(10): # for 10 test case
    trip_cost = int(input()) #  get input for trip cost
    proportions = input().split()
    num_students = int(input()) # input no of std
    for i in range(len(proportions)): # change to float 
        proportions[i] = float(proportions[i])
    students_per_year = []
    for proportion in proportions:
        students = int(num_students * proportion) # find students per year
    students_per_year.append(students) 
    counted = sum(students_per_year) # count the total
    uncounted = num_students- counted # if any missing value 
    most = max(students_per_year) # fing the index of max 
    where = students_per_year.index(most) # add the missing to max value
    students_per_year[where] = students_per_year[where] + uncounted
    total_raised = 0
    for i in range(len(students_per_year)): # for every character
        total_raised = total_raised + students_per_year[i] * YEAR_COSTS[i] # calculate the total amount
    if total_raised / 2 < trip_cost: # if total is less than trip cost
        print('YES')  # print yes
    else:
        print('NO') # or print no