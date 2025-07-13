# enter the 4 digits of the phone no
num1 = int(input("Enter the first digit of the ph number:"))
num2 = int(input("Enter the second digit of the ph number:"))
num3 = int(input("Enter the third digit of the ph number:"))
num4 = int(input("Enter the fourth digit of the ph number:8"))
# if it stars with 8 or 9 and ends with the no 
# and 2nd and 3rd are same
if ((num1 == 8 or num1 == 9) and (num4 == 8 or num4 == 9) and (num2 == num3)):
    print("ignore the call") # print statement
else:
    print("answer the call") # print string