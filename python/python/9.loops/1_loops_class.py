##1

# for i in range(1,10):
#     print(i, end=(" "))


##2

# for i in range(1,20):
#     if i%2==0:
#         print(f"{i} is even!!") 

##3

# for leap_year in range(2000, 2030):
#     if leap_year%4==0:
#         print(f"{leap_year} is leap year")

# #4

# start= int(input("enter a starting number: "))
# end= int(input("enter a ending number: "))

# for i in range(start,end):
#     if i%2==0:
#         print(f"{i} is even!!")

# #5

# total = 0

# for i in range(1,11):
#     total= total + i
#     print(total)

# #6




# string=input("enter a string: ").strip().lower()

# string2 = ""


# length = len(string)

# for element in range (length-1,-1,-1):

#     string2 = string2 + string[element]

# if string == string2:
#     print("string is palindrom")

# else :
#     print("string is not palindrom")


# # 7

# total = 0

# for i in range(1, 6):
#     total = total + i

# print(total)

# #8 method 

# name = "Aeish"

# for character in name:
#     print(character)

# #9 tradition method

# name = "Aeish"

# length = len(name)

# for element in range (0,length):
#     print(name[element])

# #10

# word = "banana"

# count = 0

# for character in word:
#     if character == "a":
#         count = count + 1

# print("Count:", count)

# #11


# word = "banana"

# length = len(word)

# count = 0

# for character in range (0,length):

#     i = word[character]

#     if i == "a":
#         count = count + 1

# print("Count:", count)


# #12

# i = 0
# j = 0

# for i in range(3):
#     i = i + 0
#     for j in range(2):
#         j = j + 0

# print(i, j)

# #13

# for row in range(4):
#     for column in range(5):
#         print("*", end=" ")
#     print()

#14

for row in range(1,11):
    for column in range(1, row+1):
       print("*", end=" ")
    print()
            

