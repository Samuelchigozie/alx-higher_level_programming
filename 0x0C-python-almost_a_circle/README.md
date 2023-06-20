# Python - Almost a Circle

**Note:** To run the tests and check Test 0, use the following command: `python3 -m unittest tests/test_models/test_base.py`

![Circle](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/331/giphy.mp4)

This project focuses on Python object-oriented programming by implementing three connected classes to represent rectangles and squares. It includes a custom test suite using the `unittest` module to ensure the functionality of each class.

The project utilizes the following Python tools:
* Importing modules
* Handling exceptions
* Working with private attributes
* Implementing getter/setter methods
* Utilizing class/static methods
* Implementing inheritance
* File input/output operations
* Understanding `args` and `kwargs` in Python
* Serializing/deserializing objects to/from JSON and CSV formats
* Writing unit tests using the `unittest` module

## Tests :heavy_check_mark:

* [tests/test_models](./tests/test_models): This folder contains independently developed test files:
  * [test_base.py](./tests/test_models/test_base.py)
  * [test_rectangle.py](./tests/test_models/test_rectangle.py)
  * [test_square.py](./tests/test_models/test_square.py)

## Classes :cl:

### Base
Represents the base class for all other classes in the project. It includes the following features:

* Private class attribute `__nb_objects = 0`.
* Public instance attribute `id`.
* Class constructor `def __init__(self, id=None):`
  * If `id` is `None`, it increments `__nb_objects` and assigns its value to the public instance attribute `id`.
  * Otherwise, it sets the public instance attribute `id` to the provided `id`.
* Static method `def to_json_string(list_dictionaries):` returns the JSON string serialization of a list of dictionaries.
  * If `list_dictionaries` is `None` or empty, it returns the string `"[]"`.
* Class method `def save_to_file(cls, list_objs):` writes the JSON serialization of a list of objects to a file.
  * The parameter `list_objs` is expected to be a list of instances inherited from the `Base` class.
  * If `list_objs` is `None`, the function saves an empty list.
  * The file is saved with the name `<cls name>.json` (e.g., `Rectangle.json`).
  * It overwrites the file if it already exists.
* Static method `def from_json_string(json_string):` returns a list of objects deserialized from a JSON string.
  * The parameter `json_string` is expected to be a string representing a list of dictionaries.
  * If `json_string` is `None` or empty, the function returns an empty list.
* Class method `def create(cls, **dictionary):` instantiates an object with provided attributes.
  * It creates an object with the attributes given in `**dictionary`.
* Class method `def load_from_file(cls):` returns a list of objects instantiated from a JSON file.
  * It reads from the JSON file `<cls name>.json` (e.g., `Rectangle.json`).
  * If the file does not exist, the function returns an empty list.
* Class method `def save_to_file_csv(cls, list_objs):` writes the CSV serialization of a list of objects to a file.
  * The parameter `list_objs` is expected to be a list of instances inherited from the `Base` class.
  * If `list_objs` is `None`, the function saves an empty list.
  