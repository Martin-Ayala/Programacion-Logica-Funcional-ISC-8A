###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones. 
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en lineas separadas.")

### Completa aquí
print("Nombre: Martin Ayala\nCiudad: FCP")

print("-------------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(type(a))  
print(type(b))  
print(type(c))  
print(type(d))  
print(type(e))  

print("------------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
print(float(int("12345"))) # El resultado es 12345.0
print(int(3.99)) # El resultado es 3, se trunca la parte decimal, no se redondea porque int() solo toma la parte entera

print("------------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# !Hola! Me llamo tu_nombre y tengo tu_edad años, mido tu_altura metros

### Completa aquí
mi_nombre = "Martin Ayala"
mi_edad = 25
mi_altura = 1.75

print(f"!Hola! Me llamo {mi_nombre} y tengo {mi_edad} años, mido {mi_altura} metros")

print("------------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

print(f"El resultado es: {round(3.14159) // 2}")