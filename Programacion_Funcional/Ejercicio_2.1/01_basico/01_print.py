from os import system
if system("clear") != 0: system("cls")

print("Hola Crayola")
print('Esto tambien funciona con una comilla')
print("Python", "es", "genial")
print("Python", "es", "brutal", sep= "-")

print("Esto se imprime", end = "\n")
print("en una linea")

print(42)

print('Esto es una "pulgada" dentro de un string con comillas simples')
print("Esto es una \"pulgada\" dentro de un string con comillas dobles")
print("""Esto es una "pulgada" dentro de un string con triple comillas""")