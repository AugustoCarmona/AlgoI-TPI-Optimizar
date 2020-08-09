def tabla(lista_funciones):
    """ [Autor: Augusto Carmona y Gastón Mondín]
        [Ayuda: Imprime una tabla en base a la lista recibida.]
    """
    #ajusta el largo de las filas
    if len(lista_funciones) % 5 == 0:
        filas = int(len(lista_funciones) / 5)
    else:
        filas = int(len(lista_funciones) / 5 + 1)
    
    #busca la funcion con mas caracteres y le da un espacio extra
    caracteres = 0
    
    for funcion in lista_funciones:
        if len(funcion) > caracteres:
            caracteres = len(funcion)
    caracteres += 4

    #debo definir que es linea
    linea = " "
    for j in range(5):
        linea += "_" + "_" * caracteres + "_ "
    print(linea)
    
    index = 0
    
    #y esto no se que es
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