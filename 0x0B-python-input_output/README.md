# Python - Input/Output

Welcome to the Python - Input/Output project repository! This project focuses on file handling in Python, utilizing various built-in functions and modules such as `with`, `open`, `read`, and `json` for reading, writing, serializing, and deserializing files and objects.

## Note: Make all files EXECUTABLE

To ensure proper execution of the files in this project, make sure to set the executable permission on each file.

## Function Prototypes :floppy_disk:

Below are the function prototypes for the functions implemented in this project:

| File        | Prototype               |
| ----------- | ----------------------- |
| `0-read_file.py` | `def read_file(filename=""):` |
| `1-number_of_lines.py` | `def number_of_lines(filename=""):` |
| `2-read_lines.py` | `def read_lines(filename="", nb_lines=0):` |
| `3-write_file.py` | `def write_file(filename="", text=""):` |
| `2-append_write.py` | `def append_write(filename="", text=""):` |
| `3-to_json_string.py` | `def to_json_string(my_obj):` |
| `4-from_json_string.py` | `def from_json_string(my_str):` |
| `5-save_to_json_file.py` | `def save_to_json_file(my_obj, filename):` |
| `6-load_from_json_file.py` | `def load_from_json_file(filename):` |
| `8-class_to_json.py` | `def class_to_json(obj):` |
| `12-pascal_triangle.py` | `def pascal_triangle(n):` |
| `100-append_after.py` | `def append_after(filename="", search_string="", new_string=""):` |

## Tasks :page_with_curl:

This project consists of multiple tasks, each with its own Python file and functionality. Here's an overview of the tasks:

* **0. Read file**
  * [0-read_file.py](./0-read_file.py): This Python function prints the contents of a UTF8 text file to the standard output.

* **1. Write to a file**
  * [1-write_file.py](./1-write_file.py): This Python function writes a string to a UTF8 text file and returns the number of characters written.

* **2. Append to a file**
  * [2-append_write.py](./2-append_write.py): This Python function appends a string to the end of a UTF8 text file and returns the number of characters appended.

* **3. To JSON string**
  * [3-to_json_string.py](./3-to_json_string.py): This Python function returns the JSON string representation of an object.

* **4. From JSON string to Object**
  * [4-from_json_string.py](./4-from_json_string.py): This Python function returns the Python object represented by a JSON string.

* **5. Save Object to a file**
  * [5-save_to_json_file.py](./5-save_to_json_file.py): This Python function writes an object to a text file using JSON representation.

* **6. Create object from a JSON file**
  * [6-load_from_json_file.py](./6-load_from_json_file.py): This Python function creates an object from a `.json` file.

* **7. Load, add, save**
  * [7-add_item.py](./7-add_item.py): This Python script stores all command line arguments to a Python list saved in the file `add_item.json`.

* **8. Class to JSON**
  * [8-class_to_json.py](./8-class_to_json.py): This Python function returns the dictionary description for simple Python data structures