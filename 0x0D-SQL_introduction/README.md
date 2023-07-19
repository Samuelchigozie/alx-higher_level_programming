# SQL Project - Introduction to Relational Databases

Welcome to the SQL project where we explore relational databases and practice introductory SQL data definitions and data manipulation language, including making subqueries and using functions.

## Tasks :page_with_curl:

* **Task 0: List Databases**
  * [0-list_databases.sql](./0-list_databases.sql): This MySQL script lists all databases.

* **Task 1: Create a Database**
  * [1-create_database.sql](./1-create_database.sql): This MySQL script creates a new database named `hbtn_0c_0`.

* **Task 2: Delete a Database**
  * [2-remove_databases.sql](./2-remove_databases.sql): This MySQL script deletes the database `hbtn_0c_0`.

* **Task 3: List Tables**
  * [3-list_tables.sql](./3-list_tables.sql): This MySQL script lists all tables in the current database.

* **Task 4: Create the First Table**
  * [4-first_table.sql](./4-first_table.sql): This MySQL script creates a table named `first_table` with the following columns:
    * `id`: INT
    * `name`: VARCHAR(256)

* **Task 5: Display Full Description**
  * [5-full_table.sql](./5-full_table.sql): This MySQL script prints the full description of the table `first_table`.

* **Task 6: List All Rows in the First Table**
  * [6-list_values.sql](./6-list_values.sql): This MySQL script lists all rows in the `first_table`.

* **Task 7: Insert a New Row**
  * [7-insert_value.sql](./7-insert_value.sql): This MySQL script inserts a new row into the `first_table` with the following values:
    * `id` = `89`
    * `name` = `Best School`

* **Task 8: Count Records with id=89**
  * [8-count_89.sql](./8-count_89.sql): This MySQL script displays the number of records with `id = 89` in the `first_table`.

* **Task 9: Create and Populate the Second Table**
  * [9-full_creation.sql](./9-full_creation.sql): This MySQL script creates and fills a table named `second_table` with the following columns:
    * `id`: INT
    * `name`: VARCHAR(256)
    * `score`: INT
  * Records:
    * `id` = 1, `name` = "John", `score` = 10
    * `id` = 2, `name` = "Alex", `score` = 3
    * `id` = 3, `name` = "Bob", `score` = 14
    * `id` = 4, `name` = "George", `score` = 8

* **Task 10: List Records in `second_table` by Best Scores**
  * [10-top_score.sql](./10-top_score.sql): This MySQL script lists the `score` and `name` of all records in the `second_table` in descending order of their `score`.

* **Task 11: Select Records with Score >= 10**
  * [11-best_score.sql](./11-best_score.sql): This MySQL script lists the `score` and `name` of all records in the `second_table` with a `score >= 10`, in descending order of their score.

* **Task 12: Update Bob's Score**
  * [12-no_cheating.sql](./12-no_cheating.sql): This MySQL script updates Bob's score to 10 in the `second_table`.

* **Task 13: Remove Records with Low Scores**
  * [13-change_class.sql](./13-change_class.sql): This MySQL script removes all records from the `second_table` with a `score <= 5`.

* **Task 14: Calculate Average Score**
  * [14-average.sql](./14-average.sql): This MySQL script computes the average `score` of all records in the `second_table`.

* **Task 15: Count Records Grouped by Score**
  * [15-groups.sql](./15-groups.sql): This MySQL script lists the `score` and the number of records with the same score in the `second_table`, in descending order of the count.

* **Task 16: List Records with Names and Scores**
  * [16-no_link.sql](./16-no_link.sql): This MySQL script lists the `score` and `name` of all records in the `second_table` in descending order of their `score`. It does not display rows without a `name` value.

* **Task 17: Convert Database to UTF8**
  * [100-move_to_utf8.sql](./100-move_to_utf8.sql): This MySQL script converts the `hbtn_0c_0` database to UTF8 encoding.

* **Task 18: Average Temperatures by City**
  * [101-avg_temperatures.sql](./101-avg_temperatures.sql): This MySQL script displays the average temperature (Fahrenheit) for each city in descending order.

* **Task 19: Top Cities by Average Temperature**
  * [102-top_city.sql](./102-top_city.sql): This MySQL script displays the three cities with the highest average temperature from July to August in descending order.

* **Task 20: Maximum Temperature by State**
  * [103-max_state.sql](./103-max_state.sql): This MySQL script displays the maximum temperature of each state, ordered by state name.

## Dump File :dolphin:
* Tasks 101-103 queries from the database are available in [temperatures.sql](./temperatures.sql).