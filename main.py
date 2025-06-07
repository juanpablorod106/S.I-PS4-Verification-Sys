from alg_luhn import *
from db import *

def ps4_account_verificaction():
    print("Bienvenido a Playstation Network... \n")
    op = input("Requiere iniciar sesion o registrarse? \n Presione 1 si requiere iniciar sesion \n Presione 2 si requiere registrarse. \n Sleccione uno de los 2 casos: ")
    match op:
        case "1":
            print("Ingrese su nombre de usuario y su contraseña:")
            username = input("Ingresa tu nombre de usuario: ")
            password = input("Ingresa tu contraseña: ")
            mycursor.execute(f"select username from usuarios where username = '{username}';")
            result = mycursor.fetchone()
            if result:
                print("Su usuario existe")
                print(f"Su usuario es \"{username}\" y su contraseña es {password}")
                validar_luhn(arg_luhn())
            else:
                print("Su usuario no existe")

        case "2":
            print("Registro de Playstation \n")
            pais = input("Ingrese su pais: \n")
            region = input("Ingrese su region: \n")
            correo = input("Ingrese su correo: \n")
            password = input("Ingrese su contraseña: \n")
            ciudad = input("Ingrese su ciudad: \n")
            region = input("Ingrese su region: \n")
            codigo_postal = int(input("Ingrese su codigo postal"))
            username = ("Ingrese su id online: \n")
ps4_account_verificaction()