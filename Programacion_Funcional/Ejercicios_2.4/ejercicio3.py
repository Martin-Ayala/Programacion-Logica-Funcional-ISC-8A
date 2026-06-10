# Ejercicio 3: Inflar globos
# Objetivo: Crea un programa que simule la inflada de globos 🎈 para una fiesta, de acuerdo al número de invitados que asistirán.
'''
1.- Define una función llamada inflar_globo que no reciba parámetros
    y devuelva el emoji de globo "🎈".
2.- Crea esta misma función usando lambda y asigna el resultado a la variable inflar_globo_lambda.
3.- crea una lista de globos usando la función lambda y una comprensión de listas, para el número de invitados que se ingresen por el usuario.  
2.- Define una función llamada preparar_globos que reciba un argumento
    numero_invitados (entero).
    Dentro de la función:
    -- Usa una comprensión de listas para llamar a inflar_globo()
       tantas veces como indique numero_invitados.
    -- Devuelve esa lista.
3.- Llama a preparar_globos solicitando al usuario ingresar el número
    de invitados a la fiesta y almacena el resultado en una variable globos_fiesta.
4.- Muestra en pantalla el contenido de globos_fiesta,
    que será una lista con varios emojis "🎈".
Ejemplo de salida:
    ¿Cuántos invitados van a la fiesta? 3
    ['🎈', '🎈', '🎈']
'''    
#1
def inflar_globo():
    return "🎈"

#2
inflar_globo_lambda = lambda: "🎈"

#3
def preparar_globos(numero_invitados):
    return [inflar_globo() for _ in range(numero_invitados)]

#4
numero_invitados = int(input("¿Cuántos invitados van a la fiesta? "))
globos_fiesta = preparar_globos(numero_invitados)
print(globos_fiesta)