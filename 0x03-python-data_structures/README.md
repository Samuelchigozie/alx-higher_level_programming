Title: Python Data Structures: Lists and Tuples (0x03)

Introduction:
This repository contains solutions to Python data structure problems related to lists and tuples. There are a total of 13 Python scripts and one C program in this repository, each of which deals with a different data structure problem. In addition to the scripts, there is also a header file for the C program and a Python script to test the C function.

Table of Contents:

0-print_list_integer.py: A Python function that prints all integers of a list.
1-element_at.py: A Python function that retrieves an element from a list like in C.
2-replace_in_list.py: A Python function that replaces an element of a list at a specific position (like in C).
3-print_reversed_list_integer.py: A Python function that prints all integers of a list in reverse order.
4-new_in_list.py: A Python function that replaces an element in a list at a specific position without modifying the original list (like in C).
5-no_c.py: A Python function that removes all characters "c" and "C" from a string.
6-print_matrix_integer.py: A Python function that prints a matrix of integers.
7-add_tuple.py: A Python function that adds 2 tuples.
8-multiple_returns.py: A Python function that returns a tuple with the length of a string and its first character.
9-max_integer.py: A Python function that finds the biggest integer of a list.
10-divisible_by_2.py: A Python function that finds all multiples of 2 in a list.
11-delete_at.py: A Python function that deletes the item at a specific position in a list.
12-switch.py: A Python program that completes source code in order to switch the values of a and b.
13-is_palindrome.c: A C program that checks if a singly linked list is a palindrome.
lists.h: A header file for the C program.
100-print_python_list_info.c: A C function to compile in a shared library that prints info on a Python list.
100-test_lists.py: A Python script to test the C function above.
Execution:
To execute the Python scripts, simply run the command "python <filename>". To execute the C program, compile it with the command "gcc -Wall -Werror -Wextra -pedantic 100-print_python_list_info.c -shared -o <output_file_name>.so" and then run the Python script "100-test_lists.py".

Note: The script "12-switch.py" requires execution permissions. If you encounter permission issues, use "chmod u+x 12-switch.py" before running the script.
