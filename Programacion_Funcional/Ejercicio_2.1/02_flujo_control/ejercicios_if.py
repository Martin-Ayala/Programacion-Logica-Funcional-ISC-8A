###
# EJERCICIOS
###

from os import system
if system("clear") != 0: system("cls")

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
num1 = float(input("Escribe tu primer numero: "))
num2 = float(input("Escribe tu segundo numero: "))

if num1 > num2:
    print(f"Numero {num1} es mayor que {num2}")
elif num2 > num1:
    print(f"Numero {num2} es mayor que {num1}.")
else:
    print("Los numeros son iguales")

print("\n------------------")
# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

#Pedir los datos al usuario
num1 = float(input("Escribe tu primer numero: "))
num2 = float(input("Escribe tu segundo numero: "))
operacion = input("Selecciona la operacion (+, -, *, /): ")

#Logica de la calculadora
if operacion == "+":
    result = num1 + num2
    print(f"Resultado: {num1} + {num2} = {result}")

elif operacion == "-":
    result = num1 - num2
    print(f"Resultado: {num1} - {num2} = {result}")

elif operacion == "*":
    result = num1 * num2
    print(f"Resultado: {num1} * {num2} = {result}")

elif operacion == "/":
    # Manejo de la división entre cero
    if num2 != 0:
        result = num1 / num2
        print(f"Resultado: {num1} / {num2} = {result}")
    else:
        print("Error: No se puede dividir entre cero.")

else:
    print("Operacion no valida. Usa +, -, * o /")

print("\n------------------")
# Ejercicio 3: Año bisiesto
# Pide al usuario introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero 

# no por 400.
#Pedimos el año al usuario
año = int(input("Escribe un año: "))

#Logica para determinar si el año es bisiesto o no
#Se usa el operador % para saber si el residuo es 0 (es divisible)
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto")
else:
    print(f"El año {año} no es bisiesto")

print("\n------------------")
# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

#Pedimos la edad al usuario
edad = int(input("Escribe tu edad: "))

#Clasificación por rangos
if edad <= 2:
    print("Tu categoria es: Bebé")
elif edad <= 12:
    print("Tu categoria es: Niño")
elif edad <= 17:
    print("Tu categoria es: Adolescente")
elif edad <= 64:
    print("Tu categoria es: Adulto")
else:
    print("Tu categoria es: Adulto mayor")