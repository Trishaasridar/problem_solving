n=int(input()) #get no  of lines to be entered
full=""
for inputs in range(n):
    line=input().lower()
    full = full +line # get all three lines in a one line
    
s=full.count("s") #count no of s characters in it
t=full.count("t") 

if s<t:
    print("English")
else:
    print("French")


