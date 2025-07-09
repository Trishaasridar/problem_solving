b=int(input()) # input of burger 
side=int(input()) # input of side dish 
drink=int(input()) # input of drink
dessert=int(input()) # input of dessert
total=0 # initiate total is 0
if b==1 :
    total = total + 461 
elif b==2:
    total = total + 431
elif b==3:
    total = total + 420   
elif b==4:
    total = total + 0

if drink==1 :
    total = total + 130
elif drink==2 :
    total = total + 160
elif drink==3 :
    total = total + 118
else:
    total = total + 0

if side==1 :
    total = total + 100
elif side ==2:
    total = total + 57
elif side ==3:
    total = total + 70
else:
    total = total + 0

if dessert ==1:
    total = total+ 167
elif dessert==2:
    total = total+ 266
elif dessert==3:
    total = total+ 75
else:
    total = total+ 0

print(f"Your total Calorie count is {total}.")