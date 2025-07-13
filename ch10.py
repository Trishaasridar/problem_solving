b1=int(input()) # getting the input in int 
b2=int(input())
b3=int(input())

maximum = max(b1,b2,b3) # finding the max number 
minimum = min(b1,b2,b3) # finding the min number
# prints the mid value
print(b1+b2+b3-maximum-minimum)