from os import system
if system("clear") != 0: system("cls")

"""
El comando type() devuelve el tipo de un objeto en Python
"""
print("int:")
print(type(10)) #Numero entero positivo
print(type(0)) #El 0 tambien es un entero
print(type(-5)) #Numero entero negativo
print(type(72384247233484874838944833834)) #Python permite enteros de gran tamaño

print("float:")
print(type(3.14))
print(type(1.0))
print(type(1e3))

print("complex:")
print(type(1 + 2j))

print("str:")
print(type("Hola"))
print(type(""))
print(type("123"))
print(type("""
Multilinea
""")) #String que abarca varias lineas usando triple comillas

print("bool:")
print(type(True))
print(type(False))
print(type(1 < 2))

print("NoneType:")
print(type(None))