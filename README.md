# Documentación

## 1. Conectar Python con Bases de Datos SQL.
mysql.connector Es una librería que se encarga de permitirnos conectarnos al DML,DDL, manejo de transacciones, etc. De una base de datos SQL.
Documentación de la librería aquí.
### 1.1 Documentación

En caso de necesitar fundamentar: [documentación][], En caso de necesitar inducción: [tutorial][].

[documentación]: https://www.mysql.com/products/connector/
[tutorial]: https://www.youtube.com/watch?v=x7SwgcpACng&list=PLB5jA40tNf3tRMbTpBA0N7lfDZNLZAa9G

### 1.2 Instalación de la librería con PIP
```
//Escribir en la terminal despues de crear un entorno virtual:
pip install mysql.connector
```
### 1.3 Librerías utilizadas
1.3.1 mysql.connector: Es una librería que se encarga de permitirnos conectar Python al DML, DDL, manejo de transacciones, etc. De una base de datos SQL.



```
import mysql.connector
```
### 1.4 Resumen - Tabla de librerías

| Librería       | Función Principal                          |
|----------------|--------------------------------------------|
| `mysql.connector`          | Conectar Python con MySQL.              |

### 1.5 Implementación de la librería
```
import mysql.connector #1.5.1
mydb = mysql.connector.connect( 
    host="localhost", #El host de las bases de datos.
    user="juanpablorod106", #El usuario de mysql.
    password="jugrega", #La contraseña de mysql. 
    database="testdb" #El nombre de la base de datos.
) #1.5.2

print(mydb) #1.5.3

mycursor = mydb.cursor() #1.5.4

mycursor.execute("select * from usuarios where username = 'juanpablorod106'") #1.5.5

for db in mycursor: 
    print(db) #1.5.6
```

#### #1.5.1 
Importar libreria para hacer la conexión de MYSQL con Python.
#### #1.5.2 
Creamos una variable para hacer la conexion con SQL. La variable ```{mydb}``` va a almacenar la funcion ```{mysql.connector.connect()}``` que se encargara de inicializar una conexion con mysql y esto va a devolvernos un objeto. 

La función connect almacenará en su argumento los parametros de acceso a las bases de datos MySQL.

Como lo son:
    
    host="localhost" #El host de las bases de datos.

    user="juanpablorod106" #El usuario de MySQL.

    password="***" #La contraseña de MySQL. 

    database="testdb" #El nombre de la base de datos.

#### #1.5.3
Imprimir el objeto de conexión con la base de datos correspondiente.

##### #1.5.4 
#La variable `{mycursor}` almacenará la variable mydb con la función `{cursor()}` que nos permitirá utilizar el DML de nuestras bases de datos ademas de permitir el manejo de transacciones. Por analogía sería nuestro intermediario entre Python y SQL.
##### #1.5.5
La función `{execute()}` será la utilizada para escribir las consultas SQL. Puede ser utilizada de dos formas principales.

#####   Con un parametro: Dónde escribiremos en una cadena de texto nuestra consulta a la base de datos SQL. Ejemplo de uso:
```
# Supongamos que tenemos una base de datos con una tabla llamada usuarios y queremos seleccionar todos sus campos.
mycursor.execute("select * from usuarios")
```
##### Con dos parametros: Dónde en el primer parametro debemos escribir la sintaxis de inserción de datos y en el segundo parametro una tupla con los datos especificos que vamos a insertar. Ejemplo de uso:
```
sqlinsertusers = "INSERT INTO usuarios(username, email, password_hash, nombre, apellido, fecha_nacimiento, id_online) VALUES (%s,%s,%s,%s,%s,%s,%s);"

new_user = ("juanpablorod106","juanpablorod106@gmail.com", "$2y$10$wIAT23C2DZ0IHXkidMFmLud1j.pruukutP1tANzn/.bCOAiwXmaxC", "Juan", "Rodriguez", "2000-10-23","juanpablorod106") 

mycursor.execute(sqlinsertusers,new_user) #Insertará los valores de la tupla {new_user} en los campos de la tabla usuarios. Estos datos de la tupla se insertarán organizadamente por medio de el caracter de control {%s}.
# A tomar en cuenta: El caracter de control cambia segun el tipo de dato, en este caso todos los campos a llenar serían cadenas de texto, pero en casos como la inserción de por ejemplo un numero entero puede variar (%i). 
```

##### la función `execute()` funcionará por medio de la variable `mycursor`.

##### #1.5.6 
Para obtener la lista de resultados obtenidos por la consulta ejecutada por medio del "cursor" de la base de datos `mycursor.execute()`. Por cada estructura de datos obtenidos del cursor imprime una estructura.

