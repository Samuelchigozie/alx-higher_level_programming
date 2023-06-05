
More Classes and Objects
Welcome to the "n" project, where we continue practicing object-oriented programming in Python. This project focuses on various concepts such as class methods, static methods, class vs instance attributes, and the usage of special methods like __str__ and __repr__.

Tests ✔️
tests: This folder contains test files provided by Holberton School.
Tasks 📋
0. Simple Rectangle

0-rectangle.py: This file defines an empty Python class named Rectangle.
1. Real Definition of a Rectangle

1-rectangle.py: This file defines a Python class named Rectangle. It builds upon 0-rectangle.py and adds the following:
A private instance attribute width.
A property getter method def width(self): to retrieve width.
A property setter method def width(self, value): to set width.
A private instance attribute height.
A property getter method def height(self): to retrieve height.
A property setter method def height(self, value): to set height.
Instantiation with optional width and height parameters: def __init(self, width=0, height=0):
If either width or height is not an integer, a TypeError is raised with the message width must be an integer or height must be an integer.
If either width or height is less than 0, a ValueError is raised with the message width must be >= 0 or height must be >= 0.
2. Area and Perimeter

2-rectangle.py: This file defines a Python class named Rectangle. It builds upon 1-rectangle.py and adds the following:
A public instance method def area(self): that returns the area of the rectangle.
A public instance method def perimeter(self): that returns the perimeter of the rectangle. If either width or height is 0, the perimeter is 0.
3. String Representation

3-rectangle.py: This file defines a Python class named Rectangle. It builds upon 2-rectangle.py and adds the following:
A special method __str__ that returns a string representation of the rectangle using the # character. If either width or height is 0, the method returns an empty string.
4. Eval is Magic

4-rectangle.py: This file defines a Python class named Rectangle. It builds upon 3-rectangle.py and adds the following:
A special method __repr__ that returns a string representation of the rectangle.
5. Detect Instance Deletion

5-rectangle.py: This file defines a Python class named Rectangle. It builds upon 4-rectangle.py and adds the following:
A special method __del__ that prints the message Bye rectangle... when a Rectangle instance is deleted.