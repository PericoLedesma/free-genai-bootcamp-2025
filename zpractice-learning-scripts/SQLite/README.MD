# SQLite Tutorial: Introduction and Setup Guide

## What is SQLite?

SQLite is a lightweight, self-contained, and serverless database engine. Unlike other relational database management systems (RDBMS) like MySQL or PostgreSQL, SQLite does not require a separate server process, making it an ideal choice for applications that need an embedded database.

### **Key Features of SQLite:**
- **Serverless:** No need to install and run a separate database server.
- **Zero Configuration:** No setup or administration required.
- **Lightweight:** Uses minimal resources and is ideal for mobile and embedded applications.
- **Cross-Platform:** Works on Windows, macOS, Linux, Android, and iOS.
- **ACID-Compliant:** Supports transactions with atomicity, consistency, isolation, and durability.

## How to Set Up SQLite

### **Step 1: Verify SQLite Installation**
SQLite comes pre-installed on macOS. To check if it is available, open **Terminal** and run:

```sh
sqlite3 --version
```

If SQLite is installed, this will display the installed version number.

### **Step 2: Using SQLite**
Since SQLite is already installed, you can start using it immediately.
```sh
sqlite3 
```

#### **Creating a New Database**
To create and open a database, run:

```sh
sqlite3 mydatabase.db
```

If `mydatabase.db` does not exist, SQLite will create it automatically.

#### **Creating a Table**
Once inside the SQLite shell, you can create a table:

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);
```
If mydatabase.db does not exist, SQLite will create it automatically. This database file will persist on disk and can be reopened later for further use.

#### **Creating a Temporary In-Memory Database**

If you only need a temporary database that disappears when closed, use:

```sh
sqlite3 :memory:
```
This creates an in-memory database that exists only during the session.

#### **Inserting Data**
To add records:

```sql
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com');
```

#### **Querying Data**
To retrieve all records:

```sql
SELECT * FROM users;
```

#### **Exiting SQLite**
Type `.exit` or press **Ctrl + D**.


## Understanding SQLite Persistence

Unlike in-memory databases, SQLite ensures persistent storage when using a .db file. This means that the data remains saved even after the database connection is closed or the system is restarted. SQLite stores data in a single .db file, which contains all tables, indexes, and data.

To check where your database file is stored, use the following command inside the SQLite
shell:

```sql
PRAGMA database_list;
```
This will display the file path of the SQLite database currently in use.

#### Backup Consideration
If you delete the database file manually, all data will be lost permanently. Always back up your .db file if needed.

## Conclusion
You have now verified and started using SQLite on macOS! It’s an excellent choice for lightweight applications and quick database prototyping. Try exploring SQLite further by using SQL commands, integrating it with Python, or using GUI tools like **DB Browser for SQLite**.

Would you like me to cover anything specific, such as using SQLite with Python? 🚀

