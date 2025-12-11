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
# Task 2 — Read from MySQL → Python
# Python must:
# 1. Select all employee rows
# 2. Convert them into Python dictionaries
# 3. Print them to console
# CRUD covered: Read
# Task 3 — Modify the Data in Python
# Modify each employee record by adding:
# "category": "Fresher" if age < 25 else "Experienced"
# Example output:
# {
#  "emp_id": 201,
#  "name": "Anu Joseph",
#  "department": "AI",
#  "age": 23,
#  "city": "Trivandrum",
#  "category": "Fresher"
# }
# Task 4 — Store Modified Data INTO MongoDB
# Day 25 4
# Database:
# ust_mongo_db
# Collection:
# employees
# Requirements:
# Insert the modified employee docs into MongoDB
# Use insert_many()
# If collection already exists, clear it first
# CRUD covered: Create
# Task 5 — Perform Basic CRUD on MongoDB
# After insertion, perform:
# 1. Insert ONE new employee
# Add a new record with minimal fields.
# 2. Read ALL employees
# Simple find() .
# 3. Update ONE employee
# Example: update city, change department.
# 4. Delete ONE employee
# Delete using emp_id.
# 5. Delete MANY employees
# Delete by department, e.g., delete Testing employees.
# All 5 CRUD operations are completed.
# Day 25 5
# 7. Expected Deliverables
# Participants must submit:
# 1. employees.json
# Provided above.
# 2. MySQL schema + data inserted
# Screenshots or SQL dump.
# 3. Python script that performs:
# JSON read
# MySQL insert
# MySQL read
# Data transformation
# MongoDB insert
# MongoDB CRUD operations
# 4. MongoDB Compass screenshots
# Collection preview
# CRUD changes visible
from pymongo import MongoClient
from day25.mysql_to_mongodb.sql_crud import update_category

client=MongoClient("mongodb://localhost:27017/")
db=client["ust_mongo_db"]
# db.create_collection("employees")

def insert_into_db():
    content=update_category()
    db.employees.insert_many(content)
    
def insert_one_db():
    nme=input("Enter the name")
    depart=input("Enter the department")
    cty=input("Enter the city")
    db.employees.insert_one({"name":nme,"department": depart,"city":cty})

def read_all_emp():
    content=db.employees.find({})
    for row in content:
        print(row)

def update_emp():
    city=input("Enter the city name")
    department=input("Enter the department")
    content=db.employees.update_one({"city":city},
                                    {"$set":{"department":department}})
    print(content)
    
def delete_one_emp():
    emp_id=int(input("Enter the employee id"))
    content=db.employees.delete_one({"emp_id":emp_id})
    print(content)
    
    

def delete_many_emp():
    department=input("Enter the department to be deleted")
    content=db.employees.delete_many({"department":department})
    print(content)
    
# insert_into_db()
# insert_one_db()
# read_all_emp()
# update_emp()
# delete_one_emp()
delete_many_emp()