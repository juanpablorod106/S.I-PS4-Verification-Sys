import mysql.connector 

mydb = mysql.connector.connect(
    host="localhost",
    user="juanpablorod106",
    password="jugrega",
    database="testdb"
)

#print(mydb)

mycursor = mydb.cursor() 

#mycursor.execute("select * from usuarios where username = 'juanpablorod106'")

for db in mycursor: 
    print(db)

# Procedimiento para depositar dinero en la tarjeta.
# CREATE PROCEDURE depositar_dinero(IN dinero_tarjeta int, IN id_tarjeta_persona int) BEGIN UPDATE tarjetas SET saldo = saldo + dinero_tarjeta where id = id_tarjeta_persona; end//
