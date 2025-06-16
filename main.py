from alg_luhn import *
from db import *
import time #time es una librería que proporciona diversas funciones relacionadas con el manejo del tiempo.
from register import *

def ps4_account_verificaction():
    limpiar_terminal()
    print("Bienvenido a Playstation Network... \n")
    op = input("Requiere iniciar sesion o registrarse? \n Presione 1 si requiere iniciar sesion. \n Presione 2 si requiere registrarse. \n Sleccione uno de los 2 casos: ")
    match op:
        case "1":
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
        case "2":
            time.sleep(3)
            limpiar_terminal()
            print("Registro de Playstation \n")
            time.sleep(3)
            registrar_usuario()
            time.sleep(5)
            ps4_account_verificaction()

ps4_account_verificaction()