
Project Description
This project covers the basics of Python programming language. It includes the implementation of conditional statements (if/else), loops (for/while), functions, and arithmetic operators. The project is divided into 13 tasks with specific requirements for each.

Functions
Here are the prototypes of the functions written in this project:

File	Prototype
7-islower.py	def islower(c):
8-uppercase.py	def uppercase(str):
9-print_last_digit.py	def print_last_digit(number):
10-add.py	def add(a, b):
11-pow.py	def pow(a, b):
12-fizzbuzz.py	def fizzbuzz():
13-insert_number.c	listint_t *insert_node(listint_t **head, int number);
101-remove_char_at.py	def remove_char_at(str, n):
102-magic_calculation.py	def magic_calculation(a, b, c):
Tasks
The following are the 13 tasks included in this project:

Task 0. Positive anything is better than negative nothing
A Python program that assigns a random signed number to the variable number each time it is executed and prints whether number is positive or negative. The program prints the number followed by:

"is positive" if the number is greater than 0
"is zero" if the number is 0
"is negative" if the number is less than 0
Task 1. The last digit
A Python program that assigns a random signed number to the variable number each time it is executed and prints its last digit. The program prints the string "Last digit of [number] is [last_digit]" followed by:

"and is greater than 5" if the last digit is greater than 5
"and is 0" if the last digit is 0
"and is less than 6 and not 0" if the last digit is less than 6 and not 0
Task 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game
A Python program that prints the alphabet in lowercase, not followed by a new line. The program uses only one print and one loop, without storing characters in variables or importing modules.

Task 3. When I was having that alphabet soup, I never thought that it would pay off
A Python program that prints the alphabet in lowercase, followed by a new line. The program uses only one print and one loop, without storing characters in variables or importing modules. It prints every letter except for 'q' and 'e'.

Task 4. Hexadecimal printing
A Python program that prints all numbers from 0 to 98 in decimal and hexadecimal. The program uses only one print and one loop, without storing numbers or strings in variables or importing modules. The printing format is [decimal] = [hexadecimal].

Task 5. 00...99
A Python program that prints numbers from 0 to 99 two digits each. The program separates the numbers by , , except for the last number, which is followed by a new line. The program uses no more than two print functions and one loop, without storing numbers or strings in variables or importing modules.

Task 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need.

ByteCode -> Python #4 mandatory
dis is a disassembler for Python bytecode. Write the Python function def magic_calculation(a, b, c): that does exactly the same as the following Python bytecode:

3 0 LOAD_FAST 0 (a)
3 LOAD_FAST 1 (b)
6 COMPARE_OP 0 (<)
9 POP_JUMP_IF_FALSE 16

4 12 LOAD_FAST 2 (c)
15 RETURN_VALUE

5 >> 16 LOAD_FAST 2 (c)
19 LOAD_FAST 1 (b)
22 BINARY_ADD
23 LOAD_FAST 0 (a)
26 BINARY_POWER
27 RETURN_VALUE

Tips:

Python's dis module may help you a lot.
Python version: 3.4
Return: exactly the same result as the bytecode
