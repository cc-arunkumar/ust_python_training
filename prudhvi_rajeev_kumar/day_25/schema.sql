USE ust_mysql_db;

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,              
    name VARCHAR(50) NOT NULL,           
    department VARCHAR(30),              
    age INT,                             
    city VARCHAR(30)                     
);


