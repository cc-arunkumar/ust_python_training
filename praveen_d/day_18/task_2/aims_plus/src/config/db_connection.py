import pymysql
import mysql.connector
import csv
from datetime import datetime 

def get_connection():
    conn=pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database=""
    )
    return conn
    
