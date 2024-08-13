# Assisted by WCA@IBM
# Latest GenAI contribution: ibm/granite-20b-code-instruct-v2
# import pyodbc
import os
import csv
import json


# Construct the connection string
def runQuery():
    server = os.getenv("SQL_SERVER_HOSTNAME")
    database = os.getenv("SQL_DATABASE_NAME")
    username = os.getenv(" SQL_DATABASE_USERNAME")
    password = os.getent(" SQL_DATABASE_PASSWORD")
    driver = "{ODBC Driver 17 for SQL Server}"
    conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    # Establish a connection with the database
    # with pyodbc.connect(conn_str) as conn:
    #     # Create a cursor object
    #     cursor = conn.cursor()

    #     # Execute a query
    #     cursor.execute("SELECT * FROM Customers")

    #     # Fetch all rows
    #     rows = cursor.fetchall()

    #     # Print the results
    #     for row in rows:
    #         print(row)

def getServiceByName(name):
    query = f"SELECT * FROM SERVICES WHERE NAME = {name}"
    # runQuery(query)
    return "Happy!"