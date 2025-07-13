p=int(input()) # get the total of more than people have had the disease
n=int(input()) # no of people had disease on day 0
r=int(input()) # the people got disease from the people next day of day 0
total=n # today the affected peoples are n
days=0
while total <= p: # until the total is more than or equal to  p
    n= n * r 
    total += n # adding the total with n
    days+=1 # increasing the days

print(days) # print the no of days



