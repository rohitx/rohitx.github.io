---
layout: post
title: Create a Database in mySQL 
tags: sql 
summary: Creating databases in the opensource SQL database (DB) program is quite straightforward. We just need to create an empty table,name the
---
Creating databases in the opensource SQL database (DB) program is quite straightforward. We just need to create an empty table, name the columns, and insert rows. This post shows you step-by-step how to create a table. In this post we will create a table of books inventory. 

The very first step is to "login" into our mySQL DB as a root. The default the root password for mySQL on your machine is blank. That is there is no password. So, to login do the following: 

~~~python

mysql -u root 

~~~

However, if you have a root password, you would need to type the following: 

~~~python

mysql -u root -p 

~~~

Once you enter the password, or have none, you should get a mysql prommpt. Now we create a new database. The command to create a blank DB is the following:  

~~~python

mysql> create database books;
Query OK, 1 row affected (0.00 sec) 

~~~

This command creates an empty database. Once this is created, we name each column in our database. 

~~~python
mysql> create table books (
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    -> Title varchar(20),
    -> Author varchar(20),
    -> CurrentMonthSales int(10));
Query OK, 0 rows affected (0.05 sec)
~~~

In this example, I have created 3 columns: Title, Author, CurrentMonthSales. If you have more columns, you could keep typing each column name on separate row in your terminal. Note that each column needs to be specified by its datatype. In this example, the first two columns are string literals while the third column is an integer. 

To view the description of the table we just created, do the following: 

~~~python

mysql> desc books;

~~~

![My helpful screenshot](/assets/mysql_db_command.jpg)

Now we begin to insert rows in our empty DB. We do this by inserting each row at a time: 

~~~python
insert into books values(1,'Pride and Prejudice', 'Austen', 15);
insert into books values(2, 'Animal Farm', 'Orwell', 7);
insert into books values(3, 'Merchant of Venice', 'Shakespeare', 5);
insert into books values(4, 'Romeo and Juliet', 'Shakespeare', 8);
insert into books values(5, 'Oliver Twist', 'Dickens', 3);
insert into books values(6, 'Candide', 'Voltaire', 9);
insert into books values(7, 'The Scarlet Letter', 'Hawthorne', 12);
insert into books values(8, 'Hamlet', 'Shakespeare', 2);
~~~

There we have it, we now have a database table with rows and columns. We can view the table using the basic SQL command: 

~~~python
mysql> select * from books;
+----+---------------------+-------------+-------------------+
| id | Title               | Author      | CurrentMonthSales |
+----+---------------------+-------------+-------------------+
|  1 | Pride and Prejudice | Austen      |                15 |
|  2 | Animal Farm         | Orwell      |                 7 |
|  3 | Merchant of Venice  | Shakespeare |                 5 |
|  4 | Romeo and Juliet    | Shakespeare |                 8 |
|  5 | Oliver Twist        | Dickens     |                 3 |
|  6 | Candide             | Voltaire    |                 9 |
|  7 | The Scarlet Letter  | Hawthorne   |                12 |
|  8 | Hamlet              | Shakespeare |                 2 |
+----+---------------------+-------------+-------------------+
8 rows in set (0.00 sec)
~~~

Note that the database is automatically saved to drive. If you were to start a new session, you will first need to login into mySQL and then do the following: 

~~~python

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| books              |
| mysql              |
| performance_schema |
| test               |
| thegeekstuff       |
+--------------------+
7 rows in set (0.00 sec)

~~~

There we see our database called "books". To work on this database, we first load it into mySQL as: 

~~~python

mysql> use books;

Database changed

~~~