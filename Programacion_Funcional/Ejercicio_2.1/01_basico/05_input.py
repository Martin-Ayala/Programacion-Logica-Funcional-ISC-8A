from os import system
if system("clear") != 0: system("cls")

#Para obtener datos del usuario se usa la funcion input()
#La funcion input() recibe un mensaje que se muestra al usuario
#y devuelve el valor introducido por el usuario
nombre = input("Hola, ¿Como te llamas?\n")
print(f"Hola {nombre}, encantado de conocerte")

#Ten en cuenta que la funcion input() devuelve un string
#Asi que si queremos obtener un numero se debe convertir el string a un numero
age = input("¿Cuantos años tienes?\n")
age = int(age)
print(f"Tienes {age} años")

#La funcion input() tambien puede devolver multiples valores
#Para hacerlo, el usuario debe separar los valores con una coma
print("Obtener multiples valores a la vez")
country, city = input("¿En que pais y ciudad vives?\n").split()

print(f"Vives en {country}, {city}")