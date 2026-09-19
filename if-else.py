#Take three numbers from the user: num1, num2, and num3.

#Determine whether they form:

#An increasing sequence → num1 < num2 < num3
#A decreasing sequence → num1 > num2 > num3
#All three numbers are equal
#Two numbers are equal
#No specific pattern

#Print the appropriate message.


num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

if num1 == num2 and num2 == num3:
    print("All three numbers are equal")

elif num1 < num2 and num2 < num3:
    print("Increasing sequence")

elif num1 > num2 and num2 > num3:
    print("Decreasing sequence")

elif num1 == num2 or num2 == num3 or num1 == num3:
    print("Two numbers are equal")

else:
    print("No specific pattern")