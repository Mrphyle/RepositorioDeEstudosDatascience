import mysql.connector as mysql
connection= mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="PepleDB"
)
cursor= connection.cursor()
print("\n==============================\nExemple:Select name FROM Peple\n==============================\n")
query = input("Enter your SQL query: ")
cursor.execute(query)
results = cursor.fetchall()
for string in results:
    print(string)        