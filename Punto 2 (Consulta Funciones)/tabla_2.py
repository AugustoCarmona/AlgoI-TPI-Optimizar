def tabla(lista_funciones):
    """ [Autor: Augusto Carmona, Gaston Mondin]
        [Ayuda: Iimprime una tabla en base a las lista recibida]
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
    print('\t\t', linea)
    
    index = 0
    
    for i in range(filas):
        
        linea = "|"
        for j in range(5):
            if index >= len(lista_funciones):
                linea += " " * (caracteres+2) + "|"
            else:
                linea += " " + lista_funciones[index] + " " * (caracteres-len(lista_funciones[index])+1) + "|"
            index+=1
        print('\t\t', linea)
        
        linea = "|"
        for j in range(5):
            linea += "_" * (caracteres+2) + "|"
        print('\t\t', linea)