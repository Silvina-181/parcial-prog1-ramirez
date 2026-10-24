""""Módulo de validaciones para NOTAFÁCIL"""


def validar_cantidad_alumnos(cantidad):
    """
    Verifica si la cantidad de alumnos esta entre 1 y 30 inclusive.
    """
    es_valido = 1 <= cantidad <= 30
    return es_valido


def validar_nota(nota):
    """
    La nota válida debe ser entre 0 y 10 inclusive.
    """
    es_valida = 0 <= nota <= 10
    return es_valida


def validar_nombre(nombre):
    """
    Validar el nombre del alumno. 
    Debe contener no menos de 5 caracteres y solo letras o espacios.
    """
    if len(nombre) < 5:
        return False
        
    for i in range(len(nombre)):
        caracter = nombre[i]
        
        es_letra_min = "a" <= caracter <= "z" or caracter == "ñ"
        es_letra_may = "A" <= caracter <= "Z" or caracter == "Ñ"
        es_espacio = caracter == " "
        
        if not (es_letra_min or es_letra_may or es_espacio):
            return False  
            
    return True

def es_numero_entero(texto):
    """Verifica si una cadena de texto contiene solo numeros enteros."""
    if len(texto) == 0:
        return False
        
    for i in range(len(texto)):
        caracter = texto[i]
        # Verificamos si NO es un numero entre 0 y 9
        if not ("0" <= caracter <= "9"):
            return False
            
    return True

