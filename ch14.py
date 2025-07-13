n = int(input()) # get no of subjects

stud = []  # get the all students ans
for u in range(n): 
    stud.append(input().upper()) # append the student answers
ans = []
for r in range(n):
    ans.append(input().upper())

count = 0
for i in range(n):
    if stud[i] == ans[i]: # check if the stud and teachers ans match
        count += 1

print(count) # print the no of crt ans
