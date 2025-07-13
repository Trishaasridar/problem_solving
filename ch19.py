n=int(input())  # get inupt of how many questions present
correct=input().upper() # get input of correct answer in uppercase
# gets the pattern no a little higher
adrian = ("ABC" * ((n // 3) + 1))[:n]
bruno = ("BABC" * ((n // 4) + 1))[:n]
goran = ("CCAABB" * ((n // 6) + 1))[:n]
# slicing it equal to the count of n
a=0
b=0 # initially assigning 0 to count the correct answers
g=0

i = 0
while i < n:
    if correct[i] == adrian[i]: # if the answer of a is correct 
        a += 1    # it adds 1 to its count
    if correct[i] == bruno[i]:
        b += 1
    if correct[i] == goran[i]:
        g += 1
    i += 1

maximum = max(a, b, g) # get the max value from the 3 person
print(maximum)

# Print names of the top scorers
if a == maximum:
    print("Adrian")
if b == maximum:
    print("Bruno")
if g == maximum:
    print("Goran")






