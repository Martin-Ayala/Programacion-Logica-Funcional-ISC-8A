# =============================================================================
#  ACTIVIDAD PRÁCTICA INTEGRADORA
#  Sistema de pedidos: Comedor Escolar
# =============================================================================
#  Programación Funcional en Python — Nivel Básico
#  Temas integrados:
#    ✅ Funciones simples y de primera clase  
#    ✅ Comprensión de listas                 
#    ✅ Funciones de orden superior           
#    ✅ Callbacks                             
#    ✅ Funciones lambda + map()              
#    ✅ Lógica condicional dentro de funcs.   
#    ✅ Entrada del usuario                   
# =============================================================================


# ─────────────────────────────────────────────────────────────────────────────
#  Sección 1 — INVESTIGA
# ─────────────────────────────────────────────────────────────────────────────
# Antes de comenzar a codificar, investiga y responde en comentarios:
#
# 1. ¿Qué es una función de primera clase en Python?
#    R: Son funciones que son tratadas como cualquier otra variable o tipo de dato. 
#       Puedes asignarlas a una variable, guardarlas en estructuras de datos 
#       (como listas o diccionarios), pasarlas como argumentos a otras funciones 
#       o retornarlas como resultado de otra función.
#
# 2. ¿Cuál es la diferencia entre una función de orden superior y un callback?
#    R: Una función de orden superior es la función que recibe a otra función como 
#       argumento (o que retorna una función). Un callback es precisamente esa función 
#       que estás pasando como argumento, la cual será ejecutada ("llamada de vuelta") 
#       dentro de la función de orden superior.
#
# 3. ¿Cuándo conviene usar comprensión de listas en lugar de un ciclo for?
#    R: Conviene usarlas cuando el objetivo principal es crear una nueva lista 
#       transformando o filtrando elementos de un iterable de forma sencilla. 
#       Hacen el código más conciso, legible y suelen ser ligeramente más rápidas en ejecución.
#
# 4. ¿Qué hace map() y cómo se relaciona con lambda?
#    R: map() recibe una función y un iterable, y aplica esa función a cada elemento del
#       iterable, devolviendo un nuevo objeto (map object) con los resultados. 
#       Se relaciona con lambda porque es muy común usar una función anónima (lambda) 
#       como el primer argumento de map() para hacer operaciones rápidas de una sola 
#       línea sin tener que definir una función con "def".
#
#
# 5. ¿Qué ventaja ofrece pasar una función como argumento a otra función?
#    R: Aporta gran flexibilidad, modularidad y reutilización de código. 
#       Permite separar la lógica principal de un proceso (el "cómo" se recorren los datos)
#       del comportamiento específico que se quiere aplicar en ese momento (el "qué" se hace con cada dato),
#       facilitando el mantenimiento y evitando repetir código.
# ─────────────────────────────────────────────────────────────────────────────


# ─────────────────────────────────────────────────────────────────────────────
# Sección 2 — PLANEA
# ─────────────────────────────────────────────────────────────────────────────
# Lee el siguiente escenario y diseña tu solución ANTES de codificar.
#
# ESCENARIO
# La cooperativa escolar ofrece tres productos en su menú:
#   🍕 Pizza  |  🥤 Agua fresca  |  🫔 Tamal
#
# El sistema debe:
#   A) Preparar cualquier producto usando una función dedicada por producto.
#   B) Tomar la orden de un grupo: recibir la FUNCIÓN del producto y la
#      CANTIDAD solicitada, y devolver una lista con todas las porciones.
#   C) Calcular el precio total aplicando el precio unitario a cada porción  
#      usando map() y una función lambda.
#   D) Aplicar una PROMOCIÓN: si el pedido es de 3 o más porciones,
#      agregar "🎁 postre gratis" a la orden.
#   E) Solicitar al usuario cuántas porciones desea de cada producto y
#      mostrar el resumen completo del pedido.
#
# Antes de codificar respone o describe:
#      - ¿Qué funciones necesitas definir?
#        R: tres funciones básicas (callbacks) para preparar cada producto 
#           (ej. preparar_pizza(), preparar_agua(), preparar_tamal()). También 
#           necesitaré una función principal para gestionar la solicitud (ej. tomar_orden()).
#
#      - ¿Cuál de ellas es de orden superior? ¿Por qué?
#        R: La función tomar_orden() será la de orden superior. La razón es que 
#           recibirá como parámetro (callback) la función de preparación específica 
#           del producto que el usuario haya seleccionado.
#
#      - ¿Dónde usarás comprensión de listas?
#        R: Dentro de la función tomar_orden(). La usaré para generar la lista 
#           final de porciones, ejecutando el callback del producto la cantidad 
#           de veces que el usuario haya indicado.
#
#      - ¿Dónde usarás lambda + map()?
#        R: En la sección donde se calcula el costo. Usaré map() y una lambda 
#           para transformar la lista de porciones en una lista de precios unitarios, 
#           para que después sea muy fácil sumarlos todos y obtener el total.
# ─────────────────────────────────────────────────────────────────────────────


# ─────────────────────────────────────────────────────────────────────────────
# Sección 3 — CODIFICA
# ─────────────────────────────────────────────────────────────────────────────
# Completa cada paso en el orden indicado.
# Puedes apoyarte en los archivos del carpeta para recordar la sintaxis.


# ── PASO 1 ──────────────────────────────────────────────────────────────────
# Define tres funciones simples, sin parámetros, que devuelvan el nombre
# (y emoji) del producto correspondiente. Son funciones de primera clase.
#
# Referencia: ejercicio1_cafe.py → preparar_cafe()
#             desafio2_alimentos.py → preparar_pizza(), preparar_hamburguesa()

def preparar_pizza():
    return "🍕 pizza"

def preparar_agua():
    return "🥤 agua fresca"

def preparar_tamal():
    return "🫔 tamal"


# ── PASO 2 ──────────────────────────────────────────────────────────────────
# Define la función calcular_promocion(cantidad).
# Si cantidad >= 3, devuelve el string "🎁 postre gratis".
# En caso contrario, devuelve un string vacío "".
#
# Referencia: desafio2_alimentos.py → calcular_bonus()

def calcular_promocion(cantidad):
    if cantidad >= 3:
        return "🎁 postre gratis"
    else:
        return ""


# ── PASO 3 ──────────────────────────────────────────────────────────────────
# Define la función tomar_orden(preparar_alimento, cantidad, precio_unitario).
#
# Esta función es de ORDEN SUPERIOR porque recibe otra función como argumento.
# preparar_alimento → función que se usará como callback (pizza, agua o tamal)
# cantidad          → número de porciones
# precio_unitario   → costo por porción (número)
#
# Dentro de la función debes:
#   a) Usar COMPRENSIÓN DE LISTAS para generar la lista de porciones,
#      llamando a preparar_alimento() en cada iteración.
#   b) Usar map() con una función LAMBDA para calcular el precio de cada
#      porción: cada elemento de la lista recibe el precio_unitario.
#      Convierte el resultado en lista con list().
#   c) Llamar a calcular_promocion(cantidad) y guardar el resultado.
#   d) Devolver una tupla: (porciones, precios, promocion)
#
# Referencia: ejercicio2_tipoCafe.py → ordenar_cafe()
#             desafio2_alimentos.py  → ordenar_alimento()
#             compresionListas.py    → map + lambda
#             funciones.py           → callbacks y orden superior

def tomar_orden(preparar_alimento, cantidad, precio_unitario):
    # a) Comprensión de listas
    porciones = [preparar_alimento() for _ in range(cantidad)]

    # b) map() + lambda para precios
    precios = list(map(lambda porcion: precio_unitario, porciones))

    # c) Promoción
    promocion = calcular_promocion(cantidad)

    # d) Devuelve los tres valores
    return porciones, precios, promocion


# ── PASO 4 ──────────────────────────────────────────────────────────────────
# Solicita al usuario la cantidad de cada producto y toma las órdenes.
# Almacena cada resultado en una variable distinta.
#
# Referencia: desafio1_hotcake.py → input() + int()

cantidad_pizzas  = int(input("¿Cuántas pizzas deseas ordenar? "))
cantidad_aguas   = int(input("¿Cuántas aguas frescas deseas ordenar? "))
cantidad_tamales = int(input("¿Cuántos tamales deseas ordenar? "))

# Llama a tomar_orden para cada producto.
# Precios sugeridos: pizza=25, agua=10, tamal=15
orden_pizza  = tomar_orden(preparar_pizza,  cantidad_pizzas,  25)
orden_agua   = tomar_orden(preparar_agua,   cantidad_aguas,   10)
orden_tamal  = tomar_orden(preparar_tamal,  cantidad_tamales, 15)


# ── PASO 5 ──────────────────────────────────────────────────────────────────
# Muestra el resumen del pedido.
# Para cada orden imprime: porciones, precios y promoción (si aplica).
#
# Ejemplo de salida esperada:
#   🍕 PIZZAS   → ['🍕 pizza', '🍕 pizza', '🍕 pizza']
#   💲 Precios  → [25, 25, 25]
#   🎁 Promo    → 🎁 postre gratis
#
# Referencia: solucionAlimentos.py → print de tupla

print("\n========== RESUMEN DEL PEDIDO ==========")
# Desempaqueta cada tupla en sus tres partes y muéstralas
porciones_pizza,  precios_pizza,  promo_pizza  = orden_pizza
porciones_agua,   precios_agua,   promo_agua   = orden_agua
porciones_tamal,  precios_tamal,  promo_tamal  = orden_tamal

print(f"\n🍕 PIZZAS   → {porciones_pizza}")
print(f"💲 Precios  → {precios_pizza}")
print(f"🎁 Promo    → {promo_pizza if promo_pizza else 'sin promoción'}")

print(f"\n🥤 AGUAS    → {porciones_agua}")
print(f"💲 Precios  → {precios_agua}")
print(f"🎁 Promo    → {promo_agua if promo_agua else 'sin promoción'}")

print(f"\n🫔 TAMALES  → {porciones_tamal}")
print(f"💲 Precios  → {precios_tamal}")
print(f"🎁 Promo    → {promo_tamal if promo_tamal else 'sin promoción'}")

print("\n========================================")


# ─────────────────────────────────────────────────────────────────────────────
# Sección 4 — PRUEBA
# ─────────────────────────────────────────────────────────────────────────────
# Ejecuta el programa con los siguientes casos y verifica los resultados.
#
# CASO 1 — Sin promoción (cantidades menores a 3):
#   Pizzas: 2  | Aguas: 1  | Tamales: 2
#   Esperado: ninguna orden muestra "🎁 postre gratis"
#
# CASO 2 — Con promoción en todas las órdenes:
#   Pizzas: 3  | Aguas: 5  | Tamales: 4
#   Esperado: las tres órdenes muestran "🎁 postre gratis"
#
# CASO 3 — Promoción mixta:
#   Pizzas: 1  | Aguas: 3  | Tamales: 2
#   Esperado: solo la orden de aguas muestra "🎁 postre gratis"
#
# CASO 4 — Verificación de precios con map() + lambda:
#   Pide 3 pizzas a $25 c/u → la lista de precios debe ser [25, 25, 25]
#   Pide 4 tamales a $15 c/u → la lista de precios debe ser [15, 15, 15, 15]
#
# Registra:
#   - ¿El resultado coincide con lo esperado? ✅ Si coincide.
#   - Si no coincide, ¿en qué función está el error? Ninguno, no hay errores.
#   - ¿Qué cambiarías para corregirlo? Nada, el código funciona correctamente.
# ─────────────────────────────────────────────────────────────────────────────


# ─────────────────────────────────────────────────────────────────────────────
# Desafío extra (opcional)
# ─────────────────────────────────────────────────────────────────────────────
# Si terminaste antes y quieres ir más allá:
#
# 1. Usa sum() y map() + lambda para calcular el TOTAL a pagar de cada orden.
# 2. Crea una función elegir_producto(nombre) que sea de ORDEN SUPERIOR:
#    recibe un string ("pizza", "agua" o "tamal") y DEVUELVE la función
#    de preparación correspondiente (sin ejecutarla).
#    Referencia: funciones.py → elegir_operacion()
# 3. Usa la función del punto 2 para reemplazar los argumentos directos en
#    las llamadas a tomar_orden().
# ─────────────────────────────────────────────────────────────────────────────
print("\n\n--- EJECUCIÓN DEL DESAFÍO EXTRA ---")

# PUNTO 2: Función de ORDEN SUPERIOR que devuelve una función de preparación
def elegir_producto(nombre):
    nombre = nombre.lower()
    if nombre == "pizza":
        return preparar_pizza
    elif nombre == "agua":
        return preparar_agua
    elif nombre == "tamal":
        return preparar_tamal

# PUNTO 3: Reemplazamos los argumentos directos usando elegir_producto()
# Haremos una orden de prueba (ejemplo: 4 tamales a $15)
orden_prueba = tomar_orden(elegir_producto("tamal"), 4, 15)

# Desempaquetamos la tupla resultante
porciones_prueba, precios_prueba, promo_prueba = orden_prueba

# PUNTO 1: Calculamos el TOTAL usando sum(), map() y lambda
total_pagar = sum(map(lambda precio: precio, precios_prueba))

# Mostramos el resultado del desafío
print(f"🫔 Orden de prueba: {porciones_prueba}")
print(f"💲 Precios: {precios_prueba} | TOTAL A PAGAR: ${total_pagar}")
print(f"🎁 Promoción: {promo_prueba if promo_prueba else 'sin promoción'}")
print("-----------------------------------")