import mysql.connector 

mydb = mysql.connector.connect(
    host="localhost",
    user="juanpablorod106",
    password="jugrega",
    database="testdb"
)

print(mydb)

mycursor = mydb.cursor() 

mycursor.execute("select * from usuarios where username = 'juanpablorod106'")

for db in mycursor: 
    print(db)