# Python - Object-relational mapping (ORM) Examples

This repository contains a collection of Python scripts that demonstrate how to perform object-relational mapping (ORM) with databases using MySQLdb and SQLAlchemy. The scripts cover various tasks related to querying, creating, editing, and deleting tables in a MySQL database.

## Tests :heavy_check_mark:

* [tests](./tests): This folder contains SQL and Python scripts designed to set up test tables for the provided files. These test files have been provided by ALX.

## Task Overview :page_with_curl:

Each task corresponds to a specific Python script that showcases a particular aspect of object-relational mapping. Here's a summary of each task:

* **Task 0: Get all states**
  * Script: [0-select_states.py](./0-select_states.py)
  * Description: Lists all states in the `hbtn_0e_0_usa` database using MySQLdb.
  * Usage: `./0-select_states.py <mysql username> <mysql password> <database name>`.
  * Results are ordered by ascending `states.id`.

* **Task 1: Filter states**
  * Script: [1-filter_states.py](./1-filter_states.py)
  * Description: Lists states with names starting with `N` in the `hbtn_0e_0_usa` database using MySQLdb.
  * Usage: `./1-filter_states.py <mysql username> <mysql password> <database name>`.
  * Results are ordered by ascending `states.id`.

* **Task 2: Filter states by user input**
  * Script: [2-my_filter_states.py](./2-my_filter_states.py)
  * Description: Displays values matching a given state name in the `states` table of the `hbtn_0e_0_usa` database using MySQLdb.
  * Usage: `./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name searched>`.
  * Results are ordered by ascending `states.id`.
  * Utilizes string formatting to construct the SQL query.

* **Task 3: Safe from SQL Injection...**
  * Script: [3-my_safe_filter_states.py](./3-my_safe_filter_states.py)
  * Description: Displays values matching a given state name in the `states` table of the `hbtn_0e_0_usa` database using MySQLdb. This script is safe from SQL injections.
  * Usage: `./3-my_safe_filter_states.py <mysql username> <mysql password> <database name> <state name searched>`.
  * Results are ordered by ascending `states.id`.

* **Task 4: Cities by states**
  * Script: [4-cities_by_state.py](./4-cities_by_state.py)
  * Description: Lists all cities from the `hbtn_0e_4_usa` database using MySQLdb.
  * Usage: `./4-cities_by_state.py <mysql username> <mysql password> <database name>`.
  * Results are ordered by ascending `cities.id`.

* ... (Continues for each task)

## Getting Started

To run any of the scripts, make sure you have the required dependencies (MySQLdb and SQLAlchemy) installed. You can install them using `pip`:

```bash
pip install mysqlclient SQLAlchemy
```

Then, navigate to the task's script you want to run and execute it with the appropriate command-line arguments.

Feel free to explore and learn from these scripts to enhance your understanding of object-relational mapping in Python.