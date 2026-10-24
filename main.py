"""Módulo principal de NOTAFÁCIL.

Maneja el menú de la consola y coordina el flujo de los datos del instituto.
"""

from validaciones import validar_cantidad_alumnos, validar_nota, validar_nombre, es_numero_entero
from procesamiento import (
    calcular_promedio_general,
    mejor_promedio,
    peor_promedio,
    contar_condiciones,
    ordenar_ranking_burbuja,
    buscar_alumno_por_nombre,
    contar_vocales,
    invertir_nombre
)


# 1. Listas paralelas vacías para almacenar la información
nombres = []
notas1 = []
notas2 = []
promedios = []

# Variable para controlar el menú
ejecutando = True

while ejecutando:
    # 2. Opciones del menú 
    print("\n===== NOTAFÁCIL =====")
    print("1. Cargar alumnos")
    print("2. Mostrar listado")
    print("3. Mostrar estadísticas")
    print("4. Ver ranking (ordenado)")
    print("5. Buscar alumno")
    print("6. Juegos con un nombre")
    print("0. Salir")
    
    opcion = input("\nSeleccione una opción: ")
    
    # 3. Estructura match-case para controlar las opciones
    match opcion:
        case "1":
            print("\n--- Opción 1: Cargar alumnos ---")

        # Pedimos y validamos la cantidad de alumnos
            entrada = input("Ingrese la cantidad de alumnos a cargar (1-30): ")
            
            while not es_numero_entero(entrada) or not validar_cantidad_alumnos(int(entrada)):
                print("Error: Debe ingresar un número entero válido entre 1 y 30.")
                entrada = input("Intente nuevamente: ")
            
            cantidad = int(entrada)
            
            # Bucle para cargar cada alumno
            for i in range(cantidad):
                print(f"\n--- Alumno {i + 1} de {cantidad} ---")
                
                # Validamos el Nombre
                nombre = input("Nombre completo: ")
                while not validar_nombre(nombre):
                    print("Error: Nombre inválido (mínimo 5 letras, sin números).")
                    nombre = input("Intente nuevamente: ")
                
                # Validamos la Nota 1
                n1 = int(input("Nota del Parcial 1 (0-10): "))
                while not validar_nota(n1):
                    print("Error: La nota debe estar entre 0 y 10.")
                    n1 = int(input("Intente nuevamente: "))
                
                # Validamos la Nota 2
                n2 = int(input("Nota del Parcial 2 (0-10): "))
                while not validar_nota(n2):
                    print("Error: La nota debe estar entre 0 y 10.")
                    n2 = int(input("Intente nuevamente: "))
                
                # Calculamos el promedio
                promedio_alumno = (n1 + n2) / 2
                
                # Guardamos los datos en las listas
                nombres = nombres + [nombre]
                notas1 = notas1 + [n1]
                notas2 = notas2 + [n2]
                promedios = promedios + [promedio_alumno]
                
            print("\n¡Carga de alumnos finalizada con éxito!")    
    
        case "2":
            print("\n--- Opción 2: Mostrar listado ---")
            
            # 1. Si la lista está vacía:
            if len(nombres) == 0:
                print("No hay alumnos cargados en el sistema.")
            else:
                print("\nListado completo de alumnos:")
                print("--------------------------------------------------")
                
                # 2. Recorremos todas las listas usando el mismo índice 'i'
                for i in range(len(nombres)):
                    print(f"Alumno: {nombres[i]}")
                    print(f"  - Parcial 1: {notas1[i]}")
                    print(f"  - Parcial 2: {notas2[i]}")
                    print(f"  - Promedio:  {promedios[i]}")
                    print("--------------------------------------------------")
 
        case "3":
            print("\n--- Opción 3: Mostrar estadísticas ---")
            if len(nombres) == 0:
                print("No hay alumnos cargados. Use la Opción 1 primero.")
            else:
                # 1. Llamamos a las funciones de procesamiento pasándole los datos
                prom_general = calcular_promedio_general(promedios)
                alumno_mejor = mejor_promedio(nombres, promedios)
                alumno_peor = peor_promedio(nombres, promedios)
                
                # Desempaquetamos los tres contadores que devuelve la función
                promocionan, aprueban, desaprueban = contar_condiciones(promedios)
                
                # 2. Mostramos todos los resultados en la pantalla de Laura
                print(f"\nPromedio general del curso: {prom_general:.2f}")
                print(f"Mejor promedio del curso:   {alumno_mejor}")
                print(f"Peor promedio del curso:    {alumno_peor}")
                print("--------------------------------------------------")
                print("Cantidad de alumnos por condición:")
                print(f"  - Promocionan: {promocionan}")
                print(f"  - Aprueban:    {aprueban}")
                print(f"  - Desaprueban: {desaprueban}")

        case "4":
            print("\n--- Opción 4: Ver ranking (ordenado de mejor a peor) ---")
            if len(nombres) == 0:
                print("No hay alumnos cargados. Use la Opción 1 primero.")
            else:
                # 1. Llamamos a la burbuja para que ordene todas las listas juntas
                ordenar_ranking_burbuja(nombres, notas1, notas2, promedios)
                
                # 2. Mostramos el listado ya ordenado usando la misma logica del Case 2
                print("\nCUADRO DE HONOR (Ranking):")
                print("--------------------------------------------------")
                for i in range(len(nombres)):
                    print(f"Puesto {i + 1}: {nombres[i]} - Promedio: {promedios[i]:.2f}")
                print("--------------------------------------------------")
            
        case "5":
            print("\n--- Opción 5: Buscar alumno ---")
            if len(nombres) == 0:
                print("No hay alumnos cargados. Use la Opción 1 primero.")
            else:
                buscado = input("Ingrese el nombre del alumno a buscar: ")
                
                # Llamamos a tu funcion con bandera de procesamiento.py
                existe, pos = buscar_alumno_por_nombre(nombres, buscado)
                
                # Aprovechamos tu idea de mostrar los datos pero los imprimimos aca en el main
                if existe:
                    print("\n===== ALUMNO ENCONTRADO =====")
                    print(f"Nombre: {nombres[pos]}")
                    print(f"Nota Parcial 1: {notas1[pos]}")
                    print(f"Nota Parcial 2: {notas2[pos]}")
                    print(f"Promedio: {promedios[pos]:.2f}")
                else:
                    print(f"\nEl alumno '{buscado}' no se encuentra en el listado.")
            
        case "6":
            print("\n--- Opción 6: Juegos con un nombre ---")
            if len(nombres) == 0:
                print("No hay alumnos cargados. Use la Opción 1 primero.")
            else:
                nombre_juego = input("Ingrese el nombre para jugar: ")
                
                # Llamamos a las dos funciones de juegos de procesamiento.py
                vocal_cant = contar_vocales(nombre_juego)
                invertido = invertir_nombre(nombre_juego)
                
                # Mostramos los resultados divertidos para Laura
                print(f"\nResultados para '{nombre_juego}':")
                print(f"  - Cantidad de vocales: {vocal_cant}")
                print(f"  - Nombre invertido:    {invertido}")

            
        case "0":
            print("\n¡Gracias por usar NotaFácil! Saliendo del programa...")
            ejecutando = False
            
        case _:
            print("\nError: Opción inválida. Intente nuevamente.")

