import mysql.connector
from mysql.connector import Error
import os
import time
from alg_luhn import *

def limpiar_terminal():
    """Limpia la pantalla de la terminal independientemente del sistema operativo."""
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Unix/Linux/MacOS
        os.system('clear')

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

def mostrar_juegos_precios():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='juanpablorod106',
            password='jugrega',
            database='testdb'
        )
        cursor = conexion.cursor(dictionary=True)
        
        cursor.execute("SELECT titulo, precio FROM videojuegos ORDER BY precio DESC")
        juegos = cursor.fetchall()
        
        print("\nVIDEOJUEGOS DISPONIBLES:")
        print("=" * 60)
        print(f"{'TÍTULO':30} | {'PRECIO':>10}")
        print("-" * 60)
        for juego in juegos:
            print(f"{juego['titulo'][:30]:30} | ${juego['precio']:>9.2f}")
        print("=" * 60)
        
    except Error as e:
        print(f"Error al obtener videojuegos: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

''' def registrar_tarjeta_segura():
   try:
        username = input("Ingrese su nombre de usuario: ")

        # Consulta segura para obtener el ID
        cursor.execute("SELECT id_usuario FROM usuarios WHERE username = %s", (username,))
        usuario = cursor.fetchone()

        if not usuario:
            print("Error: Usuario no encontrado")
            return
        
        id_usuario = usuario['id_usuario']  # Aquí definimos id_usuario

        print("\nREGISTRO DE TARJETA")
        numero = input("Número completo de tarjeta (16 dígitos): ").replace(" ", "")
        alias = input("Alias para la tarjeta (ej. 'Mi Visa Principal'): ")
        fecha_ven = input("Fecha de vencimiento (MM/YY): ")
        metodo_pago = int(input("ID de método de pago (1=Visa, 2=Mastercard, etc.): "))
        
        # Validación básica
        if len(numero) != 16 or not numero.isdigit():
            print("Número de tarjeta inválido. Debe tener 16 dígitos.")
            return False
            
        if len(fecha_ven) != 5 or fecha_ven[2] != '/':
            print("Formato de fecha inválido. Use MM/YY.")
            return False
            
        validar_luhn(arg_luhn())
            
        # Conexión a la base de datos
        conexion = mysql.connector.connect(
            host='localhost',
            user='juanpablorod106',
            password='juan22092005',
            database='testdb'
        )
        cursor = conexion.cursor()
        
        # Insertar tarjeta (solo últimos 4 dígitos)
        ultimos_4 = numero[-4:]
        
        cursor.execute(
            """INSERT INTO tarjetas 
               (id_usuario, id_metodo_pago, alias_tarjeta, ultimos_cuatro_digitos, 
                token_pago, fecha_vencimiento, saldo) 
               VALUES (%s, %s, %s, %s, %s, %s)""",
            (id_usuario, metodo_pago, alias, ultimos_4, fecha_ven, 0.00)
        )
        
        conexion.commit()
        print("¡Tarjeta registrada exitosamente!")
        return True
        
    except ValueError:
        print("Error: El ID de método de pago debe ser un número.")
    except Exception as e:
        print(f"Error al registrar tarjeta: {e}")
        if 'conexion' in locals():
            conexion.rollback()
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
    return False
'''
'''
 def comprar_con_tarjeta():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='juanpablorod106',
            password='jugrega',
            database='testdb'
        )
        
        cursor = conexion.cursor(dictionary=True)
        
        # ID de usuario.
        username = input("Ingrese su nombre de usuario: ")

        # Consulta segura para obtener el ID
        cursor.execute("SELECT id_usuario FROM usuarios WHERE username = %s", (username,))
        usuario = cursor.fetchone()

        if not usuario:
            print("Error: Usuario no encontrado")
            return
        
        id_usuario = usuario['id_usuario']  # Aquí definimos id_usuario
        
        # ID de juego.
        titulo = input("Ingrese su nombre de juego: ")

        # Consulta segura para obtener el ID
        cursor.execute("SELECT id_usuario FROM usuarios WHERE titulo = %s", (titulo,))
        juego = cursor.fetchone()

        if not juego:
            print("Error: Juego no encontrado")
            return
        
        id_juego = juego['id_juego']  # Aquí definimos id_juego

        # ID de tarjeta.
        four_digitos = input("Ingrese los ultimos cuatro digitos de su numero de tarjeta: ")

        # Consulta segura para obtener el ID
        cursor.execute("SELECT id_usuario FROM usuarios WHERE ultimo_cuatro_digitos = %s", (four_digitos,))
        digitos = cursor.fetchone()

        if not digitos:
            print("Error: Tarjeta no encontrado")
            return
        
        id_tarjeta = digitos['id_tarjeta']  # Aquí definimos id_tarjeta

        cursor = conexion.cursor(dictionary=True)
        
        # Iniciar transacción
        conexion.start_transaction()
        
        # 1. Obtener precio del juego
        cursor.execute("SELECT precio FROM videojuegos WHERE id_juego = %s FOR UPDATE", (id_juego,))
        juego = cursor.fetchone()
        if not juego:
            raise Exception("Juego no encontrado")
        precio = juego['precio']
        
        # 2. Verificar tarjeta y saldo
        cursor.execute(
            """SELECT saldo FROM tarjetas 
               WHERE id_tarjeta = %s AND id_usuario = %s FOR UPDATE""", 
            (id_tarjeta, id_usuario)
        )
        tarjeta = cursor.fetchone()
        
        if not tarjeta:
            raise Exception("Tarjeta no encontrada o no pertenece al usuario")
            
        if tarjeta['saldo'] < precio:
            raise Exception(f"Saldo insuficiente. Saldo actual: ${tarjeta['saldo']:.2f}, Precio: ${precio:.2f}")
        
        # 3. Actualizar saldo
        nuevo_saldo = tarjeta['saldo'] - precio
        cursor.execute(
            "UPDATE tarjetas SET saldo = %s WHERE id_tarjeta = %s",
            (nuevo_saldo, id_tarjeta)
        )
        
        # 4. Registrar en biblioteca
        cursor.execute(
            """INSERT INTO biblioteca_usuario 
               (id_usuario, id_juego, precio_compra) 
               VALUES (%s, %s, %s)""",
            (id_usuario, id_juego, precio)
        )
        
        # 5. Registrar transacción (opcional, si tienes tabla transacciones)
        # cursor.execute("INSERT INTO transacciones (...) VALUES (...)")
        
        conexion.commit()
        print(f"¡Compra exitosa! Nuevo saldo: ${nuevo_saldo:.2f}")
        return True
        
    except Exception as e:
        conexion.rollback()
        print(f"Error en la compra: {e}")
        return False
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
'''
def comprar_videojuego():
    conexion = None
    cursor = None
    
    try:
        # 1. Establecer conexión
        conexion = mysql.connector.connect(
            host='localhost',
            user='juanpablorod106',
            password='jugrega',
            database='testdb'
        )
        cursor = conexion.cursor(dictionary=True)

        # 2. Obtener nombre de usuario
        username = input("\nIngrese su nombre de usuario: ")

        # 3. Obtener ID de usuario
        cursor.execute("SELECT id_usuario FROM usuarios WHERE username = %s", (username,))
        usuario = cursor.fetchone()

        if not usuario:
            print("Error: Usuario no encontrado")
            return False
        
        id_usuario = usuario['id_usuario']

        # 4. Mostrar videojuegos disponibles
        print("\nVIDEOJUEGOS DISPONIBLES:")
        cursor.execute("SELECT id_juego, titulo, precio FROM videojuegos ORDER BY titulo")
        juegos = cursor.fetchall()
        
        if not juegos:
            print("No hay videojuegos disponibles en este momento.")
            return False
        
        for i, juego in enumerate(juegos, 1):
            print(f"{i}. {juego['titulo']} - ${juego['precio']:.2f}")

        # 5. Seleccionar juego
        seleccion = input("\nSeleccione el número del juego (0 para cancelar): ")
        if not seleccion.isdigit() or int(seleccion) < 0 or int(seleccion) > len(juegos):
            print("Selección inválida.")
            return False
        
        if seleccion == "0":
            print("Compra cancelada.")
            return False
        
        juego_seleccionado = juegos[int(seleccion)-1]

        # 6. Verificar si ya lo posee
        cursor.execute(
            "SELECT 1 FROM biblioteca_usuario WHERE id_usuario = %s AND id_juego = %s",
            (id_usuario, juego_seleccionado['id_juego'])
        )
        if cursor.fetchone():
            print(f"Ya posees este juego: {juego_seleccionado['titulo']}")
            return False

        # 7. Confirmar compra
        confirmacion = input(
            f"\n¿Confirmas la compra de '{juego_seleccionado['titulo']}' por ${juego_seleccionado['precio']:.2f}? (S/N): "
        ).upper()

        if confirmacion != "S":
            print("Compra cancelada.")
            return False

        # 8. Insertar en biblioteca (OBJETIVO PRINCIPAL)
        cursor.execute(
            """INSERT INTO biblioteca_usuario 
               (id_usuario, id_juego, fecha_compra, precio_compra) 
               VALUES (%s, %s, CURRENT_TIMESTAMP, %s)""",
            (id_usuario, juego_seleccionado['id_juego'], juego_seleccionado['precio'])
        )
        
        conexion.commit()
        print(f"\n¡Felicidades! Has adquirido '{juego_seleccionado['titulo']}'")
        return True
        
    except Error as e:
        print(f"\nError en la compra: {e}")
        if conexion:
            conexion.rollback()
            interfaz_ps()
        return False
    finally:
        if cursor and conexion and conexion.is_connected():
            cursor.close()
            conexion.close()
            interfaz_ps()


def interfaz_ps():
    limpiar_terminal()
    op = input("\n--- Bienvenido a la interfaz de Usuario de PLaystation --- \n \n Presione 1 si desea ver su biblioteca de juegos. \n Presione 2 si desea ingresar a playstation Network para comprar juegos. \n Sleccione uno de los 2 casos: ")
    match op:
        case "1":
            limpiar_terminal()
            print("--- Bienvenido a tu biblioteca de Videojuegos de PlayStation ---")
            mostrar_biblioteca_usuario()  
        case "2":
            limpiar_terminal()
            print("--- Bienvenido a PlayStation Store ---")
            mostrar_juegos_precios()
            time.sleep(5)
            comprar_videojuego()

import mysql.connector
from mysql.connector import Error

def mostrar_biblioteca_usuario():
    """
    Muestra todos los juegos en la biblioteca de un usuario específico
    
    Args:
        id_usuario (int): ID del usuario cuya biblioteca se quiere mostrar
    """
    conexion = None
    cursor = None
    
    try:
        # 1. Establecer conexión con la base de datos
        conexion = mysql.connector.connect(
            host='localhost',
            user='juanpablorod106',      # Reemplaza con tus credenciales
            password='jugrega', # Reemplaza con tu contraseña
            database='testdb'
        )
        
        cursor = conexion.cursor(dictionary=True)
        
        username = input("Ingrese su nombre de usuario: ")

        # Consulta segura para obtener el ID
        cursor.execute("SELECT id_usuario FROM usuarios WHERE username = %s", (username,))
        usuario = cursor.fetchone()

        if not usuario:
            print("Error: Usuario no encontrado")
            return
        
        id_usuario = usuario['id_usuario']  # Aquí definimos id_usuario

        # 2. Consulta para obtener los juegos del usuario
        query = """
            SELECT v.id_juego, v.titulo, v.descripcion, v.precio, 
                   v.desarrolladora, v.genero, bu.fecha_compra
            FROM biblioteca_usuario bu
            JOIN videojuegos v ON bu.id_juego = v.id_juego
            WHERE bu.id_usuario = %s
            ORDER BY bu.fecha_compra DESC
        """
        cursor.execute(query, (id_usuario,))
        juegos = cursor.fetchall()
        
        # 3. Mostrar resultados
        if not juegos:
            print("\nTu biblioteca está vacía. ¡Visita la tienda para agregar juegos!")
            return
        
        print("\n📚 TU BIBLIOTECA DE VIDEOJUEGOS 📚")
        print("=" * 80)
        print(f"{'ID':<5} | {'TÍTULO':<25} | {'GÉNERO':<15} | {'PRECIO':>10} | {'FECHA COMPRA':<12}")
        print("-" * 80)
        
        for juego in juegos:
            print(
                f"{juego['id_juego']:<5} | "
                f"{juego['titulo'][:25]:<25} | "
                f"{juego['genero'][:15]:<15} | "
                f"${juego['precio']:>9.2f} | "
                f"{juego['fecha_compra'].strftime('%d/%m/%Y')}"
            )
        
        print("=" * 80)
        print(f"Total de juegos en tu biblioteca: {len(juegos)}")
        
    except Error as e:
        print(f"\n❌ Error al cargar la biblioteca: {e}")
    finally:
        op = input("\n    ----- Si deseas salir a la interfaz anterior, Presiona Enter -----    ")
        match op:
            case "":
                interfaz_ps()