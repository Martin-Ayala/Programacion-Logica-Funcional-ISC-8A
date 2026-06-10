# ejercicio 2: ordenar tipo de cafe
# objetivo: ordenar distintos tipos de cafe.

"""Los grupos de VIII de ISC tienen cambios de humor y ahora cada grupo quiere un tipo de cafe:
    --cafe americano y
    --cafe de olla

Dato curioso: Los cambios

1. Crear una funcion preparar cade que no recibe parametros y devuelve una cadena que representa una taza de cade americano.
2. crea otra, esta funcion que devuelve una cadena que representa una taza de cafe de olla.
3. crea otra funcion ordenar cafe que acepta dos parametros: una funcion que prepara cafe y numero de  tazas.
4. Dentro de la funcion ordenar crea una lista que guarde las tazas de cafe.
5. Dentro de la funcion ordenar, aplica la iteracion a traves de la lista por compresion para llamar a la funcion preparar_cafe segun el numero_tazas proporcionado.
6. Finaliza en la funcion ordenar, devuelve la lista tazas_cafe.
7.crear una nueva variable cafe para el grupo A que recibe"""


def preparar_cafe_americano():
    return "cafe americano"


def preparar_cafe_olla():
    return "cafe de olla"


def ordenar_cafe(preparar_cafe_func, numero_tazas):
    tazas_cafe = [preparar_cafe_func() for _ in range(numero_tazas)]
    return tazas_cafe


cafe_grupo_a = ordenar_cafe(preparar_cafe_americano, 10)
cafe_grupo_b = ordenar_cafe(preparar_cafe_olla, 10)


print("Cafe para el grupo A:", cafe_grupo_a)
print("Cafe para el grupo B:", cafe_grupo_b)