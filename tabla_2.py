#este modulo genera una taba para consulta.py con el nombre de las funciones del programa a analizar
def tabla(lista_funciones):
    """ [Autor: Augusto Carmona y Gastón Mondín]
        [Ayuda: Imprime una tabla en base a la lista recibida.]
    """
    if len(lista_funciones) % 5 == 0:
        filas = int(len(lista_funciones) / 5)
    else:
        filas = int(len(lista_funciones) / 5 + 1)
    
    caracteres = 0
    
    for funcion in lista_funciones:
        if len(funcion) > caracteres:
            caracteres = len(funcion)
    caracteres += 4

    linea = " "
    for j in range(5):
        linea += "_" * (caracteres+3)
    print(linea)
    
    index = 0
    
    for i in range(filas):
        
        linea = "|"
        for j in range(5):
            if index >= len(lista_funciones):
                linea += " " * (caracteres+2) + "|"
            else:
                linea += " " + lista_funciones[index] + " " * (caracteres-len(lista_funciones[index])+1) + "|"
            index+=1
        print(linea)
        
        linea = "|"
        for j in range(5):
            linea += "_" * (caracteres+2) + "|"
        print(linea)