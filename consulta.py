from tabla_2 import tabla
#------------------------------------------------------------
def extraer_informacion():
    
    dicc_funciones = {}
    dicc_general = extractor_informacion_general()
    dicc_comentarios = extractor_informacion_ayuda()

    for funcion in dicc_general:
        dicc_funciones[funcion] = dicc_general[funcion], dicc_comentarios[funcion]

    return sorted(dicc_funciones), dicc_funciones

#------------------------------------------------------------
def extractor_informacion_general(): #se activa en main
    """ [Autor: Augusto Carmona]
        [Ayuda: Lee cada línea del archivo .csv y extrae los datos de las funciones.
        Por último genera una lista ordenada alfabeticamente con los nombres de las funciones
        en el archivo y la devuelve junto con el diccionario original.]
    """
    with open("fuente_unico.csv", "r") as fuente:

        dicc_informacion_general = {}
        for linea in fuente:
            
            #nombre de la funcion y modulo
            funcion = linea.rstrip().split(";")[0]

            lineas = linea.rstrip().split(";")[1:]

            #empalme
            dicc_informacion_general[funcion] = lineas
            
        return dicc_informacion_general

#------------------------------------------------------------
def extractor_informacion_ayuda():
    """ [Autor: Augusto Carmona]
        [Ayuda: ]
    """
    with open("comentarios.csv", "r") as comentarios:
        
        dicc_comentarios = {}
        comentarios.seek(0)

        for linea in comentarios:
            
            funcion = linea.rstrip("\n").split(";")[0]
            if len(linea.rstrip("\n").split(";")) > 1:
                autor = linea.rstrip("\n").split(";")[1]
                if len(linea.rstrip("\n").split(";")) > 2:
                    ayuda = linea.rstrip("\n").split(";")[2]
                    if len(linea.rstrip("\n").split(";")) > 3:
                        comentarios = linea.rstrip("\n").split(";")[3:]
            else:
                autor = "**No hay autor disponible**"
                ayuda = "**No hay ayuda disponible**"

            #empalme
            dicc_comentarios[funcion] = autor, ayuda
        
        return dicc_comentarios

#------------------------------------------------------------
#------------------------------------------------------------
def generador_tabla(lista_funciones): #se activa en main
    """ [Autor: Augusto Carmona]
        [Ayuda: Agrega a cada funcion un "()" y utiliza la lista de funciones para 
        (por medio del modulo tabla_2) generar la tabla correspondiente.]
    """
    nueva_lista_funciones = []

    print("FUNCIONES:")
    print("-" * 10)
    for i in lista_funciones:
        i += "()"
        nueva_lista_funciones.append(i)
    
    tabla(nueva_lista_funciones)

#------------------------------------------------------------
#------------------------------------------------------------
def consulta_individual(funcion, diccionario_funciones): #se activa en menu_ingreso
    """ [Autor: Augusto Carmona]
        [Ayuda: Recibe el nombre de una función y el diccionario de funciones
        y devuleve la información de ayuda, autor y parametros de dicha función.]
    """
    print()
    print('----------------------------------------------')
    print()
    print('|Info|:')
    print('-------------')
    print(diccionario_funciones[funcion][1][0].strip("[]")) #autor
    print("-" * 6)
    print(diccionario_funciones[funcion][1][1].strip("[]")) #ayuda
    print("-" * 6)
    print("Parametros: {}".format(diccionario_funciones[funcion][0][0])) #parametros
    print('----------------------------------------------')
    print()

#------------------------------------------------------------
def descripcion_individual(funcion, diccionario_funciones): #se activa en menu_ingreso
    """ [Autor: Augusto Carmona]
        [Ayuda: Recibe el nombre de una función y el diccionario de funciones
        y devuleve la informacion de contadores relevante a dicha función.]
    """
    print()
    print('-----------------------------------')
    print('|Informacion Interna de la Funcion|:')
    print()
    print('|Nombre: {}()'.format(funcion))
    print('|Modulo:', diccionario_funciones[funcion][0][1])
    print('|Parametros:', diccionario_funciones[funcion][0][0])
    print("|Contenido: ")
    for i in diccionario_funciones[funcion][0][2:]:
        print("\t", i)
    print('-----------------------------------')
    print()

#------------------------------------------------------------
def consulta_general(lista_funciones, diccionario_funciones): #se activa en menu_ingreso
    """ [Autor: Augusto Carmona]
        [Ayuda: Muestra en display la sección de ayuda, autor y parametros de cada función, anteponiendo
        el nombre de la función a la que corresponda.]
    """
    for funcion in lista_funciones:
        consulta_individual(funcion, diccionario_funciones)
        

#------------------------------------------------------------
def descripcion_general(lista_funciones, diccionario_funciones): #se activa en menu_ingreso
    """ [Autor: Augusto Carmona]
        [Ayuda: Muestra en display la informacción de contadres internos de cada función, anteponiendo
        el nombre de la función a la que corresponda.]
    """
    for funcion in lista_funciones:
        descripcion_individual(funcion, diccionario_funciones)

#------------------------------------------------------------
def imprimir_ayuda(lista_funciones, diccionario_funciones):
    archivo_imprimir = open('ayuda_funciones.txt', 'w')
    for funcion in lista_funciones:
        archivo_imprimir.write('-----------------------------------\n')
        archivo_imprimir.write('|Funcion|: {}()\n'.format(funcion))
        archivo_imprimir.write("{}\n".format(diccionario_funciones[funcion][1][0].strip("[]"))) #autor
        archivo_imprimir.write("{}\n".format(diccionario_funciones[funcion][1][1].strip("[]"))) #ayuda
        archivo_imprimir.write("Parametros: {}\n".format(diccionario_funciones[funcion][0][0])) #parametros
        archivo_imprimir.write('-----------------------------------')
    archivo_imprimir.close()
    print()
    print('Se mando todo al archivo ayuda_funciones.txt')
    print()

#------------------------------------------------------------
def menu_ingreso(lista_funciones, diccionario_funciones): #se activa en main
    """ [Autor: Augusto Carmona]
        [Ayuda: Solicita el ingreso de la función a analizar y la deriva a la función
        correspondiente y/o pide un reingreso, dependiendo de lo que ingrese el usuario.]
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

#--------------------------------------------------------------------------------------------------------------------------
#------------------------------------------- bloque principal -------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
def main_consulta():
    """[Autor: Augusto Carmona]
       [Ayuda: Ejecuta la función principal y hace display de los comandos.]
    """
    # aqui se imprimen los comandos que puede ejecutar el usuario en el programa
    print()
    print('-------------------------------------------------------------------------------------------------------------------')
    print(' COMANDOS:')
    print()
    print( '| ? + (funcion) |: muestra la informacion de autor, ayuda, y parametros que espera recibir la funcion ingresada') #comando a
    print()
    print( '| # + (funcion) |: muestra todo lo relativo a la funcion (modulo, parametros y el contenido de sus lineas)') #comando b
    print()
    print( '| ?todo |: muestra la descripcion asociada al uso de cada funcion en el programa') #comando c
    print()
    print( '| #todo |: mustra todo lo relativo a cada funcion en el programa') #comando d
    print()
    print( '| imprimir?todo |: envia al archivo ayuda_funciones.txt el contenido corresponiente') #comando e
    print()
    print( '| ingrese: INTRO |: cuando desee terminar la ejecucion del programa') #comando f
    print('-------------------------------------------------------------------------------------------------------------------')
    print()
    # aqui se llaman a las funciones que modularizan el programa
    lista_funciones, diccionario_funciones = extraer_informacion() #extrae los odatos necesarios para el funcionamiento del modulo
    generador_tabla(lista_funciones) #genera la tabla
    print()
    menu_ingreso(lista_funciones, diccionario_funciones) #recibe los comandos que ingrese el usuario