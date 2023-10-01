# postgres

PostgreSQL command line:

**Connecting to PostgreSQL**

```sql
psql -U username -d database
```

This will connect you to the PostgreSQL server as the specified user and database.

**Creating a table**

```sql
CREATE TABLE table_name (
  column_name1 data_type1,
  column_name2 data_type2,
  ...
);
```

This will create a table with the specified name and columns.

**Inserting data into a table**

```sql
INSERT INTO table_name (column_name1, column_name2, ...) VALUES (value1, value2, ...);
```

This will insert a new row into the specified table with the specified values.

**Selecting data from a table**

```sql
SELECT * FROM table_name;
```

This will select all of the rows from the specified table. You can also specify specific columns to select by adding their names to the `SELECT` clause.

**Updating data in a table**

```sql
UPDATE table_name SET column_name = new_value WHERE condition;
```

This will update the value of the `column_name` column in all of the rows in the table that meet the `condition`.

**Deleting data from a table**

```sql
DELETE FROM table_name WHERE condition;
```

This will delete all of the rows in the table that meet the `condition`.

**Other common commands**

* `\l`: List all of the databases on the server.
* `\c database_name`: Connect to the specified database.
* `\d table_name`: Describe the specified table.
* `\q`: Quit PostgreSQL.

**Example queries**

```sql
# Create a table called users with two columns, id and name
CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(255)
);

# Insert a new row into the users table
INSERT INTO users (id, name) VALUES (1, 'John Doe');

# Select all of the users from the users table
SELECT * FROM users;

# Select the user with the ID of 1
SELECT * FROM users WHERE id = 1;

# Update the name of the user with the ID of 1 to "Jane Doe"
UPDATE users SET name = 'Jane Doe' WHERE id = 1;

# Delete the user with the ID of 1
DELETE FROM users WHERE id = 1;
```
