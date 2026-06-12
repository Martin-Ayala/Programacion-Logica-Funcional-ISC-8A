# Sistema Experto de Orientación Vocacional

**Actividad:** AA 3.2 Sistema experto (Tema 3)  
**Institución:** TecNM Campus Felipe Carrillo Puerto  
**Autores:** Martin Adrian Ayala Uc y Fabian Kinil Adame

## Descripción del Proyecto
Este proyecto es un sistema experto diseñado para recomendar una carrera ideal a los estudiantes de nuevo ingreso del Tecnológico. Evalúa los perfiles para las carreras de: Sistemas Computacionales, Ciencia de Datos, Administración, Industrial, Alimentarias, Desarrollo Comunitario y Gestión Empresarial.

El sistema integra dos paradigmas de programación:
1. **Paradigma Lógico (Prolog):** Actúa como el motor de inferencia, almacenando la base de conocimientos y las reglas lógicas que relacionan intereses y habilidades con las carreras.
2. **Paradigma Funcional (Python):** Funciona como el controlador de la aplicación. Aplica inmutabilidad, recursión y funciones de orden superior (`map`) para procesar el cuestionario interactivo y comunicarse de forma segura con Prolog.

## Requisitos Previos
* Python 3.x
* SWI-Prolog instalado y configurado en las variables de entorno del sistema (PATH).

## Instalación y Ejecución

1. Clonar el repositorio en tu máquina local.
2. Abrir una terminal en la carpeta raíz del proyecto.
3. Instalar la dependencia necesaria para levantar el servidor de Prolog (`swiplserver`):
   ```bash
   pip install -r requirements.txt