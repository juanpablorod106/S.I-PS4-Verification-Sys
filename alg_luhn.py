import os

def validar_luhn(numero):
    """
    Valida un número usando el algoritmo de Luhn.
    """
    # 1. Preparar el número
    numero = "".join(filter(str.isdigit, str(numero)))  # Eliminar caracteres no numéricos
    numero_lista = [int(d) for d in numero]
    # 2. Doblar cada segundo dígito
    for i in range(len(numero_lista) - 2, -1, -2):
        numero_lista[i] *= 2
        if numero_lista[i] > 9:
            numero_lista[i] -= 9  # o: numero_lista[i] = (numero_lista[i]//10) + (numero_lista[i]%10)
    # 3. Sumar los dígitos
    suma = sum(numero_lista)
    # 4. Validar
    return suma % 10 == 0

def arg_luhn():
    # 5. Ingresar datos al algoritmo
    numero = input("\n Ingresa tu numero de tarjeta para llevar a cabo esta compra: ")
    if validar_luhn(numero):
        print(f"El número {numero} es válido según Luhn.")
    else:
        print(f"El número {numero} es inválido según Luhn.")