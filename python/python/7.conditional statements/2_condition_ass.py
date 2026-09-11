# #1
# a = input("Enter a number: ")
# a = int(a)

# if a > 10:
#     print("The number is greater than 10.")
# #2
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("adult")
# #3
# number = int(input("Enter a number: "))
# if number >0:
#     print("positive number")

# #4
# marks = int(input("Enter your marks: "))
# if marks >= 40:
#     print("passed")

# number = int(input("Enter a number: "))
# if number==0:
#     print("zero")

# #6
# if number > 0:
#     print("positive number")
# else:
#     print("not positive number")

# #7
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("adult")
# else:
#     print("minor") 

# #8
# number = int(input("Enter a number: "))
# if number%2 == 0:
#     print("even number")
# else:
#     print("odd number")

# #9
# marks = int(input("Enter your marks: "))
# if marks >= 40:
#     print("pass")
# else:
#     print("fail")

# #10
# number=int(input("Enter a number: "))
# number1=int(input("Enter a number: "))
# if number > number1:
#     print(f"{number} is greater than {number1}")
# else:
#     print(f"{number1} is greater than {number}")

# #11
# marks=int(input("enter your marks :"))
# if marks >=90:
#     print("A")
# if marks>=75 and marks<=89:
#      print("B")
# if marks>=60 and marks<=74:
#     print("C")
# if marks>=40 and marks<=59:
#     print("D")
# if marks<=40:
#     print("F")

# #12

# number = int(input("enter your number: "))
# if number>0:
#     print("Positive")
# elif number<0:
#     print("negative")
# elif number==0  :
#     print("zero") 
# else :
#     print("just a number") 

# #13

# print("1_Monday", "2_Tuesday", "3_Wednesday", "4_Thursday", "5_Friday")

# day = input("enter number for a day:").strip().lower()

# if day== "Monday" or day== str(1):
#     print("Monday")
# elif day== "Tuesday" or day== str(2):
#     print("Tuesday")
# elif day== "Wednesday" or day== str(3):
#     print("Wednesday")
# elif day== "Thursday" or day== str(4):
#     print("Thursday")
# elif day== "Friday" or day== str(5):
#     print("Friday")
# else:
#     print("other")

# #14

# marks= int(input("enter your marks: ").strip())

# if marks >= 90:
#     print("Excellent")
# elif marks>=70 and marks<=89:
#     print("Good")
# elif marks>=50 and marks<=69:
#     print("Pass")
# elif marks>=35 and marks<=49:
#     print("Improvement needed")
# elif marks<=34:
#     print("Fail")
# else:
#     print("marks")

# #15

# number = int(input("enter your number: "))

# if number == 1:
#     print("1")
# elif number == 2:
#     print("2")
# elif number == 3:
#     print("3")
# else:
#     print("other")

# #16

# age = int(input("enter your age: ").strip())

# if age >= 18:
#     print("yes")
#     if age <=60:
#         print("Between 18 and 60")

# #17

# marks = int(input("enter your marks: ").strip())

# if marks>=40:
#     print("Passed")
#     if marks>=75:
#         print("Good")
# else:
#     print("Falied")        

# #18

# number = int(input("enter your number: ").strip())

# if number > 0:
#     print("Positive")
#     if number>100:
#         print("The given Number is greather than 100!!")
# else:
#     print("just a number")

# #19

# age = int(input("enter your age: ").strip())

# if age >= 18:
#     print("yes")
#     if age <=60:
#         print("Between 18 and 60")

# #20

# number = int(input("enter your number: ").strip())

# if number!= 0:
#     print("non-zero")
#     if number>0:
#         print("Positive")
#     elif number<0:
#         print("Negative")

# #21

# age = int(input("enter your age: ").strip())

# marks = int(input("enter your marks: ").strip())

# if age >= 18 and marks >= 40:
#     print("Eligible")
# else:
#     print("Not Eligible")

# #22

# number = int(input("enter your number: ").strip())

# if number < 10 or number > 100:
#     print("Special")

# #23

# age=int(input("Enter your age:"))
# has_id=True
# if age>=18 and has_id==True:
#     print("Allowed")

##24

# first_number=int(input("Enter first number"))
# second_number=int(input("Enter second number"))
# if first_number>10 and second_number>10:
#     print("Both are greater than 10")

##25

# first_number=int(input("Enter first number"))
# second_number=int(input("Enter second number"))
# if first_number<0 or second_number>100:
#     print("Both are in range")

##27

# number=int(input("Enter number"))

# if number>10 and number<50:
#     print("The number is between 10-50")

##28

# number=int(input("Enter number"))

# if number>10 or number<50:
#     print("The number is between 10-50")

##29

# is_student = True
# has_id = True
# has_ticket = True


# if is_student and has_id and has_ticket:
#     print("Allowed")

##30

age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
has_id = input("Do you have an ID? (True/False): ") == "True"
if age >= 18 and marks >= 40 and has_id is True:
    print("Eligible")
else:
    print("Not eligible")


