import mysql.connector #Importar libreria para hacer la conexión de MYSQL con Python.

#Creamos una variable para hacer la conexion con SQL.
#La variable {mydb} va a almacenar la funcion {mysql.connector.connect()} que se encargara de inicializar una conexion con mysql y esto va a devolvernos un objeto.
mydb = mysql.connector.connect( #La función connect almacenará en su argumento los parametros de acceso a las bases de datos mysql.
    host="localhost", #El host de las bases de datos.
    user="juanpablorod106", #El usuario de mysql.
    password="jugrega", #La contraseña de mysql. 
    database="testdb" #El nombre de la base de datos.
)

print(mydb) #Imprimir el objeto de conexión con la base de datos correspondiente.

mycursor = mydb.cursor() #La variable {mycursor} almacenará la variable mydb con la función {cursor()} que nos permitirá utilizar el DML 
# de nuestras bases de datos ademas de permitir el manejo de transacciones. Por analogía sería nuestro intermediario entre Python y SQL.

sqlinsertusers = "INSERT INTO usuarios(username, email, password_hash, nombre, apellido, fecha_nacimiento, id_online) VALUES (%s,%s,%s,%s,%s,%s,%s);"
new_user = ("juanpablorod106","juanpablorod106@gmail.com", "$2y$10$wIAT23C2DZ0IHXkidMFmLud1j.pruukutP1tANzn/.bCOAiwXmaxC", "Juan", "Rodriguez", "2005-09-22","juanpablorod106")

mycursor.execute("select * from usuarios where username = 'juanpablorod106'")

for db in mycursor:
    print(db)