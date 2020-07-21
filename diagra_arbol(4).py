def diccionario_general(archivo):
    """ [Autor: Augusto Carmona]
        [Ayuda: desarrolla la iteracion de lineas del archivo, las deriva a su analisis y genera un diccionario
        con una clave (nombre de la funcion), cuyo valor es una tupla con los componentes internos: cantidad de
        lineas [0] y funciones a las que llama [1]]
    """
    dicc_funciones = {}

    linea = archivo.readline().split(";")
    while linea != [""]:
        
        nombre_funcion, lineas_funcion, llamados_funcion = analizar_linea(linea)
        dicc_funciones[nombre_funcion] = lineas_funcion, llamados_funcion
        
        linea = archivo.readline().split(";")

    return dicc_funciones

#---------------------------------#

def analizar_linea(linea):
    """ [Autor: Augusto Carmona]
        [Ayuda: extrae de cada linea el nombre de la funcion, la cantidad de lineas de esta y los llamados que realiza
    """
    nombre = linea[0]
    lineas = linea[-1]
    llamados = linea[1:-1]

    return nombre, int(lineas), llamados
    
#---------------------------------#
def buscar_main(diccionario):
    """ [Autor: Augusto Carmona]
        [Ayuda: muestra en pantalla un diagrama de arbol con la informacion de las funciones]
    """
    nombre_funcion_principal = []
    listado_funcion = []
    funciones_final = []
    
    for clave in diccionario:

        nombre, contenido = invocaciones(clave, diccionario)
        listado_funcion.extend([nombre, contenido]) #agrega cada funcion individual
        
        if len(diccionario[clave][1]) > len(nombre_funcion_principal): 
            nombre_funcion_principal = clave #identfica la funcion con mas llamados    
    
    contenido_principal = diccionario[nombre_funcion_principal]
    funcion_principal = [nombre_funcion_principal, contenido_principal]

    for funcion in listado_funcion:
        if funcion not in funcion_principal:
            funciones_final.append(funcion)

    return funcion_principal

#---------------------------------#
def invocaciones(clave, diccionario):
    """ [Autor: Augusto Carmona]
        [Ayuda: exporta]
    """
    nombre = clave
    contenido = diccionario[clave]

    return nombre, contenido

#---------------------------------#
def imprimir(funcion_principal, diccionario_funciones):
    """ [Autor: Augusto Carmona]
        [Ayuda: imprime]
    """
    print()
    print()
    print("=====ARBOL DE INVOCACIONES=====================================================")
    print()
    print("{}({})".format(funcion_principal[0], funcion_principal[1][0]))

    acumulador = []
    for funcion in funcion_principal[1][1]:
        if funcion not in acumulador:
            print(" " * len(funcion_principal[0]), "--> {}({})".format(funcion, diccionario_funciones[funcion][0]))
            if len(diccionario_funciones[funcion][1]) > 0:

                segundo_acumulador = []
                for i in diccionario_funciones[funcion][1]:
                    if i not in segundo_acumulador:
                        print(" " * len(funcion_principal[0]) + "\t\t", "-->{}({})".format(i))
                    segundo_acumulador. append(i)
            print()
        acumulador.append(funcion)
    print("===============================================================================")
    print()
    print()


#------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------- bloque principal ---------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------#
def main():
    """ [Autor: Augusto Carmona]
        [Ayuda: abre el archivo principal, lo deriva  la funcion diccionario_general para obtener un diccionario
        con las funciones a analizar y cierra el archivo. Una vez obtenido el diccionario general lo envia a la
        funcion imprimir]
    """
    archivo = open('data_arbol.csv', 'r')
    diccionario_funciones = diccionario_general(archivo)
    archivo.close()
    funcion_principal = buscar_main(diccionario_funciones)
    imprimir(funcion_principal, diccionario_funciones)

main()