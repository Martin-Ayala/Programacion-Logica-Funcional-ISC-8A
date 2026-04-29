###
# 03 - range()
# Permite crear una secuencia de numeros. Puede ser util para for, pero no solo para eso
###

from os import system
if system("clear") != 0: system("cls")

print("\nrange():")

# Generado una secuencia de numeros del 0 al 9
for num in range(10):
    print(num)

# range (inicio, fin)
for num in range(5, 10):
    print(num)

#range (inicio, fin, paso)
for num in range(0, 1000, 5):
    print(num)

for num in range(-5, 0):
    print(num)

for num in range(10, 0, -1):
    print(num)

for num in range(0, 444):
    print(num)

nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)

# seria para hacerlo cinco veces
for _ in range(5):
    print("hacer cinco veces algo")

###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir numeros del 1 al 10
#Imprime los numeros del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")

# Ejercicio 2: Imprimir numeros impares del 1 al 20