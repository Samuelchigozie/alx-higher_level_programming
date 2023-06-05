# Python - Exceptions

In this project, you learned how to handle errors and exceptions in Python using the `try` and `except` statements.

## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File                             | Prototype                                               |
| -------------------------------- | ------------------------------------------------------- |
| `0-safe_print_list.py`           | `def safe_print_list(my_list=[], x=0):`                 |
| `1-safe_print_integer.py`        | `def safe_print_integer(value):`                        |
| `2-safe_print_list_integers.py`  | `def safe_print_list_integers(my_list=[], x=0):`        |
| `3-safe_print_division.py`       | `def safe_print_division(a, b):`                        |
| `4-list_division.py`             | `def list_division(my_list_1, my_list_2, list_length):` |
| `5-raise_exception.py`           | `def raise_exception():`                                |
| `6-raise_exception_msg.py`       | `def raise_exception_msg(message=""):`                  |
| `100-safe_print_integer_err.py`  | `def safe_print_integer_err(value):`                    |
| `101-safe_function.py`           | `def safe_function(fct, *args):`                        |
| `102-magic_calculation.py`       | `def magic_calculation(a, b);`                          |
| `103-python.c`                   | `void print_python_list(PyObject *p);`<br>`void print_python_bytes(PyObject *p);`<br>`void print_python_float(PyObject *p);` |

## Tasks :page_with_curl:

* **0. Safe list printing**
  * [0-safe_print_list.py](./0-safe_print_list.py): This is a Python function that prints `x` elements of a list on the same line, followed by a new line.
  * The parameter `x` represents the number of elements to print and can be greater than the length of `my_list`.
  * The function returns the actual number of elements printed.
  * This function does not import any modules or use the `len()` function.

* **1. Safe printing of an integers list**
  * [1-safe_print_integer.py](./1-safe_print_integer.py): This is a Python function that prints an integer in `"{:d}".format()` format.
  * The parameter `value` can be of any type.
  * The function returns `True` if `value` was printed correctly (i.e., if it was an integer), and `False` otherwise.
  * This function does not import any modules or use the `type()` function.

* **2. Print and count integers**
  * [2-safe_print_list_integers.py](./2-safe_print_list_integers.py): This is a Python function that prints the first `x` elements of a list that are integers on the same line, followed by a new line.
  * The parameter `my_list` can contain elements of any type.
  * The parameter `x` represents the number of elements to print and can be greater than the length of `my_list`.
  * The function returns the actual number of integers printed.
  * This function does not import any modules or use the `len()` function.

* **3. Integers division with debug**
  * [3-safe_print_division.py](./3-safe_print_division.py): This is a Python function that divides two integers and prints the result using `finally`.
  * The function assumes that the arguments are integers.
  * If the division is successful, the function returns the value of the division; otherwise, it returns `None`.
