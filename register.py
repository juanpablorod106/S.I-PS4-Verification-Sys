import mysql.connector
from mysql.connector import Error

def registrar_usuario():
    # Obtener datos del usuario
    print("\n--- Registro de Nuevo Usuario ---")
    pais = input("Ingrese su país: ")
    region = input("Ingrese su región: ")
    correo = input("Ingrese su correo electrónico: ")
    username = input("Ingrese su ID online (username): ")
    nombre = input("Ingrese su nombre: ") 
    apellido = input("Ingrese su apellido: ")
    password_hash = input("Ingrese su contraseña: ")
    fecha_de_nacimiento = input("Ingrese su fecha de nacimiento en el siguiente formato YYYY/MM/DD: \n")
    ciudad = input("Ingrese su ciudad: ")
    codigo_postal = int(input("Ingrese su código postal: "))
    
    # Conectar a la base de datos
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='juanpablorod106',
            password='jugrega',
            database='testdb'
        )
        
        cursor = conexion.cursor()
        
        # Iniciar transacción
        conexion.start_transaction()
        
        # 1. Insertar o obtener el país
        cursor.execute("INSERT IGNORE INTO paises (nombre_pais) VALUES (%s)", (pais,))
        cursor.execute("SELECT id_pais FROM paises WHERE nombre_pais = %s", (pais,))
        id_pais = cursor.fetchone()[0]
        
        # 2. Insertar o obtener la región
        cursor.execute(
            "INSERT IGNORE INTO regiones (id_pais, nombre_region) VALUES (%s, %s)",
            (id_pais, region)
        )
        cursor.execute(
            "SELECT id_region FROM regiones WHERE id_pais = %s AND nombre_region = %s",
            (id_pais, region)
        )
        id_region = cursor.fetchone()[0]
        
        # 3. Insertar o obtener la ciudad
        cursor.execute(
            "INSERT IGNORE INTO ciudades (id_region, nombre_ciudad, codigo_postal) VALUES (%s, %s, %s)",
            (id_region, ciudad, codigo_postal)
        )
        cursor.execute(
            "SELECT id_ciudad FROM ciudades WHERE id_region = %s AND nombre_ciudad = %s",
            (id_region, ciudad)
        )
        id_ciudad = cursor.fetchone()[0]
        
        # 4. Insertar el usuario principal
        cursor.execute(
            "INSERT INTO usuarios (username, email, password_hash, nombre, apellido, fecha_nacimiento, id_online) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (username, correo, password_hash, nombre, apellido, fecha_de_nacimiento, username)
        )
        id_usuario = cursor.lastrowid
        
        # 5. Insertar el perfil del usuario
        cursor.execute(
            """INSERT INTO perfiles_usuarios 
               (id_usuario, id_pais, id_region, id_ciudad) 
               VALUES (%s, %s, %s, %s)""",
            (id_usuario, id_pais, id_region, id_ciudad)
        )
        
        # Confirmar transacción
        conexion.commit()
        print("\n¡Registro exitoso! Bienvenido/a,", username)
        
    except Error as e:
        conexion.rollback()
        print("\nError al registrar usuario:", e)
        if "Duplicate entry" in str(e):
            if "username" in str(e):
                print("El nombre de usuario ya está en uso.")
            elif "email" in str(e):
                print("El correo electrónico esta en uso.")
            elif "id_online" in str(e):
                print("El id_online esta en uso.")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
def iniciar_sesion():
    print("\n Ingrese su nombre de usuario y su contraseña:")
    username = input("Ingresa tu nombre de usuario: ")
    password = input("Ingresa tu contraseña: ")
        mycursor.execute(f"select username from usuarios where username = '{username}' and password_hash = '{password}';")
        result = mycursor.fetchone()
        if result:
            print("Su usuario existe")
            print(f"Su usuario es \"{username}\" y su contraseña es {password}")
            validar_luhn(arg_luhn())
        else:
            print("Su usuario no existe, vuelva a ingresar sus datos o cree una cuenta.")
            time.sleep(5) #time.sleep() Es una función para congelar el programa durante un tiempo específicado.
            ps4_account_verificaction()