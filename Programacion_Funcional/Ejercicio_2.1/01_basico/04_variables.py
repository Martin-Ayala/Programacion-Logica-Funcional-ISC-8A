from os import system
if system("clear") != 0: system("cls")

# Para asignar una variable solo hace falta el nombre de la variable y asignarlo
my_name = "Martin"
print(my_name)

age = 18
print(age)

age = 22
print(age)

#Tipado dinamico: el tipo de dato se determina en tiempo de ejecucion
#No es necesario declarar explicitamente el tipo de variable
name = "Martin"
print(type(name)) #Muestra el tipo de dato de la variable name (str)

name = 32
print(type(name)) #Muestra ahora el tipo de dato como int

#Tipado fuerte
#print(10 + "2") esto no se puede

#f-string (literal de cadena de formato)
print(f"Hola {my_name}, tengo {age + 5} años")

#No recomendada forma de asignar variables
mi_nombre_de_variable = "ok" #snake_case
nombre = "ok"

miNombreDeVariable = "no-recomendado" #camelCase
MiNombreDeVariable = "no-recomendado" #PascalCase
minombredevariable = "no-recomendado" #todojunto

mi_nombre_de_variable_123 = "ok"

MI_CONSTANTE = 3.14 # UPPER_CASE -> constantes

#Anotaciones de tipo (opcional, para mayor claridad en el codigo)
is_user_logged_in: bool = True # Indica que la variable es un booleano
print(is_user_logged_in)

name: str = "Martin" #Indica que la variable es una cadena de texto
print(name)
