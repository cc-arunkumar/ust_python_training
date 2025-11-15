#day2 Task1: Function without arguments and without return

# Task: UST Employee DailyWork Report
# Automation
# Background:
# UST managers maintain daily work reports for each employee.
# Every employee records:
# How many hours they worked,
# How many tasks they completed, and
# Their department name.
# The HR department wants a small Python program that helps them automate a
# few daily actions.
# You have been assigned to build this small program step-by-step using different
# kinds of Python functions.
# The goal of this exercise is not only to get the output but also to understand when
# and why we use:
# 1. Functions with arguments and return values
# 2. Functions without arguments but with return values
# 3. Functions with arguments but without return values
# 4. Functions without arguments and without return values
# 5. Functions with variable arguments ( args )
# Part 1: Function without arguments and without
# return
# Objective:
# Day 2 1
# When the program starts, it should display a small welcome message for the user.
# This message doesn’t depend on any input from the user — it will always remain
# the same.
# Requirements:
# Create a function that prints a welcome message like:
# “Welcome to UST Employee Work Report System”
# “This program helps HR calculate employee performance easily.”
# The function should not take any parameters.
# It should only display the message and not return anything.

# code

# Define a function named Welcome_ust
def Welcome_ust():
    # Print a welcome message for the system
    print("Welcome to UST Employee Work Report System")
    # Print a description of what the program does
    print("This Program helps HR calculate employee Performance easily")

# Call the function to display the messages
Welcome_ust()

#output
# PS C:\Users\303379\day2_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day2_training/functions.py
# Welcome to UST Employee Work Report System
# This Program helps HR calculate employee Performance easily
# PS C:\Users\303379\day2_training> 

