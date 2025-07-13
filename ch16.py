n=int(input()) # get the no of times they press the button

char="A" # initially the string is a

for i in range(n):
    word=""
    for c in char: # looping every charcters
        if c == "A": 
            word += "B" # adding to word
        elif c == "B":
            word += "BA"
    char=word

a=char.count("A") # counting the a char
b=char.count("B")
print(a, b)

"""
n = int(input())

a, b = 1, 0  # a = A count, b = B count

for _ in range(n):
    a, b = b, a + b  # A(n) = B(n-1), B(n) = A(n-1) + B(n-1)

print(a, b)
"""