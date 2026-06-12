# Tupla inmutable con las preguntas y los identificadores de interés
PREGUNTAS = (
    {"texto": "¿Te gusta programar y desarrollar software? (s/n): ", "interes": "programacion"},
    {"texto": "¿Te interesa el diseño de redes y conectividad de computadoras? (s/n): ", "interes": "redes"},
    {"texto": "¿Te apasiona el análisis de grandes volúmenes de datos? (s/n): ", "interes": "analisis_datos"},
    {"texto": "¿Te llaman la atención las matemáticas avanzadas y la estadística? (s/n): ", "interes": "matematicas"},
    {"texto": "¿Te gustaría liderar equipos y administrar finanzas? (s/n): ", "interes": "liderazgo"},
    {"texto": "¿Te interesa la optimización de procesos de producción y logística? (s/n): ", "interes": "optimizacion"},
    {"texto": "¿Te gusta la química, biología y el control de calidad de alimentos? (s/n): ", "interes": "quimica"},
    {"texto": "¿Te motiva desarrollar proyectos de impacto social y sostenibilidad? (s/n): ", "interes": "gestion_social"},
    {"texto": "¿Te interesa el mundo de los negocios y la innovación empresarial? (s/n): ", "interes": "negocios"}
)

def recopilar_intereses(preguntas, indice=0, intereses_acumulados=()):
    """
    Función recursiva pura que reemplaza los bucles tradicionales.
    Mantiene la inmutabilidad creando nuevas tuplas en cada iteración.
    """
    if indice >= len(preguntas):
        return intereses_acumulados
    
    pregunta = preguntas[indice]
    respuesta = input(pregunta["texto"]).strip().lower()
    
    # Si la respuesta es 's', se añade el interés a una nueva tupla
    nuevos_intereses = intereses_acumulados + (pregunta["interes"],) if respuesta == 's' else intereses_acumulados
    
    # Llamada recursiva con el siguiente índice
    return recopilar_intereses(preguntas, indice + 1, nuevos_intereses)