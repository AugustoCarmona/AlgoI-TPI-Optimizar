def tabla(diccionario):
    """ [Autor: Augusto Carmona]
        [Ayuda: Ajusta la informacion de cada linea a un maximo de 35 caracteres por nombre de funcion,
        2 caracteres por contador y 15 caracteres por nombre y le agrega divisores]
    """
    #ajusta los nombres de las funciones a un maximo de 35 caracteres
    ajuste_str(diccionario, 'FUNCION', 35)
    
    #ajuste de la informacion de contadores
    ajuste_int(diccionario, 'Parámetros')
    ajuste_int(diccionario, 'Líneas')
    ajuste_int(diccionario, 'Invocaciones')
    ajuste_int(diccionario, 'Returns')
    ajuste_int(diccionario, 'If/elif')
    ajuste_int(diccionario, 'For')
    ajuste_int(diccionario, 'While')
    ajuste_int(diccionario, 'Break')
    ajuste_int(diccionario, 'Exit')
    ajuste_int(diccionario, 'Coment')

    #ajusta la informacion del autor a un maximo de 15 caracteres
    ajuste_str(diccionario, 'Autor', 15)

    #imprime las divisiones
    index = 0
    for clave in diccionario:
        if index == 12:
            print("|", diccionario[clave], end="|\n")
        else:
            print("|", diccionario[clave], end=" ")
        index += 1
#--------------------------------------------------------------------------
def ajuste_str(diccionario, clave, max_carac):
    """ [Autor: Augusto Carmona]
        [Ayuda: Ajusta la cantidad de caracteres de la clave del diccionario según se ingrese]
    """
    cont_carac = 0
    for i in diccionario[clave]:
        cont_carac += 1
    
    if cont_carac < max_carac:
        agregar = max_carac - cont_carac
        diccionario[clave] = diccionario[clave] + " " * agregar
    else:
        diccionario[clave][0:max_carac]

#--------------------------------------------------------------------------
def ajuste_int(diccionario, clave):
    """ [Autor: Augusto Carmona]
        [Ayuda: recibe un diccionario y la clave que debe buscar en ese y convierte su int a str, y lo ajusta a 2 caracteres]
    """
    num = 0
    diccionario[clave] = str(diccionario[clave])

    for i in diccionario[clave]:
        num += 1
    if num < 3:
        agregar = 3 - num
        diccionario[clave] = diccionario[clave] + " " * agregar
    else:
        diccionario[clave][0:3]