## 1. Print a 3×3 Star Grid
# Write a Python program to print:

# * * *
# * * *
# * * *
# Hint
# Use one loop for 3 rows.
# Use another loop for 3 stars in each row.

for i in range(0,3):
    for j in range(0,3):
        print("*", end=" ")
    print()

# # 2. Print Numbers in Rows
# Write a Python program to print:

# 1 2 3
# 1 2 3
# 1 2 3
# Hint
# Outer loop controls the 3 rows.
# Inner loop should print numbers from 1 to 3.

for i in range(1,4):
    for j in range(1,4):
        print(j, end=" ")
    print()

# # 3. Print Row Numbers
# Write a Python program to print:

# 1 1 1
# 2 2 2
# 3 3 3
# Hint
# Outer loop should represent the row number.
# Inner loop should repeat the current row number 3 times.

for i in range(1,4):
    for j in range(1,4):
        print(i, end=" ")
    print()


# # 4. Increasing Star Pattern
# Write a Python program to print:

# *
# * *
# * * *
# * * * *
# * * * * *
# Hint
# Outer loop runs from 1 to 5.
# Number of stars in each row depends on the current row number.

for i in range(0,6):
    for j in range(0,i+1):
        print("*", end=" ")
    print()


# # 5. Decreasing Star Pattern
# Write a Python program to print:

# * * * * *
# * * * *
# * * *
# * *
# *
# Hint
# Start with 5 stars.
# Reduce the number of stars by 1 after every row.

for i in range(6,0,-1):
    for j in range(i-1,-1,-1):
        print("*", end=" ")
    print()


# # 6. Increasing Number Pattern
# Write a Python program to print:

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# Hint
# Outer loop represents the row.
# Inner loop starts from 1 and ends at the current row number.

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

# # 7. Repeated Number Pattern
# Write a Python program to print:

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# Hint
# The outer loop gives the number to print.
# The inner loop repeats that number according to the row number.

for i in range(1,6):
        for j in range(1,i+1):
        print(i, end=" ")
    print()

# # 8. Multiplication Tables from 1 to 5
# Write a Python program to print multiplication tables from 1 to 5.

# Each table should contain multiplication from 1 to 10.

# Hint
# Outer loop selects the table number.
# Inner loop runs from 1 to 10.
# Multiply the outer-loop number by the inner-loop number.


for i in range(1,6):
    for j in range(1,11):
        print(i*j,end=" ")
    print()

# # 9. Multiplication Grid
# Write a Python program to print:

# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# Hint
# Outer loop represents numbers 1 to 3.
# Inner loop represents numbers 1 to 5.
# Multiply the two loop variables.


for i in range(1,4):
    for j in range(1,6):
        print(i*j,end=" ")
    print()

# # 10. Print Squares in Rows
# Write a Python program to print the squares of numbers from 1 to 5 in 5 rows.

# Expected pattern:

# 1 4 9 16 25
# 1 4 9 16 25
# 1 4 9 16 25
# 1 4 9 16 25
# 1 4 9 16 25
# Hint
# Outer loop controls the rows.
# Inner loop goes from 1 to 5.
# Print the square of the inner-loop number.


for i in range(1,6):
    for j in range(1,6):
        print(j*j,end=" ")
    print()


# # 11. Alphabet Pattern
# Write a Python program to print:

# A
# A B
# A B C
# A B C D
# A B C D E
# Hint
# Outer loop controls the number of characters in each row.
# Inner loop starts from A and prints up to the required character.
# You can use character codes to generate letters.


for i in range(5):
    current_char_code = 65
    for j in range(i+1):
        print(chr(current_char_code), end="")
        current_char_code += 1 
    print()

# # 12. Repeated Alphabet Pattern
# Write a Python program to print:

# A
# B B
# C C C
# D D D D
# E E E E E
# Hint
# Outer loop decides which alphabet to print.
# Inner loop repeats the same alphabet.
# Number of repetitions increases with each row.


for i in range(5): 
    for j in range(i+1):
        ch = chr(65 + j)
        print(ch, end=" ")   
    print()


# # 12. Repeated Alphabet Pattern
# Write a Python program to print:

# A
# B B
# C C C
# D D D D
# E E E E E
# Hint
# Outer loop decides which alphabet to print.
# Inner loop repeats the same alphabet.
# Number of repetitions increases with each row.


for i in range(5):
    ch = chr(65 + i)
    for j in range(i+1):
        print(ch, end="")   
    print()


# # 13. Odd Number Pattern
# Write a Python program to print:

# 1
# 1 3
# 1 3 5
# 1 3 5 7
# 1 3 5 7 9
# Hint
# Outer loop controls the number of values in each row.
# Inner loop generates odd numbers.
# Think about the formula for the nth odd number.

num= 0

for i in range(5):
    for j in range(i+1):
        num = 2*j + 1 
        print(num,end=" ")
    print()


#orrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr

n= int(input("enter your value =>"))

for i in range(n+1):
    for j in range(2*i + 2):
        if j%2 !=0 :
            print (j,end=" ")
    print()


# # 14. Even Number Pattern
# Write a Python program to print:

# 2
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10
# Hint
# Outer loop controls rows.
# Inner loop generates even numbers.
# Think about the formula for the nth even number.


num = 1

for i in range(6):
    for j in range(1,i+1):
        num = 2*j
        print(num,end=" ")
    print()


#orrrrrrrrrrr

n= int(input("enter your value =>"))

for i in range(n+1):
    for j in range(1,2*i + 2):
        if j%2 ==0 :
            print (j,end=" ")
    print()

# # 15. 5×5 Star Square
# Write a Python program to print:

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# Hint
# Outer loop should run 5 times.
# Inner loop should also run 5 times.
# Print a star inside the inner loop.

for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()


# # 16. 5×5 Number Square
# Write a Python program to print:

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# Hint
# Outer loop controls 5 rows.
# Inner loop prints numbers from 1 to 5.
# The inner loop starts again for every row.

for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()


# # 17. Row-wise Numbers
# Write a Python program to print:

# 1 2 3
# 4 5 6
# 7 8 9
# Hint
# Create a number variable before the loops.
# Print the number inside the inner loop.
# Increase the number after every print.

no = int(input("enter a number =>"))

num = 1

for i in range(no):
    for j in range(3):
        print(num,end=" ")
        num +=1 
    print()

# # 18. Print 1 to 20 in 4 Rows
# Write a Python program to print numbers from 1 to 20 in 4 rows, with 5 numbers in each row.

# Expected output:

# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# Hint
# Outer loop should create 4 rows.
# Inner loop should print 5 numbers per row.
# Keep one number variable that continues increasing.

num = 1

for i in range(4):
    for j in range(5):
        
        print(num,end=" ")
        num +=1 
    print()

# # 19. Print Coordinate Pairs
# Write a Python program to print:

# (1,1) (1,2) (1,3)
# (2,1) (2,2) (2,3)
# (3,1) (3,2) (3,3)
# Hint
# Outer loop represents the first coordinate.
# Inner loop represents the second coordinate.
# Print both loop variables together.

for i in range(1,4):
    for j in range(1,4):
        print(f"({i},{j})" , end=" ")
    print()

# # 20. Print All Number Combinations
# For numbers from 1 to 3, print every possible pair:

# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3
# Hint
# Both loops should run from 1 to 3.
# The inner loop must complete all values before the outer loop moves to the next value.

for i in range(1,4):
    for j in range(1,4):
        print(f"{i} {j}")
        

# # 21. 10×10 Multiplication Grid
# Write a Python program to print a multiplication grid from 1 to 10.

# Hint
# Both loops should run from 1 to 10.
# Multiply the outer-loop value by the inner-loop value.
# Use spacing or tabs to make the output readable.


for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=" ")
    print()


# # 22. Repeated Number Pattern
# Write a Python program to print:

# 1
# 22
# 333
# 4444
# 55555
# Hint
# Outer loop decides the number.
# Inner loop decides how many times the number is printed.
# Number of repetitions is equal to the current row.

for i in range(5):
    for j in range(i+1):
        print(i+1 , end="")
    print()

# # 23. Decreasing Number Pattern
# Write a Python program to print:

# 12345
# 1234
# 123
# 12
# 1
# Hint
# Outer loop should decrease from 5 to 1.
# Inner loop should print numbers starting from 1.
# The number of values printed decreases every row.

for i in range(7,0,-1):
    for j in range(1,i-1):
        print(j,end="")
    print()

# # 24. Reverse Number Pattern
# Write a Python program to print:

# 54321
# 5432
# 543
# 54
# 5
# Hint
# Outer loop controls how many numbers are printed.
# Inner loop should print numbers in decreasing order.
# Start with 5 and reduce the ending value after every row.


for i in range(6,0,-1):
    for j in range(i-1,0,-1):
        print(j,end="")
    print()


# # 25. Repeated Row Number Pattern
# Write a Python program to print:

# 11111
# 22222
# 33333
# 44444
# 55555
# Hint
# Outer loop decides which number is printed.
# Inner loop prints the same number 5 times.
# Move to the next number after completing each row.

for i in range(1,6):
    for j in range(1,6):
        print(i,end="")
    print()
