import mysql.connector

def get_connection():
  return mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pythondb",
    port=3309
  )
