w=int(input()) # weight of pizza
c=int(input()) # cheese content in pizza

if   w== 3 and  c >= 95:
    m="absolutely" 
elif w == 1 and c <= 50:
    m = "fairly"
else:
    m = "very"

print(f"C.C. is {m} satisfied with her pizza.")