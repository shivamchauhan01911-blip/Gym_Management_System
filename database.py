import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql@1911",
    database="gymdb"
)

print("MySQL Connected Successfully")