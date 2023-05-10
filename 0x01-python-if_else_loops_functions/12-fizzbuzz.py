#!/usr/bin/python3
# Author - Samuel Chigozie
"""Output numbers 1 to 100 with a space as a separator.
If a number is divisible by 3, print "Fizz" instead of the number.
If a number is divisible by 5, print "Buzz" instead of the number.
If a num is divisible by both 3 & 5, print "FizzBuzz" than num.
"""


def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
