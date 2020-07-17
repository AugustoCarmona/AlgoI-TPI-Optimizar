lista = ["hola", "chau", "como", "estas", "bien", 
        "hola", "chau", "como", "estas", "bien", 
        "hola", "chau", "como", "estas", "bien", 
        "casi"]

def obtener_tabla_para_imprimir(lista_funciones):
    '''[Autor: Ivan Litteri]
    [Ayuda: A esta funcion le llega por parametro una lista con los nombres de todas las funciones
    y concatena a estos nombres a una cadena que llamo tabla, con un formato como el que se pide en 
    la consigna (5 columnas, x filas)]'''
    
    #Creo una cadena vacia, para llenar luego con los nombres de las funciones
    tabla = ""
    #Recorro los indices de la lista
    for i in range(len(lista)):
        #Si llegue a una columna 5 entonces da un enter para pasar a la siguiente fila
        if (i % 5 == 0) and (i != 0):
            tabla += "\n"
        #Sumo los nombres de las funciones separadas con una tabulacion
        tabla += "\t"+lista[i]

    return tabla

obtener_tabla_para_imprimir(lista)