#Este modulo solo requiere una lista anidada
#--------------------------------------------------------------------------------------------------------------------------#
def generador(lista_anidada):
    """ [Autor: Augusto Carmona]
        [Ayuda: Recibe una lista anidada, identifica la palabra mas larga de la lista
        para dar formato a la tabla por medio de la funcion ajustar() e imprime las
        listas horizontalmente]
    """
    max_caracteres = 0 #identifica la palabra con mas caracteres
    for lista in lista_anidada:
        for elemento in lista:
            if len(elemento) > max_caracteres:
                max_caracteres = len(elemento) * 2
    
    lista_ajustada = [] #ajusta el largo de cada lista y lo adihere a una nueva lista anidada y ajustada
    for lista in lista_anidada:
        renglon = ajustar(lista, max_caracteres)
        lista_ajustada.append(renglon)
    
    cant_caracteres = " || ".join(lista_ajustada[0])
    caracteres_renglon = len(cant_caracteres)
    
    print("\n\t", "-" * caracteres_renglon, end = "\n")
    for i in lista_ajustada: #enflila cada lista interna de la nueva lista ajustada
        for j in i:
            print("\t|{}|".format(j), end = "")
        print("\n\t", "-" * caracteres_renglon, end = "\n") #separa las filas
    
#----------------
def ajustar(fila, max_caracteres):
    """ [Autor: Augusto Carmona]
        [Ayuda: da a cada elemento de la lista que se ingrese el mismo largo de max_caracteres
        (que es la cantidad de caracteres de la palabra mas larga de la lista anidada que llama
        a esta funcion)]
    """
    renglon = []
    for i in fila: #da a cada elemento de la lista el largo (en caracteres) de la palabra mas larga
        if len(i) == max_caracteres:
            renglon.append(i)
        elif len(i) < max_caracteres:
            adicion = max_caracteres - len(i)
            i = i + " " * adicion
            renglon.append(i)
    
    return renglon

#--MAIN--------------------------------------------------#
def tabla(lista_anidada):
    """ [Autor: Augusto Carmona]
        [Ayuda: recibe una lista anidada y la envia al generador() para que se la imprima en formato de tabla]
    """
    generador(lista_anidada)