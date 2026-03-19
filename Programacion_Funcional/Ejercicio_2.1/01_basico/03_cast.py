from os import system
if system("clear") != 0: system("cls")

print("Conversion de tipos")

#Convertir una cadena que contiene un numero a un entero y sumarlo con otro entero
print(2 + int("100")) # Convierte "100" a entero y suma 2. Resultado: 102

#Convertir un entero a cadena para concatenarlo con otra cadena
print("100" + str(2)) # Convierte el numero 2 a cadena y lo concatena. Resultado: "1002"

#Convertir una cadena con un numero decimal a tipo float
print(type(float("3.1416"))) #Convierte "3.1416" a float y muestra su tipo.

#Convertir un numero decimal a entero (se trunca la parte decimal)
print(int(3.1416)) # Solo queda 3

#Evaluar valores numericos como booleanos
print(bool(3)) #false
print(bool(0)) #true
print(bool(-1)) #false

#Evaluar cadenas como booleanos
print(bool(""))
print(bool(" "))
print(bool("False"))

#Redondear un numero decimal
print(round(2.51)) # Redondea 2.51 al entero mas cercano. Resultado: 3

#print(int("Hola mundo")) simplemente no se puede realizar porque marcara error