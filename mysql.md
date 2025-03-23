# MySQL Data Types

## **1. Numeric Data Types**
- **TINYINT** (1 byte) – Stores integers from -128 to 127 (or 0 to 255 if unsigned).
- **SMALLINT** (2 bytes) – Stores integers from -32,768 to 32,767.
- **MEDIUMINT** (3 bytes) – Stores integers from -8,388,608 to 8,388,607.
- **INT / INTEGER** (4 bytes) – Stores integers from -2,147,483,648 to 2,147,483,647.
- **BIGINT** (8 bytes) – Stores very large integers.
- **DECIMAL (M, D) / NUMERIC** – Stores exact decimal values, where M is the total number of digits, and D is the number of decimal places.
- **FLOAT (4 bytes)** – Stores approximate decimal values with single precision.
- **DOUBLE (8 bytes)** – Stores approximate decimal values with double precision.

## **2. String Data Types**
- **CHAR (M)** – Fixed-length string (1 to 255 characters).
- **VARCHAR (M)** – Variable-length string (1 to 65,535 characters, depending on row size).
- **TEXT** – Stores large text data:
  - **TINYTEXT** (255 characters)
  - **TEXT** (65,535 characters)
  - **MEDIUMTEXT** (16,777,215 characters)
  - **LONGTEXT** (4,294,967,295 characters)
- **BLOB** – Stores binary data (like images and files) with the same size limits as TEXT types.
- **ENUM** – Stores predefined string values (e.g., `'small', 'medium', 'large'`).
- **SET** – Stores multiple predefined values in a single column.

## **3. Date & Time Data Types**
- **DATE** – Stores date values (YYYY-MM-DD).
- **DATETIME** – Stores date and time (YYYY-MM-DD HH:MM:SS).
- **TIMESTAMP** – Stores date and time but updates automatically on changes.
- **TIME** – Stores time (HH:MM:SS).
- **YEAR** – Stores a 4-digit year.

# Common MySQL Commands

## Database Commands
- **Show Databases:** `SHOW DATABASES;` – Lists all databases.
- **Create Database:** `CREATE DATABASE db_name;` – Creates a new database.
- **Use Database:** `USE db_name;` – Selects a database for use.
- **Drop Database:** `DROP DATABASE db_name;` – Deletes a database.

## Table Management Commands
- **Show Tables:** `SHOW TABLES;` – Lists all tables in the selected database.
- **Create Table:**
  ```sql
  CREATE TABLE table_name (
      id INT PRIMARY KEY,
      name VARCHAR(50)
  );
  ```
  – Creates a new table.
- **Drop Table:** `DROP TABLE table_name;` – Deletes a table.
- **Truncate Table:** `TRUNCATE TABLE table_name;` – Deletes all rows but keeps the structure.
- **Rename Table:** `RENAME TABLE old_name TO new_name;` – Renames a table.

## Altering Tables
- **Add Column:** `ALTER TABLE table_name ADD COLUMN age INT;`
- **Modify Column:** `ALTER TABLE table_name MODIFY COLUMN age BIGINT;`
- **Change Column Name:** `ALTER TABLE table_name CHANGE COLUMN age new_age INT;`
- **Drop Column:** `ALTER TABLE table_name DROP COLUMN age;`
- **Add Primary Key:** `ALTER TABLE table_name ADD PRIMARY KEY (id);`
- **Drop Primary Key:** `ALTER TABLE table_name DROP PRIMARY KEY;`
- **Add Foreign Key:**
  ```sql
  ALTER TABLE orders ADD CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id);
  ```
- **Drop Foreign Key:** `ALTER TABLE orders DROP FOREIGN KEY fk_user;`

## Data Manipulation Commands
- **Insert Data:** `INSERT INTO table_name (id, name) VALUES (1, 'John');`
- **Select Data:** `SELECT * FROM table_name;`
- **Update Data:** `UPDATE table_name SET name = 'Jane' WHERE id = 1;`
- **Delete Data:** `DELETE FROM table_name WHERE id = 1;`

## Indexing and Performance
- **Create Index:** `CREATE INDEX idx_name ON table_name(name);`
- **Drop Index:** `DROP INDEX idx_name ON table_name;`
- **Show Indexes:** `SHOW INDEX FROM table_name;`

## User and Privileges Management
- **Create User:** `CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';`
- **Grant Privileges:** `GRANT ALL PRIVILEGES ON db_name.* TO 'user'@'localhost';`
- **Revoke Privileges:** `REVOKE ALL PRIVILEGES ON db_name.* FROM 'user'@'localhost';`
- **Show Users:** `SELECT User, Host FROM mysql.user;`
- **Drop User:** `DROP USER 'user'@'localhost';`

## Transactions
- **Start Transaction:** `START TRANSACTION;`
- **Commit Transaction:** `COMMIT;`
- **Rollback Transaction:** `ROLLBACK;`

## Backup and Restore
- **Backup Database:**
  ```sh
  mysqldump -u user -p db_name > backup.sql
  ```
- **Restore Database:**
  ```sh
  mysql -u user -p db_name < backup.sql
