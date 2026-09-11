### level 1

# #1

# number = int(input("enter your number: ").strip())

# if number > 0:
#     print("Positive")
# if number < 0:
#     print("Negative")
# if number == 0:
#     print("Zero") 

# #2

# number = int(input("enter your number: ").strip())

# if number > 0 and number%2 == 1:
#     print("positive Odd")
# if number > 0 and number%2 == 0:
#     print("Positive Even")
# if number < 0 and number%2 == 1:
#     print("Negative Odd")
# if number < 0 and number%2 == 0:
#     print("Negative Even")
# if number == 0:
#     print("Zero") 

# #3

# number1 = int(input("enter your first number: ").strip())
# number2 = int(input("enter your second number: ").strip())

# if number2 > number1 :
#     print(f"The larger number is : {number2}")
# elif number1 > number2 :
#     print(f"The larger number is : {number1}")
# elif number1 == number2:
#     print("Both are equal")
  
# #4

# number1 = int(input("enter your first number: ").strip())
# number2 = int(input("enter your second number: ").strip())
# number3 = int(input("enter your third number: ").strip())

# if number1<number2 and number1<number3 :
#     print(f"The smallest number is: {number1}")
# elif number2<number1 and number2<number3 :
#     print(f"The smallest number is: {number2}")
# elif number3<number1 and number3<number2:
#     print(f"The smallest number is: {number3}")
# else:
#     print("there is no smaller number")

# #5

# number1 = int(input("enter your first number: ").strip())
# number2 = int(input("enter your second number: ").strip())
# number3 = int(input("enter your third number: ").strip())

# if number1>number2 and number1>number3 :
#     print(f"The largest number is: {number1}")
# elif number2>number1 and number2>number3 :
#     print(f"The largest number is: {number2}")
# elif number3>number1 and number3>number2:
#     print(f"The largest number is: {number3}")
# else:
#     print("there is no largest number")

# #6

# number = int(input("enter your number: ").strip())

# if number%5==0 and number%11==0:
#     print("Divisible by both 5 and 11")
# elif number%5==0:
#     print("Divisible only by 5")
# elif number%11==0:
#     print("Divisible only by 11")
# elif number%5!=0 and number%11!=0:
#     print("Divisible by neither")

# #7

# number = int(input("enter your number: ").strip())

# if number%5==3 and number%7==0:
#     print("Divisible by both 3 and 7")
# elif number%3==0:
#     print("Divisible only by 3")
# elif number%7==0:
#     print("Divisible only by 7")
# elif number%3!=0 and number%7!=0:
#     print("Divisible by neither")

# #8

# number = int(input("enter your number: ").strip())

# if number>100:
#     print("Invalid Marks")
# elif number>=40:
#     print("Pass")
# elif number<0:
#     print("Invalid Marks")
# elif number<40:
#     print("Fail")

# #9

# marks = int(input("enter your number: ").strip())

# if marks >= 90 and marks <= 100:
#     print("A")
# elif marks>=80 and marks<=89:
#     print("B")
# elif marks>=70 and marks<=79:
#     print("C")
# elif marks>=60 and marks<=69:
#     print("D")
# elif marks>=40 and marks<=59:
#     print("E")
# elif marks<40:
#     print("Fail")

# #10

# age = int(input("enter your age: ").strip())

# if age<0 :
#     print("Invalid age")
# elif age<18 :
#     print("Cannot vote")
# elif age>=18 and age<=100:
#     print("Can vote")
# else:
#     print("Not Acceptable")

###level 2

# #11

# year = int(input("enter a year : "))


# if year%4==0:
#     print(f"{year} is a Leap year")


# elif year%4!=0:
#     print(f"{year} is a not Leap year")

# #12

# value = input("enter one character: ").strip()

 
# if "A" <= value <= "Z":
#     print("Uppercase alphabet")
# elif "a" <= value <= "z":
#     print("Lowercase alphabet")
# elif str(-9) <= value <= str(9):
#     print("Digit") 
# else:
#     print("Special character")

# #13

# value = input("enter one character: ").lower()

# if value=="a" or value=="e" or value=="i" or value=="o" or value=="u":
#     print("Vowel")
# elif "a" < value <= "z" and value!="a" and value!="e" and value!="i" and value!="o" and value!="u":
#     print("Consonant")
# else:
#     print("Invalid input")

# #14

# Cost_price = int(input("enter cost price of the product: "))
# Selling_price = int(input("enter selling price of the product: "))

# if Cost_price > Selling_price :
#     print("Loss")
# elif Cost_price < Selling_price :
#     print("Profit")
# elif Cost_price == Selling_price :
#     print("No profit and no loss")

# #15

# Cost_Price = int(input("enter cost price of the product: "))
# Selling_Price = int(input("enter selling price of the product: "))

# Profit = (Selling_Price - Cost_Price)
# Loss = (Cost_Price - Selling_Price)

# Profit_Pr = Profit / Cost_Price * 100
# Loss_Pr = Loss / Cost_Price * 100

# if Profit_Pr > Loss_Pr:
#     print(f" profit percentage is {Profit_Pr}")
# elif Profit_Pr < Loss_Pr:
#     print(f" loss percentage is {Loss_Pr}")

# #16


units = float(input("enter units: "))

total=""

if  units <= 100:
    print(units*5)
   
elif 100 < units <= 200 :
    first_total = float(100*5)
    second_total = float((units-100)*7)
    print(first_total+ second_total)

else:
    first_total = float(100*5)
    second_total = float((units-100)*7)
    remaining_total = float((units-200)*10)
    print(first_total + second_total + remaining_total)




# #17

# number1 = int(input("enter your first number: ").strip())
# number2 = int(input("enter your second number: ").strip())
# print("+, -, *, /")
# operator = input("enter operator : ")

# if operator == "/" and number2!= 0:
#     print(number1/number2)

# elif operator == "+":
#     print(number1+number2)

# elif operator == "-":
#     print(number1-number2)

# elif operator == "*":
#     print(number1*number2)

#18

tem = float(input("Enter a temperature in Celsius: "))

if tem <= 0:
    print("Freezing")
elif 0 < tem <= 15:
    print("Very Cold")
elif 16 <= tem <= 25:
    print("Cold")
elif 26 <= tem <= 35:
    print("Normal")
elif tem > 35:
    print("Hot")


