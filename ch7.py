m=int(input()) # get the month
d=int(input()) # get the date in integer

if m < 2:
    print("Before")

elif m == 2 : 
    if d < 18:
        print("Before")
    elif d > 18:
        print("After")
    else :   # if its a feb 18 it is special day
        print("Special")

else :
    print("After")