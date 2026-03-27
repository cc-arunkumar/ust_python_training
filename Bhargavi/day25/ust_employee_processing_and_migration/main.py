
# Day 25
# UST – Employee Migration & Processing
# Project Requirement Document
# 1. Project Overview
# UST is migrating part of its internal employee data from legacy systems (stored in 
# MySQL) into a newer flexible analytics system built on MongoDB.
# Before migrating, a small data transformation is required by a Python service.
# This project simulates that end-to-end pipeline.
# 2. Objective
# Participants must:
# 1. Read JSON sample employee data
# 2. Load it into MySQL (ust_mysql_db)
# 3. Read data back from MySQL using Python
# 4. Modify/transform the data slightly
# 5. Store the transformed data into MongoDB (ust_mongo_db)
# 6. Perform basic CRUD operations in both MySQL and MongoDB
# 3. Entity Used - Employees
# Only one entity is used:
# employee
# Day 25 1
# 4. JSON Sample Data
# Save as employees.json
# [
#  {
#  "emp_id": 201,
#  "name": "Anu Joseph",
#  "department": "AI",
#  "age": 23,
#  "city": "Trivandrum"
#  },
#  {
#  "emp_id": 202,
#  "name": "Rahul Menon",
#  "department": "Cloud",
#  "age": 26,
#  "city": "Kochi"
#  },
#  {
#  "emp_id": 203,
#  "name": "Sahana R",
#  "department": "Testing",
#  "age": 22,
#  "city": "Chennai"
#  },
#  {
#  "emp_id": 204,
#  "name": "Vishnu Prakash",
#  "department": "Cybersecurity",
#  "age": 29,
#  "city": "Trivandrum"
#  },
#  {
#  "emp_id": 205,
#  "name": "Maya Kumar",
# Day 25 2
#  "department": "AI",
#  "age": 25,
#  "city": "Bangalore"
#  }
# ]
# 5. MySQL Table Requirement
# Database:
# ust_mysql_db
# Table:
# employees
# Schema: employees Table Structure
# Column Name Data Type Constraints Description
# emp_id INT PRIMARY KEY Unique employee ID
# name VARCHAR(50)
# NOT NULL
# (optional) Employee full name
# department VARCHAR(30) —
# Department name
# (AI/Cloud/Testing etc.)
# age INT — Employee age
# city VARCHAR(30) — Employee city
# 6. Required Tasks
# Task 1 — Load JSON → MySQL
# Python app must:
# Day 25 3
# 1. Read employees.json
# 2. Insert all records into MySQL table
# 3. Prevent duplicates using emp_id (primary key)
# 4. Confirm row count
# CRUD covered: Create


# Import the necessary scripts
from load_data_to_mysql import load_data_to_mysql
from read_from_mysql import read_from_mysql
from store_to_mongo import store_to_mongo
from perform_mongo_crud_operations import perform_mongo_crud_operations

def main():
    # Step 1: Load data into MySQL
    print("Loading data into MySQL...")
    load_data_to_mysql()

    # Step 2: Read data from MySQL, modify it, and store it in MongoDB
    print("Reading data from MySQL and inserting into MongoDB...")
    store_to_mongo()

    # Step 3: Perform CRUD operations in MongoDB
    print("Performing CRUD operations in MongoDB...")
    perform_mongo_crud_operations()

if __name__ == "__main__":
    main()

# Successfully connected to the database.
# Checking if employee 201 exists...
# Employee 201 already exists, skipping insertion.
# Checking if employee 202 exists...
# Employee 202 already exists, skipping insertion.
# Checking if employee 203 exists...
# Employee 203 already exists, skipping insertion.
# Checking if employee 204 exists...
# Employee 204 already exists, skipping insertion.
# Checking if employee 205 exists...
# Employee 205 already exists, skipping insertion.
# Data loading completed
# [{'emp_id': 201, 'name': 'Anu Joseph', 'department': 'AI', 'age': 23, 'city': 'Trivandrum', 'category': 'Fresher'}, {'emp_id': 202, 'name': 'Rahul Menon', 'department': 'Cloud', 'age': 26, 'city': 'Kochi', 'category': 'Experienced'}, {'emp_id': 203, 'name': 'Sahana R', 'department': 'Testing', 'age': 22, 'city': 'Chennai', 'category': 'Fresher'}, {'emp_id': 204, 'name': 'Vishnu Prakash', 'department': 'Cybersecurity', 'age': 29, 'city': 'Trivandrum', 'category': 'Experienced'}, {'emp_id': 205, 'name': 'Maya Kumar', 'department': 'AI', 'age': 25, 'city': 'Bangalore', 'category': 'Experienced'}]
# Data successfully inserted into MongoDB.
# Employee 206 inserted.
# All employees:
# {'_id': ObjectId('69392091b81e94445106a7f1'), 'emp_id': 201, 'name': 'Anu Joseph', 'department': 'AI', 'age': 23, 'city': 'Trivandrum', 'category': 'Fresher'}
# {'_id': ObjectId('69392091b81e94445106a7f2'), 'emp_id': 202, 'name': 'Rahul Menon', 'department': 'Cloud', 'age': 26, 'city': 'Kochi', 'category': 'Experienced'}
# {'_id': ObjectId('69392091b81e94445106a7f3'), 'emp_id': 203, 'name': 'Sahana R', 'department': 'Testing', 'age': 22, 'city': 'Chennai', 'category': 'Fresher'}
# {'_id': ObjectId('69392091b81e94445106a7f4'), 'emp_id': 204, 'name': 'Vishnu Prakash', 'department': 'Cybersecurity', 'age': 29, 'city': 'Trivandrum', 'category': 'Experienced'}
# {'_id': ObjectId('69392091b81e94445106a7f5'), 'emp_id': 205, 'name': 'Maya Kumar', 'department': 'AI', 'age': 25, 'city': 'Bangalore', 'category': 'Experienced'}
# {'_id': ObjectId('69392091b81e94445106a7f7'), 'emp_id': 206, 'name': 'Arjun Sharma', 'department': 'AI', 'age': 28, 'city': 'Mumbai', 'category': 'Experienced'}
# Employee 206 updated.
# Employee 206 deleted.
# All AI department employees deleted.
# Loading data into MySQL...
# Successfully connected to the database.
# Checking if employee 201 exists...
# Employee 201 already exists, skipping insertion.
# Checking if employee 202 exists...
# Employee 202 already exists, skipping insertion.
# Checking if employee 203 exists...
# Employee 203 already exists, skipping insertion.
# Checking if employee 204 exists...
# Employee 204 already exists, skipping insertion.
# Checking if employee 205 exists...
# Employee 205 already exists, skipping insertion.
# Data loading completed
# Reading data from MySQL and inserting into MongoDB...
# Data successfully inserted into MongoDB.
# Performing CRUD operations in MongoDB...
# Employee 206 inserted.
# All employees:
# {'_id': ObjectId('69392091b81e94445106a7f9'), 'emp_id': 201, 'name': 'Anu Joseph', 'department': 'AI', 'age': 23, 'city': 'Trivandrum', 'category': 'Fresher'}
# {'_id': ObjectId('69392091b81e94445106a7fa'), 'emp_id': 202, 'name': 'Rahul Menon', 'department': 'Cloud', 'age': 26, 'city': 'Kochi', 'category': 'Experienced'}
# {'_id': ObjectId('69392091b81e94445106a7fb'), 'emp_id': 203, 'name': 'Sahana R', 'department': 'Testing', 'age': 22, 'city': 'Chennai', 'category': 'Fresher'}
# {'_id': ObjectId('69392091b81e94445106a7fc'), 'emp_id': 204, 'name': 'Vishnu Prakash', 'department': 'Cybersecurity', 'age': 29, 'city': 'Trivandrum', 'category': 'Experienced'}
# {'_id': ObjectId('69392091b81e94445106a7fd'), 'emp_id': 205, 'name': 'Maya Kumar', 'department': 'AI', 'age': 25, 'city': 'Bangalore', 'category': 'Experienced'}
# {'_id': ObjectId('69392091b81e94445106a7ff'), 'emp_id': 206, 'name': 'Arjun Sharma', 'department': 'AI', 'age': 28, 'city': 'Mumbai', 'category': 'Experienced'}
# Employee 206 updated.
# Employee 206 deleted.
# All AI department employees deleted.