# JavaScript: Objects, Scopes, and Closures

## Function Prototypes 📼

Below are the function prototypes for the functions implemented in this project:

| File              | Prototype                                               |
| ----------------- | ------------------------------------------------------- |
| `7-occurrences.js`| `exports.nbOccurrences = function(list, searchElement)`|
| `8-esrever.js`    | `exports.esrever = function(list)`                     |
| `9-logme.js`      | `exports.logMe = function(item)`                       |
| `10-converter.js` | `exports.converter = function(base)`                   |

## Tasks 📄

1. **Rectangle #0**
   - [0-rectangle.js](./0-rectangle.js): This JavaScript script defines an empty class `Rectangle`.

2. **Rectangle #1**
   - [1-rectangle.js](./1-rectangle.js): This script defines a class `Rectangle` that builds on [0-rectangle.js](./0-rectangle.js) by adding:
     - A constructor that initializes instance attributes `width` and `height` with the provided parameters `w` and `h`.

3. **Rectangle #2**
   - [2-rectangle.js](./2-rectangle.js): Here, a class `Rectangle` is defined that builds on [1-rectangle.js](./1-rectangle.js) with the addition that if provided `w` and `h` are less than or equal to `0`, an empty object is created.

4. **Rectangle #3**
   - [3-rectangle.js](./3-rectangle.js): This script extends the `Rectangle` class from [2-rectangle.js](./2-rectangle.js) by adding an instance method `print()` to print the rectangle using the `X` character.

5. **Rectangle #4**
   - [4-rectangle.js](./4-rectangle.js): This script further extends the `Rectangle` class from [3-rectangle.js](./3-rectangle.js) with two instance methods:
     - `rotate()`: Swaps the `width` and `height` of the `Rectangle`.
     - `double()`: Multiplies the `width` and `height` of the `Rectangle` by `2`.

6. **Square #0**
   - [5-square.js](./5-square.js): This script defines a `Square` class that inherits from the `Rectangle` class. The constructor of `Square` takes one argument `size`.

7. **Square #1**
   - [6-square.js](./6-square.js): This script builds on [5-square.js](./5-square.js) by adding an instance method `charPrint(c)` to the `Square` class. If `c` is not provided, it uses the character `X` for printing.

8. **Occurrences**
   - [7-occurrences.js](./7-occurrences.js): This JavaScript function returns the number of occurrences of a given element in a list.

9. **Esrever**
   - [8-esrever.js](./8-esrever.js): This JavaScript function reverses a given list.

10. **Log Me**
    - [9-logme.js](./9-logme.js): This JavaScript function prints both the count of arguments already printed and the new argument value. Output format: `<number of arguments already printed>: <current argument value>`

11. **Number Conversion**
    - [10-converter.js](./10-converter.js): This JavaScript function converts a number from base 10 to another base specified as an argument.

12. **Factor Index**
    - [100-map.js](./100-map.js): This script imports an array and creates a new array with each value equal to the value of the initial list multiplied by the index of the new list. Both the initial and new lists are printed.

13. **Sorted Occurrences**
    - [101-sorted.js](./101-sorted.js): This script imports a dictionary of occurrences by user ID and computes a new dictionary of user IDs by occurrences. The resulting dictionary is printed.

14. **Concat Files**
    - [102-concat.js](./102-concat.js): This script concatenates two files passed as arguments into a file specified as the third argument. Usage: `./102-concat.js fileA fileB fileC`.

Feel free to explore these tasks to deepen your understanding of JavaScript's object-oriented features, scopes, and closures!