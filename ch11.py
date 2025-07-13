password = input() # entering the password
lower =0 # assinging 0 initially
upper=0
digit=0

for p in password: # for every string checking
    if p.islower(): # counting the lower case
        lower=lower+1
    elif p.isupper(): # counting the upper case
        upper=upper+1
    elif p.isdigit(): # counting the digits
        digit += 1

if 8<=len(password)<=12 : # checks the condtion
    if lower >=3 and upper>=2 and digit>=1:
        print("valid") # prints string
    else:
        print("Invalid")
else:
    print("Invalid")