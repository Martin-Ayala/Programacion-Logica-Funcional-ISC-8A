###
# 04 - Funciones
# Bloques de codigo reutilizables y parametrizables para hacer tareas especificas
###

from os import system
if system("clear") != 0: system("cls")

# """ Definion de una funcion

# def nombre_de_la_funcion(parametro1, parametro2, ...):
#   # docstring
#   # cuerpo de la funcion
#   return valor_de_retorno # opcional

# """

# #Ejemplo de una funcion para imprimir algo en consola
# def saludar():
#     print("¡Hola!")

# #Ejemplo de una funcion con parametro
# def saludar_a(nombre):
#     print(f"¡Hola, {nombre}!")

# saludar_a("Estudiante")
# saludar_a("jefa")
# saludar_a("profesor")
# saludar_a("Directora")
# saludar_a("prefecto")

# #Funciones con mas parametros
# def sumar(a, b):
#     suma = a + b
#     return suma

# result = sumar(2, 3)
# print(result)

# # Documentar las funciones con docstrings
# def restar(a, b):
#     """Resta dos numeros y devuelve el resultado"""
#     return a - b

# parametros por defecto
# def multiplicar(a, b = 2):
#     return a * b

# print(multiplicar(2))
# print(multiplicar(2, 3))

# Argumentos por posición
def describir_persona(nombre: str, edad: int, sexo: str):
    print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}.")

# parametros son posicionales
describir_persona(1, 25, "gato")
describir_persona("Carlos", 25, "pajaro")
describir_persona("persona", "ingeniero", 39)

# Argumentos por clave}
# parametros nombrados
describir_persona(sexo="perro", nombre="Reyes", edad=25)
describir_persona(sexo="mujer", nombre="Alejandra", edad=21)

# Argumentos de longitud de variable (*args)
def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2))
print(sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Argumentos de clave-valor variable (**kwargs):
def mostrar_informacion_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="Carlos", edad=25, sexo="ave")
print("\n")
mostrar_informacion_de(nombre="Sofia", edad=21, country="Mexico")
print("\n")
mostrar_informacion_de(nick="socio", es_sub=True, is_rich=True)
print("\n")
mostrar_informacion_de(super_name="La que barre", es_modo=True, gatos=40)

# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones