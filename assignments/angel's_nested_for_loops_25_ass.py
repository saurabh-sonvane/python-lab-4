# Python Nested Loop Patterns

## 1. Print a 3×3 Star Grid

### Question

Write a Python program to print:

```text
* * *
* * *
* * *
```

### Hint

* Use one loop for 3 rows.
* Use another loop for 3 stars in each row.

### Code

```python
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()
```

---

## 2. Print Numbers in Rows

### Question

Write a Python program to print:

```text
1 2 3
1 2 3
1 2 3
```

### Hint

* Outer loop controls the 3 rows.
* Inner loop should print numbers from 1 to 3.

### Code

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(j, end=" ")
    print()
```

---

## 3. Print Row Numbers

### Question

Write a Python program to print:

```text
1 1 1
2 2 2
3 3 3
```

### Hint

* Outer loop represents the row number.
* Inner loop repeats the current row number 3 times.

### Code

```python
for i in range(1, 4):
    for j in range(3):
        print(i, end=" ")
    print()
```

---

## 4. Increasing Star Pattern

### Question

Write a Python program to print:

```text
*
* *
* * *
* * * *
* * * * *
```

### Hint

* Outer loop runs from 1 to 5.
* Number of stars in each row depends on the current row number.

### Code

```python
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
```

---

## 5. Decreasing Star Pattern

### Question

Write a Python program to print:

```text
* * * * *
* * * *
* * *
* *
*
```

### Hint

* Start with 5 stars.
* Reduce the number of stars by 1 after every row.

### Code

```python
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
```

---

## 6. Increasing Number Pattern

### Question

Write a Python program to print:

```text
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

### Hint

* Outer loop represents the row.
* Inner loop starts from 1 and ends at the current row number.

### Code

```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

---

## 7. Repeated Number Pattern

### Question

Write a Python program to print:

```text
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

### Hint

* The outer loop gives the number to print.
* The inner loop repeats that number according to the row number.

### Code

```python
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()
```

---

## 8. Multiplication Tables from 1 to 5

### Question

Write a Python program to print multiplication tables from 1 to 5.

Each table should contain multiplication from 1 to 10.

### Hint

* Outer loop selects the table number.
* Inner loop runs from 1 to 10.
* Multiply the outer-loop number by the inner-loop number.

### Code

```python
for i in range(1, 6):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()
```

---

## 9. Multiplication Grid

### Question

Write a Python program to print:

```text
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
```

### Hint

* Outer loop represents numbers 1 to 3.
* Inner loop represents numbers 1 to 5.
* Multiply the two loop variables.

### Code

```python
for i in range(1, 4):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()
```

---

## 10. Print Squares in Rows

### Question

Write a Python program to print the squares of numbers from 1 to 5 in 5 rows.

### Expected Output

```text
1 4 9 16 25
1 4 9 16 25
1 4 9 16 25
1 4 9 16 25
1 4 9 16 25
```

### Hint

* Outer loop controls the rows.
* Inner loop goes from 1 to 5.
* Print the square of the inner-loop number.

### Code

```python
for i in range(5):
    for j in range(1, 6):
        print(j * j, end=" ")
    print()
```

---

## 11. Alphabet Pattern

### Question

Write a Python program to print:

```text
A
A B
A B C
A B C D
A B C D E
```

### Hint

* Outer loop controls the number of characters in each row.
* Inner loop starts from A and prints up to the required character.
* You can use character codes to generate letters.

### Code

```python
for i in range(5):
    current_char_code = 65

    for j in range(i + 1):
        print(chr(current_char_code), end=" ")
        current_char_code += 1

    print()
```

---

## 12. Repeated Alphabet Pattern

### Question

Write a Python program to print:

```text
A
B B
C C C
D D D D
E E E E E
```

### Hint

* Outer loop decides which alphabet to print.
* Inner loop repeats the same alphabet.
* Number of repetitions increases with each row.

### Code

```python
for i in range(5):
    ch = chr(65 + i)

    for j in range(i + 1):
        print(ch, end=" ")

    print()
```

---

## 13. Odd Number Pattern

### Question

Write a Python program to print:

```text
1
1 3
1 3 5
1 3 5 7
1 3 5 7 9
```

### Hint

* Outer loop controls the number of values in each row.
* Inner loop generates odd numbers.
* The nth odd number can be generated using `2 * j + 1`.

### Code

```python
for i in range(5):
    for j in range(i + 1):
        num = 2 * j + 1
        print(num, end=" ")

    print()
```

### Alternative Using User Input

```python
n = int(input("Enter your value: "))

for i in range(n):
    for j in range(i + 1):
        num = 2 * j + 1
        print(num, end=" ")

    print()
```

---

## 14. Even Number Pattern

### Question

Write a Python program to print:

```text
2
2 4
2 4 6
2 4 6 8
2 4 6 8 10
```

### Hint

* Outer loop controls rows.
* Inner loop generates even numbers.
* The nth even number can be generated using `2 * j`.

### Code

```python
for i in range(1, 6):
    for j in range(1, i + 1):
        num = 2 * j
        print(num, end=" ")

    print()
```

### Alternative Using User Input

```python
n = int(input("Enter your value: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        num = 2 * j
        print(num, end=" ")

    print()
```

---

## 15. 5×5 Star Square

### Question

Write a Python program to print:

```text
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```

### Hint

* Outer loop should run 5 times.
* Inner loop should also run 5 times.
* Print a star inside the inner loop.

### Code

```python
for i in range(5):
    for j in range(5):
        print("*", end=" ")

    print()
```

---

## 16. 5×5 Number Square

### Question

Write a Python program to print:

```text
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
```

### Hint

* Outer loop controls 5 rows.
* Inner loop prints numbers from 1 to 5.
* The inner loop starts again for every row.

### Code

```python
for i in range(5):
    for j in range(1, 6):
        print(j, end=" ")

    print()
```

---

## 17. Row-wise Numbers

### Question

Write a Python program to print:

```text
1 2 3
4 5 6
7 8 9
```

### Hint

* Create a number variable before the loops.
* Print the number inside the inner loop.
* Increase the number after every print.

### Code

```python
no = int(input("Enter the number of rows: "))

num = 1

for i in range(no):
    for j in range(3):
        print(num, end=" ")
        num += 1

    print()
```

---

## 18. Print 1 to 20 in 4 Rows

### Question

Write a Python program to print numbers from 1 to 20 in 4 rows, with 5 numbers in each row.

### Expected Output

```text
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
```

### Hint

* Outer loop should create 4 rows.
* Inner loop should print 5 numbers per row.
* Keep one number variable that continues increasing.

### Code

```python
num = 1

for i in range(4):
    for j in range(5):
        print(num, end=" ")
        num += 1

    print()
```

--
