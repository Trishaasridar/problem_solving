apple_three = int(input("Enter the number of successful three-point shots for the Apples:"))
apple_two = int(input("Enter  the number of successful two-point shots for the Apples:"))
apple_one = int(input("Enter  the number of successful one-point shots for the Apples:"))
banana_three = int(input("Enter the number of successful three-point shots for the Banana:"))
banana_two = int(input("Enter  the number of successful two-point shots for the Banana:"))
banana_one = int(input("Enter  the number of successful one-point shots for the Banana:"))

apple_total = apple_three * 3 + apple_two * 2 + apple_one
banana_total = banana_three * 3 + banana_two * 2 + banana_one

if apple_total > banana_total:
    print("A\n Apple win!")
elif banana_total > apple_total:
    print("B\n Banana Win!")
else:
    print("T\n Tie!")