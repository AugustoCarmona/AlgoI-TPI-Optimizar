def saco_info ():
    """ [Autor:Jose Piñeiro]
        [Ayuda:Esta funcion abre el archivo fuente_unico y extrae el codigo de cada una y su nombre]
    """
    codigos = open("data\\fuente_unico.csv","r")
    linea = codigos.readline().split(";")
    funciones = {}
    
    while(linea != [""]):
        funciones[linea[0]]=linea[3:]
        linea = codigos.readline().split(";")
    codigos.close()

    return(funciones)

#------------------------------------------------------------
def busco_funciones(lista):
    """ [Autor:Jose Piñeiro]
        [Ayuda:Esta funcion dice quien llama a quien y cuantas lineas de codigo hay de cada funcion]
    """
    funciones_nombres = {}
    diccionario_Arbol = {}

    for funcion in lista:
        funciones_nombres[funcion] = [len(lista[funcion])]#cantidad de codigo de la funcion
    
    for funcion in funciones_nombres:
        for linea in lista:
            index = 0
            while index < len(lista[linea]):
                parte_por_parte=lista[linea][index].split(" ")
                parte_index=0
                while parte_index < len(parte_por_parte):
                    if (funcion == parte_por_parte[parte_index]) or ((funcion in parte_por_parte[parte_index]) and ("." in parte_por_parte[parte_index])):
                        if not linea in diccionario_Arbol:
                            diccionario_Arbol[linea] = [[funcion]]
                        else:
                            diccionario_Arbol[linea][0].append(funcion)
                    elif ("(" in parte_por_parte[parte_index]):
                        lugar_parentesis = parte_por_parte[parte_index].find("(")
                        lugar_primera_letra_funcion = parte_por_parte[parte_index].find(funcion)
                        if (lugar_primera_letra_funcion > 0) and (not (parte_por_parte[parte_index][lugar_primera_letra_funcion - 1].isalpha) or (parte_por_parte[parte_index][lugar_primera_letra_funcion - 1] != "_")):
                            if (parte_por_parte[parte_index][lugar_parentesis] == "(" ):
                                if not linea in diccionario_Arbol:
                                    diccionario_Arbol[linea] = [[funcion]]
                                else:
                                    diccionario_Arbol[linea][0].append(funcion)
                        elif (lugar_primera_letra_funcion == 0) and (lugar_parentesis != 0) and (funcion in parte_por_parte[parte_index]):
                            if (parte_por_parte[parte_index][lugar_primera_letra_funcion + len(funcion)] == "(" ):
                                if not linea in diccionario_Arbol:
                                    diccionario_Arbol[linea] = [[funcion]]
                                else:
                                    diccionario_Arbol[linea][0].append(funcion)

                    parte_index+=1
                index += 1
    
    uniones = union(diccionario_Arbol,funciones_nombres)
    return uniones

#------------------------------------------------------------
def union(llamados,cantidad_lineas):
    """ [Autor:Jose Piñeiro]
        [Ayuda:Esta funcion une en un solo diccionario dando la cantidad de lineas de codigo de cada funcion y 
        que funcion es llamada]
    """
    no_llamados = []
    lista_finale = llamados
    
    for funcion in cantidad_lineas:
        no_llamados.append(funcion)
    for los_que_llaman in llamados:
        lista_finale[los_que_llaman].append(cantidad_lineas[los_que_llaman])
        no_llamados.remove(los_que_llaman)
    for los_llamados in no_llamados:
        lista_finale[los_llamados] = ("", cantidad_lineas[los_llamados])
    
    return lista_finale

#------------------------------------------------------------
def obtener_informacion():
    """ [Autor:Jose Piñeiro]
        [Ayuda:Esta funcion llama al resto de las funciones, para devolver 
        el diccionario utilizado en el punto 4]
    """
    diccionario = saco_info()
    diccionario_final = busco_funciones(diccionario)
    return diccionario_final

#---------------------------------#
def buscar_principal(diccionario):
    """ [Autor: Augusto Carmona]
        [Ayuda: identifica a la funcion que llama a más funciones del programa]
    """
    llamados_principal = []
    for clave in diccionario: #por cada funcion en el diccionario
        if len(diccionario[clave][0]) > len(llamados_principal): #si la funcion llama a mas funciones que la que se tiene como llamados_principal
            llamados_principal = diccionario[clave][0] #pasa a ser principal
    fue_llamada_luego = llamados_principal.copy()
    for clave in diccionario:
        if len(diccionario[clave][0]) >= 1:
            for funcion in diccionario[clave][0]:
                if not funcion in fue_llamada_luego:
                    fue_llamada_luego.append(funcion)
    return fue_llamada_luego,llamados_principal

#---------------------------------#
def imprimir(diccionario):
    """ [Autor: Augusto Carmona]
        [Ayuda: imprime un diagrama de arbol indicando que funcion llama a que funcion y entre parentesis 
        la cantidad de lineas de codigo de cada una]
    """
    print()
    print("=====ARBOL DE INVOCACIONES=====================================================")
    buscador(diccionario)
    print("===============================================================================")
    print()

#---------------------------------#
def buscador(diccionario):
    """ [Autor: Augusto Carmona]
        [Ayuda: buca e imprime]
    """
    llamados_secundarios , llamados_principales= buscar_principal(diccionario)
    for clave in diccionario: #por cada clave en el diccionario
        if (diccionario[clave][0] != "") and (not clave in llamados_secundarios): #si llama funciones y no es la principal
            print("{}({})".format(clave, diccionario[clave][-1][0])) #se imprime
            for funcion in diccionario[clave][0]: #por cada funcion que esta llama
                print()
                print("\t--> {}({})".format(funcion, diccionario[funcion][-1][0])) #tambien se imprimen
                if (diccionario[funcion][0] != "") and (funcion in llamados_principales): #si llama más funciones
                        for elemento in diccionario[funcion][0]:
                            espacio = "\t\t"
                            ajuste= espacio + "--> {}({})"
                            print(ajuste.format(elemento, diccionario[elemento][-1][0]))
                            print()
                            while diccionario[elemento][0] != "":
                                if diccionario[elemento][0] != "":
                                    espacio += "\t"
                                    ajuste= espacio + "--> {}({})"
                                    for seudo_elemento in diccionario[elemento][0]:
                                        print(ajuste.format(seudo_elemento, diccionario[seudo_elemento][-1][0]))
                                        print()
                                    elemento = seudo_elemento
                        
#------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------- bloque principal ---------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------#
def main():
    """ [Autor: Augusto Carmona]
        [Ayuda: abre el archivo principal, lo deriva  la funcion diccionario_general para obtener un diccionario
        con las funciones a analizar y cierra el archivo. Una vez obtenido el diccionario general lo envia a la
        funcion imprimir]
    """
    diccionario_funciones = obtener_informacion()
    imprimir(diccionario_funciones)

main()