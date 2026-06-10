# Compresion de lista

# EJEMPLO DE FUNCION ANONIMA = LAMBDA

doble = lambda x: x * 2  # funcion anonima que recibe un argumento x y devuelve su doble
doble
print(doble(5))


def cuadrado(x):
    print(cuadrado(4))


# funcion de orden superior que recibe una funcion como argumento
def aplicar_funcion(funcion, valor):
    return funcion(valor)


# objetivo: Mostrar el uso de compresion de listas en python

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doble = []

for n in numeros:
    doble.append(n * 2)

print(doble)


# Genera otra lista de los cuadrados de los numeros en la lista numeros
cuadrados = [num**2 for num in numeros]

lista_cuadruple = list(map(lambda x: x * 4, numeros))  # esto ees compresion de lista
print(lista_cuadruple)


# Genera otra lista en el cubo de cada uno de los numeros de la lista
cubo = [elemento**3 for elemento in numeros]

cadena = ["hola " + "que hace" for _ in range(3)]


# Genera una lista de cadenas para cada elemento del rango de 5
saludos = ["hola" for _ in range(5)]
saludos2 = ["hola " + "que hace" for _ in range(3)]


# Elebora una serie de ejercicios unsando compresion de lista para practicar su uso.

# Ejercicio