# Parcial de Programación 1
# Proyecto NOTAFÁCIL - Instituto Horizonte

Este sistema permite registrar alumnos, calificaciones, calcular promedios, mostrar estadisticas.

# Estructura del Proyecto

El proyecto está dividido en tres módulos:

* main.py : Contiene el menú principal y la estructura `match-case` 
* validaciones.py : Contiene las funciones de control de datos para la cantidad de alumnos, notas de parciales, formato estricto de nombres y verificación de tipos de datos.
* procesamientos.py : Centraliza los promedios, máximos, mínimos, contadores, el ordenamiento burbuja clásico de listas paralelas y el manejo manual de cadenas.

# Funciones
* **Carga y Validación:** Registro de hasta 30 alumnos.
* **Estadísticas Automáticas:** Rendimiento general, mejores/peores promedios y recuento por condición (Promociona, Aprueba, Desaprueba).
* **Ranking Integrado:** Cuadro de honor ordenado de mayor a menor promedio mediante el algoritmo de ordenamiento burbuja.
* **Búsqueda Secuencial:** Localización inmediata de las notas de cualquier estudiante por su nombre.
* **Juegos con Cadenas:** Herramienta interactiva para contar vocales e invertir nombres de forma manual.

# Requisitos y Ejecución
El programa fue desarrollado en Python.
Para iniciar la aplicación, deberá tener instalado Python 3.10 o superior. Ejecutando el siguiente comando:

```bash
python main.py
```
