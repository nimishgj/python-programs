import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="captn3m0")

print(mydb)