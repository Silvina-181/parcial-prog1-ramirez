def calcular_promedio_general(promedios):
    """Calcula el promedio general del curso."""
    # Si no hay promedios, devolvemos 0 para evitar division por cero
    if len(promedios) == 0:
        return 0.0
        
    suma_total = 0
    
    # Recorremos la lista sumando cada promedio individual
    for i in range(len(promedios)):
        suma_total = suma_total + promedios[i]
        
    # Calculamos la division final
    promedio_general = suma_total / len(promedios)
    
    return promedio_general


def mejor_promedio(nombres, promedios):
    """Encuentra el nombre del alumno con el promedio mas alto."""
    indice_mejor = 0
    
    # Comparamos todos los promedios contra el de la posicion 'indice_mejor'
    for i in range(len(promedios)):
        if promedios[i] > promedios[indice_mejor]:
            indice_mejor = i  # Actualizamos solo la posicion si encontramos uno mayor
            
    return nombres[indice_mejor]


def peor_promedio(nombres, promedios):
    """Encuentra el nombre del alumno con el promedio mas bajo."""
    indice_peor = 0
    
    # Comparamos todos los promedios contra el de la posicion 'indice_peor'
    for i in range(len(promedios)):
        if promedios[i] < promedios[indice_peor]:
            indice_peor = i  # Actualizamos solo la posicion si encontramos uno menor
            
    return nombres[indice_peor]


def contar_condiciones(promedios):
    """Cuenta cuantos alumnos promocionan, aprueban o desaprueban."""
    cant_promociona = 0
    cant_aprueba = 0
    cant_desaprueba = 0
    
    for i in range(len(promedios)):
        if promedios[i] >= 6:
            cant_promociona = cant_promociona + 1
        elif promedios[i] >= 4:
            cant_aprueba = cant_aprueba + 1
        else:
            cant_desaprueba = cant_desaprueba + 1
            
    return cant_promociona, cant_aprueba, cant_desaprueba


def ordenar_ranking_burbuja(nombres, notas1, notas2, promedios):
    """Ordena las listas paralelas de mayor a menor promedio."""
    n = len(promedios)
    
    # El bucle externo controla cuantas pasadas hacemos sobre la lista
    for i in range(n - 1):
        # El bucle interno compara los elementos adyacentes
        for j in range(n - 1 - i):
            
            # Como queremos de mayor a menor, si el de la derecha es mas grande, intercambiamos
            if promedios[j] < promedios[j + 1]:
                
                # 1. Intercambiamos los promedios
                aux_promedio = promedios[j]
                promedios[j] = promedios[j + 1]
                promedios[j + 1] = aux_promedio
                
                # 2. Intercambiamos los nombres (obligatorio por ser listas paralelas)
                aux_nombre = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = aux_nombre
                
                # 3. Intercambiamos las notas del parcial 1
                aux_n1 = notas1[j]
                notas1[j] = notas1[j + 1]
                notas1[j + 1] = aux_n1
                
                # 4. Intercambiamos las notas del parcial 2
                aux_n2 = notas2[j]
                notas2[j] = notas2[j + 1]
                notas2[j + 1] = aux_n2


def contar_vocales(nombre):
    """Cuenta la cantidad de vocales que tiene un nombre."""
    contador = 0
    
    for i in range(len(nombre)):
        caracter = nombre[i]
        
        # Buscamos las vocales
        es_vocal = (caracter == "a" or caracter == "e" or caracter == "i" or 
                    caracter == "o" or caracter == "u" or caracter == "A" or 
                    caracter == "E" or caracter == "I" or caracter == "O" or 
                    caracter == "U" or caracter == "á" or caracter == "é" or 
                    caracter == "í" or caracter == "ó" or caracter == "ú")
        
        if es_vocal:
            contador = contador + 1
            
    return contador


def invertir_nombre(nombre):
    """Da vuelta el texto de un nombre de atras para adelante."""
    nombre_invertido = ""
    
    # Recorremos la cadena al reves, desde el ultimo indice hasta el 0
    for i in range(len(nombre) - 1, -1, -1):
        nombre_invertido = nombre_invertido + nombre[i]
        
    return nombre_invertido


def buscar_alumno_por_nombre(nombres, nombre_buscado):
    """Busca un alumno en la lista y dice si lo encontro y en que posicion."""
    encontrado = False
    posicion_encontrada = 0
    
    # Recorremos la lista para comparar nombre por nombre
    for i in range(len(nombres)):
        if nombres[i] == nombre_buscado:
            encontrado = True
            posicion_encontrada = i
            
    return encontrado, posicion_encontrada

