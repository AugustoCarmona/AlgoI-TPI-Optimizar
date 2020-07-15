#FUNCIONES
#-----------------------------------
def extractor_informacion(): #se activa en main
    """ [Autor: Augusto Carmona]
        [Ayuda: Lee cada linea del archivo .csv y extrae los datos de las funciones.
        Por ultimo genera una lista ordenada alfabeticamente con los nombres de las funciones
        en el archivo y la devuelve junto con el diccionario original.]
    """
    with open("panel_general.csv", "r") as archivo:

        dicc_funciones = {}
        linea = archivo.readline()
        for linea in archivo: #acumula los nombres de las funciones como clave en un diccionario y agrega la info de cada funcion a su lista correspondiente
            nombre, parametros, lineas, invocaciones, retorno, si, para, mientras, quiebre, salida, comentarios, ayuda, autor, info = linea.rstrip().split(",")
            funcion, modulo = nombre.split(".")
            dicc_funciones[funcion] = [modulo, parametros, lineas, invocaciones, retorno, si, para, mientras, quiebre, salida, comentarios, ayuda, autor, info]

        return sorted(dicc_funciones), dicc_funciones

#-----------------------------------
def ajustar_largo(texto, largo): #se activa en generador_tabla
    """[Autor: Augusto Carmona]

"""
    if len(texto) > largo:
        texto = texto[:largo]
    elif len(texto) < largo:
        texto = (texto + " " * largo)[:largo]
    
    return texto
#-----------------------------------
def generador_tabla(lista_funciones): #se activa en main
    """ [Autor: Augusto Carmona]
        [Ayuda: Genera e imprime la tabla de funciones]
    """
    funciones_por_columna = round(len(lista_funciones) / 5)
        
    columna_1 = lista_funciones[:funciones_por_columna]
    columna_2 = lista_funciones[funciones_por_columna:funciones_por_columna*2]
    columna_3 = lista_funciones[funciones_por_columna*2:funciones_por_columna*3]
    columna_4 = lista_funciones[funciones_por_columna*3:funciones_por_columna*4]
    columna_5 = lista_funciones[funciones_por_columna*4:]
        
    data = [columna_1, columna_2, columna_3, columna_4, columna_5]
        
    print('|FUNCIONES DEL MODULO:', '-'*77, end = '|')
    print()
    for i in data:
        print("| ", end = " ")
        for columna in i:
            print(ajustar_largo(columna + '()', 20), end = '  |  ')
        print()
    print('|', '-'*98, end = '|')
            
#-----------------------------------
def consulta_individual(funcion, diccionario_funciones): #se activa en menu_ingreso
    """ [Autor: Augusto Carmona]
        [Ayuda: Recibe el nombre de una funcion y el diccionario de funciones
        y devuleve la informacion de ayuda, autor y parametros de dicha funcion]
    """
    print()
    print('-----------------------------------')
    print()
    print('|Info|:')
    print('-------')
    print(diccionario_funciones[funcion][13].replace('"', '').replace('[', '').replace(']', '\n').replace('\n (', '\n Parametros: ('))
    print('-----------------------------------')
    print()

#-----------------------------------
def descripcion_individual(funcion, diccionario_funciones): #se activa en menu_ingreso
    """ [Autor: Augusto Carmona]
        [Ayuda: Recibe el nombre de una funcion y el diccionario de funciones
        y devuleve la informacion de contadores relevante a dicha funcion]
    """
    print()
    print('-----------------------------------')
    print('|Contadores Internos de la Funcion|:')
    print()
    print('|Modulo:', diccionario_funciones[funcion][0])
    print('|Cantidad de Parametros:', diccionario_funciones[funcion][1])
    print('|Lineas de Codigo de la Funcion:', diccionario_funciones[funcion][2])
    print('|Cantidad de Invocaciones a la Funcion:', diccionario_funciones[funcion][3])
    print('|Cantidad de Returns:', diccionario_funciones[funcion][4])
    print('|Cantidad de Ciclos If/elif:', diccionario_funciones[funcion][5])
    print('|Cantidad de Ciclos For:', diccionario_funciones[funcion][6])
    print('|Cantidad de Ciclos While:', diccionario_funciones[funcion][7])
    print('|Cantidad de Breaks:', diccionario_funciones[funcion][8])
    print('|Cantidad de Exits:', diccionario_funciones[funcion][9])
    print('|Cantidad de Comentarios:', diccionario_funciones[funcion][10])
    print('|Ayuda:', diccionario_funciones[funcion][11])
    print('|Autor:', diccionario_funciones[funcion][12])
    print('-----------------------------------')
    print()

#-----------------------------------
def consulta_general(lista_funciones, diccionario_funciones): #se activa en menu_ingreso
    """ [Autor: Augusto Carmona]
        [Ayuda: Muestra en display la seccion de ayuda autor y parametros de cada funcion, anteponiendo
        el nombre de la funcion a la que corresponda]
    """
    for funcion in lista_funciones:
        print()
        print('-----------------------------------')
        print('|Funcion|: {}()'.format(funcion))
        print()
        print('|Info|:')
        print('-------')
        print(diccionario_funciones[funcion][13].replace('"', '').replace('[', '').replace(']', '\n').replace('\n (', '\n Parametros: ('))
        print('-----------------------------------')
        print()

#-----------------------------------
def descripcion_general(lista_funciones, diccionario_funciones): #se activa en menu_ingreso
    """ [Autor: Augusto Carmona]
        [Ayuda: Muestra en display la informacción de contadres internos de cada funcion, anteponiendo
        el nombre de la funcion a la que corresponda]
    """
    for funcion in lista_funciones:
        print()
        print('-----------------------------------')
        print('|Funcion|: {}()'.format(funcion))
        print('|Contadores Internos de la Funcion|')
        print()
        print('|Modulo:', diccionario_funciones[funcion][0])
        print('|Cantidad de Parametros:', diccionario_funciones[funcion][1])
        print('|Lineas de Codigo de la Funcion:', diccionario_funciones[funcion][2])
        print('|Cantidad de Invocaciones a la Funcion:', diccionario_funciones[funcion][3])
        print('|Cantidad de Returns:', diccionario_funciones[funcion][4])
        print('|Cantidad de Ciclos If/elif:', diccionario_funciones[funcion][5])
        print('|Cantidad de Ciclos For:', diccionario_funciones[funcion][6])
        print('|Cantidad de Ciclos While:', diccionario_funciones[funcion][7])
        print('|Cantidad de Breaks:', diccionario_funciones[funcion][8])
        print('|Cantidad de Exits:', diccionario_funciones[funcion][9])
        print('|Cantidad de Comentarios:', diccionario_funciones[funcion][10])
        print('|Ayuda:', diccionario_funciones[funcion][11])
        print('|Autor:', diccionario_funciones[funcion][12])
        print('-----------------------------------')
        print()
        
#-----------------------------------        
def imprimir_ayuda(lista_funciones, diccionario_funciones):
    print()
    print('Se mando todo al archivo ayuda_funciones.txt wachinn. Dale que vaaaa')
    print()

#-----------------------------------
def menu_ingreso(lista_funciones, diccionario_funciones): #se activa en main
    """ [Autor: Augusto Carmona]
        [Ayuda: Solicita el ingreso de la funcion a analizar y la deriva a la funcion
        correspondiente y/o pide un reingreso, dependiendo de lo que ingrese el usuario]
    """
    print()
    ing = input("|Funcion: ")
    
    #solicitud de ingreso y derivacion
    while (ing != ""):
        if ing.strip('?').strip('#') in lista_funciones:
            funcion = ing.strip('?').strip('#')
            
            if '?' in ing:
                consulta_individual(funcion, diccionario_funciones) #comando a
                ing = input("|Funcion: ")
            
            elif '#' in ing:
                descripcion_individual(funcion, diccionario_funciones) #comando b
                ing = input("|Funcion: ")
            else:
                print()
                ing = input(" Usted ha ingresado una orden incorrecta, por favor reingrese: ")
        
        elif ing == '?todo':
            consulta_general(lista_funciones, diccionario_funciones) #comando c
            ing = input("|Funcion: ")
        
        elif ing == '#todo':
            descripcion_general(lista_funciones, diccionario_funciones) #comando d
            ing = input("|Funcion: ")
        
        elif ing == 'imprimir?todo':
            imprimir_ayuda(lista_funciones, diccionario_funciones) #comando e
            ing = input("|Funcion: ")
        
        else:
            print()
            ing = input(" Usted ha ingresado una orden incorrecta, por favor reingrese: ")
            
#--------------------------------------------------------------------------------------#
#---------------------------------- bloque principal ----------------------------------#
#--------------------------------------------------------------------------------------#
def main():
    """[Autor: Augusto Carmona]
    """
    print('-------------------------------------------------------------------------------------------------------------------')
    print(' COMANDOS:')
    print()
    print( '| ? + (funcion) |: muestra la descripcion de la funcion ingresada, autor, modulo y parametros formales que espera') #comando a
    print()
    print( '| # + (funcion) |: muestra todo lo relativo a la funcion') #comando b
    print()
    print( '| ?todo |: muestra la descripcion asociada al uso de cada funcion en el programa') #comando c
    print()
    print( '| #todo |: mustra todo lo relativo a cada funcion en el programa') #comando d
    print()
    print( '| imprimir?todo |: envia al archivo ayuda_funciones.txt el contenido corresponiente') #comando e
    print('-------------------------------------------------------------------------------------------------------------------')
    
    print()
    lista_funciones, diccionario_funciones = extractor_informacion()
    generador_tabla(lista_funciones)
    print()
    menu_ingreso(lista_funciones, diccionario_funciones)

main()