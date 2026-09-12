#1 Take three numbers from the user and find the largest number.
# num1=int(input("Enter your first number:"))
# num2=int(input("Enter your second number:"))
# num3=int(input("Enter your third number:"))
# if num1>num2 and num3:
#     print(f"Largest={num1}")
# elif num2>num3 and num1:
#     print(f"Largest={num2}")
# elif num3>num2 and num1:
#     print(f"Largest={num3}")

#2
# Allow withdrawal only when:
#Withdrawal amount is greater than 0
# Withdrawal amount is less than or equal to balance
# Withdrawal amount is a multiple of 100
# Otherwise display an appropriate

# balance=float(input("Enter your bank balance:"))
# withdraw_amount=float(input("Enter the amount you want tom withdraw:"))
# if withdraw_amount>0 and withdraw_amount<=balance and withdraw_amount%100==0:
#     print("The aount will be withdrawed soon:")
# else:
#     print("Withdrawal not possible" )/

#3 Find the second largest number.
# num1=int(input("Enter your first number:"))
# num2=int(input("Enter your second number:"))
# num3=int(input("Enter your third number:"))
# if num2>num1>num3 or num3>num1>num2:
#     print(f"Second largest={num1}")
# if num1>num2>num3 or num3>num2>num1:
#     print(f"Second largest={num2}")
# if num2>num3>num1 or num1>num3>num2:
#     print(f"Second largest={num3}")

#4
# Use a for loop to print numbers from 1 to 50.
# For each number:
# If divisible by 3 → print Fizz
# If divisible by 5 → print Buzz
# If divisible by both → print FizzBuzz
# Otherwise → print the number
# n=int(input("Enter any number:"))
# for n in range(1,n+1,1):
#  
#     if n%3==0:
#         print("Fizz")
#     elif n%5==0:
#         print("Buzz")
#     elif n%3==0 and n%5==0:
#         print("FizzBuzz")
#     else:
#         print(n)

#5 Digital Door Lock and Give the user only 3 attempts using a for loop.
# for attempt in range(3):
#     entered_pin = int(input("Enter your house pin: "))
#     if entered_pin == 2468:
#         print("Door unlocked")
#         break
# else:
#     print("Access denied. 3 attempts used.")