import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="87Amore;;w34"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Petmatch")