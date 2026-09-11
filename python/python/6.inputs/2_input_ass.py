# # # # # # # # #name = input("Enter your name: ")

# # # # # # # # #print("Your name is:", name)

# # # # # # # # #city = input("Enter your city: ")

# # # # # # # # #print("Your city is:", city)

# # # # # # # # name = input("Enter your name: ")
# # # # # # # # age = int(input("Enter your age: "))

# # # # # # # # print(f"MY name is {name} and MY age is: {age}")

# # # # # # # age = int(input("Enter your age: "))
# # # # # # # print(age, type(age))

# # # # # # first_name = input("Enter your first name: ")
# # # # # # last_name = input("Enter your last name: ")

# # # # # # print(f"My name is {first_name} {last_name}")

# # # # # name = input("Enter your name: ")
# # # # # city = input("Enter your city: ")
# # # # # college = input("Enter your college name: ")

# # # # # print(f"My name is {name}, I am from {city} and I study in {college}.")

# # # # # a,b = map(int,input("Enter your two numbers:").split())

# # # # # print(f"A = {a}, B = {b}")

# # # # # course ,name  = input("Enter string numbers:").split()

# # # # # print(f"Course = {course}, Name = {name}")


# # # # a,b,c = map(int,input("Enter three numbers:").split())
# # # # print(f"A = {a}, B = {b}, C = {c}")

# # # a = int("25")
# # # print(a, type(a))

# # a = float("25.5")
# # print(a, type(a))


# a = str(100)
# print(a, type(a))

# name = input("Enter your name: ")
# city = input("Enter your city: ")
# print(name)
# print(city)
# print(f"Hello, {name}! You live in {city}.")
# age=input("Enter your age: ")
# print(f"You are {name} and you are {age} years old.")

# #input always returns a string, so if you want to use the age as a number, you need to convert it to an integer or float. For example:

# num=(input("Enter a number: "))
# print(type(num))

# #6
# first_name=input("Enter your first name: ")
# last_name=input("Enter your last name: ")
# print(f"Hello, {first_name} {last_name}!")

# #7
# name=input("Enter your name: ")
# city=input("Enter your city: ")
# college=input("Enter your college: ")
# print(f"Hello, {name}! You live in {city} and you go to {college}.")

# #8
# name1, name2 = input("Enter two names: ").split()
# print(f"Hello, {name1} and {name2}!")

# #9 if the user enters python priogramming then the output will be:
# #Hello, python and programming! where name1=python and name2=programming

# #10
# word1, word2, word3 = input("Enter three words: ").split()
# print(word1)
# print(word2)
# print(word3)

# #11

# number=int(input("Enter a number: "))
# print(type(number))

# #12

# number1=float("25.5")
# print(type(number1))

# #13

# number2=str(100)
# print(type(number2))

# #14

# integer=int(input("Enter an integer: "))
# print(f"You entered the integer: {integer}")
# print(type(integer))

# #15

# float_number=float(input("Enter a float number: "))
# print(f"You entered the float number: {float_number}")
# print(type(float_number))

#16

# a = input("enter any number")
# b = input("enter the second number")


# print(a + b)
#the input function always returns the value in string datatype and thus will concanicate the strings


# #17
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print(a + b)

# #18

# name = "Rahul"
# age = 20
# print=(f"My {name} is Rahul and I am {age} years old.")

# #19
# a = 10
# b = 20
# print(f"the sum of {a} and {b} is {int(a)+int(b)}")

#20

# user_name=input("enter the username:")
# user_age=input("enter the users age:")
# print(f"user name is {user_name} and age is {user_age}")

#21

# price1=23.455
# print(f"{price1:.2f}")

#22 
#:.2f is used to get two values after the decimal point in floating values


#23
# product_name=input("enter product name:")
# price=input("enter the product price:")
# quantity=input("enter the product quantity")

# print(product_name)
# print(price)
# print(quantity)
# print(f"the name of the product is{product_name}and the purchaser bought {quantity} which costs {price} each")

#24
print("A", "B", "C")

#25
print("2026", "08", "19")

#26
print("Hello", end=" ")
print("World")

#27
first_number=int(input("enter the first number"))
second_number=int(input("enter the second number"))

print(f"sum of both the numbers is{first_number+second_number}")

#28
price=input("price of one product")
quantity=input("no. of products purchased")
print(f"total price:{int(price)*int(quantity)}")

#29
name=input("enter the user name")
age=int(input("enter the age of the user"))
marks=input("enter the user age")
print(f"the users age is {int(age)} and marks are {float(marks)}")

#30
#STUDENT INFORMATION:

name= input("Enter name: ")
age= int(input("Enter age: "))
height= float(input("Enter height: "))
city= input("Enter city name: ")
print(f"The student's name is {name}. He is {age} years old. He is {height:.2f} cm tall. He lives in {city}.")