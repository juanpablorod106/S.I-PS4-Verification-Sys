import mysql.connector 

#Creamos una variable para hacer la conexion con SQL.
#La variable {mydb} va a almacenar la funcion {mysql.connector.connect()} que se encargara de inicializar una conexion con mysql y esto va a devolvernos un objeto.
mydb = mysql.connector.connect( #La función connect almacenará en su argumento los parametros de acceso a las bases de datos mysql.
    host="localhost", #El host de las bases de datos.
    user="root", #El usuario de mysql.
    password="", #La contraseña de mysql. 
    database="testdb" #El nombre de la base de datos.
)

print(mydb)

mycursor = mydb.cursor() 

mycursor.execute("select * from usuarios where username = 'juanpablorod106'")

for db in mycursor: 
    print(db)