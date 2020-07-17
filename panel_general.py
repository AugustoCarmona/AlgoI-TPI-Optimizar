"""
    ** Panel General de Funciones **
    Este modulo es el encargado de mostrar una tabla con la informacion de las funciones
    internas del programa que se esté analizando (parametros, lineas, invocaciones, returns
    if/elif, for, while, break, exit, comment, ayuda y autor).
    Tambien debe generar el archivo panel_general.csv con la informacion previamente impresa
    en pantalla.
"""
#############################################################################################
# Ejemplos de contadores:
# el problema de las siguientes funciones es que cuentan TODOS los parametros del codigo y no solo los incluidos en la funcion

# Contador de lineas de codigo
def contador_lineas():
    with open("lib_matematica.py", "r") as modulo:
        cont_lineas = 0
        for linea in modulo:
            if len(linea) > 2:
                cont_lineas += 1
        return cont_lineas

# Contador de puntos de salida
def contador_returns(): 
    with open("lib_matematica.py", "r") as modulo:
        cont_return = 0
        for linea in modulo:
            if "return" in linea:
                cont_return += 1
    return cont_return

# Contador de if
def contador_if(): 
    with open("lib_matematica.py", "r") as modulo:
        cont_if = 0
        for linea in modulo:
            if "if" or "elif" in linea:
                cont_if += 1
    return cont_if

# Contador de for
def contador_for(): 
    with open("lib_matematica.py", "r") as modulo:
        cont_for = 0
        for linea in modulo:
            if "for" in linea:
                cont_for += 1
    return cont_for

# Contador de while
def contador_while(): 
    with open("lib_matematica.py", "r") as modulo:
        cont_while = 0
        for linea in modulo:
            if "while" in linea:
                cont_while += 1
    return cont_while

# Contador de break
def contador_break(): 
    with open("lib_matematica.py", "r") as modulo:
        cont_break = 0
        for linea in modulo:
            if "break" in linea:
                cont_break += 1
    return cont_break

# Contador de exit
def contador_exit(): 
    with open("lib_matematica.py", "r") as modulo:
        cont_exit = 0
        for linea in modulo:
            if "exit" in linea:
                cont_exit += 1
    return cont_exit

# Contador de comentarios
def contador_coment():
    with open("lib_matematica.py", "r") as modulo:
        cont_coment = 0
        for linea in modulo:
            if "#" in linea:
                cont_coment += 1
    return cont_coment    

#############################################################################################

#-------------------------------
def extractor_de_funciones(): # Este codigo esa ok (creo)
    """ [Autor: Augusto Carmona Perez]
        [Ayuda: Identifica funciones en un codigo, extrae su nombre y las inserta como clave
        en un diccionario con una lista asociada. También cuenta la cantidad de parametros en
        cada una de estas funciones y lo ingresa como el primer valor de la lista]
    """
    with open("lib_matematica.py", "r") as modulo:
        
        funciones = {}
        for linea in modulo:
            if "def" in linea:
                nombre_funcion = linea[4:linea.index("(")]
                parametros = linea.count(",") + 1
                funciones[nombre_funcion] = [parametros]
                
    return funciones

#-------------MAIN-------------#
print("Diccionario: ", extractor_de_funciones())
# parametros [check]
print("Cantidad de Lineas de Codigo: ", contador_lineas())
print("Cantidad de Returns: ", contador_returns())
print("Cantidad de If/Elif: ", contador_if())
print("Cantidad de Fors: ", contador_for())
print("Cantidad de Whiles: ", contador_while())
print("Cantidad de Breaks: ", contador_break())
print("Cantidad de Exits: ", contador_exit())
print("Cantidad de Comentarios: ", contador_coment())
# Ayuda (por si o por no)
# Autor (firma)