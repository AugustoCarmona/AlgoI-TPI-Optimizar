def leo_comentario ():
    """ [Autor:Jose Piñeiro]
        [Ayuda:Esta funcion señala que autor hizo que funcion]
    """
    diccionario_De_autores={}
    with open ("data\\comentarios.csv") as archivo:
        linea = archivo.readline().split(";")
        while linea != [""]:
            if len(linea)>1:
                if linea[1] != [""]:
                    autor = linea[1].strip("[Autor:]")
                    if autor in diccionario_De_autores:
                        diccionario_De_autores[autor].append([linea[0]])
                    else:
                        diccionario_De_autores[autor]=[[linea[0]]]
            linea = archivo.readline().split(";")

    return diccionario_De_autores
#------------------------------------------------------------

def leo_fuente ():
    """ [Autor:Jose Piñeiro]
        [Ayuda:Esta funcion devuelve un diccionario con las funciones y su cantidad de lineas de codigo]
    """
    with open ("data\\fuente_unico.csv") as archivo:
        diccionario_De_funciones={}
        linea = archivo.readline().split(";")
        while linea != [""]:
            diccionario_De_funciones[linea[0]]=[len(linea)-3]
            linea = archivo.readline().split(";")
    return diccionario_De_funciones
#------------------------------------------------------------

def uno_fuente_comentario (funciones,autores):
    """ [Autor:Jose Piñeiro]
        [Ayuda:Esta funcion une a las funciones con su cantidad de lineas de codigo]
    """
    diccionario_final = {}
    for autor in autores:
        tamaño=len(autores[autor])
        index = 0
        while index < tamaño:
            nombre = autores[autor][index][0]
            cantidad = funciones[autores[autor][index][0]][0]
            if autor in diccionario_final:
                diccionario_final[autor].append([nombre,cantidad])
            else:
                diccionario_final[autor] = [[nombre,cantidad]]
            index += 1
    return diccionario_final
#------------------------------------------------------------

def suma_funciones ():
    """ [Autor:Jose Piñeiro]
        [Ayuda:Esta funcion mantiene la cuenta de cantidad de codigo y cantidad de funciones]
    """
    with open ("data\\fuente_unico.csv") as archivo:
        numero_renglones=0
        numero_funciones=0
        linea = archivo.readline().split(";")
        while linea != [""]:
            numero_renglones += len(linea)-3
            numero_funciones += 1
            linea = archivo.readline().split(";")
    return numero_renglones,numero_funciones
#------------------------------------------------------------

def imprimir (diccionario,total_lineas,funciones_totales,texto_participacion):
    """ [Autor:Jose Piñeiro]
        [Ayuda:Esta funcion imprime el diccionario de autores de la forma pedida y da el porcentaje]
    """
    for autor in diccionario:
        print ("%-1s %s" %("Autor:", autor))
        texto_participacion.writelines(("%-1s %s" %("Autor:", autor)) + '\n')
        print("%-6s %-23s %s" %("","Funcion", "Lineas"))
        texto_participacion.writelines(("%-6s %-23s %s" %("","Funcion", "Lineas")) + '\n')
        print ("---------------------------------------")
        texto_participacion.writelines("---------------------------------------" + '\n')
        print ("")
        texto_participacion.writelines("" + '\n')
        lineas_imprimir(diccionario,autor,total_lineas,texto_participacion)
    print("%s %s %-1s %6s" %("Total:",funciones_totales, "Funciones - Lineas",total_lineas) )
    texto_participacion.writelines(("%s %s %-1s %6s" %("Total:",funciones_totales, "Funciones - Lineas",total_lineas) ) + '\n')
#------------------------------------------------------------

def lineas_imprimir(diccionario,autor,total_lineas,texto_participacion):
    """ [Autor:Jose Piñeiro]
        [Ayuda:Esta funcion imprime el o los renglones de las funciones en las que trabajo cada autor
        y tambien da el porcentaje de trabajo]
    """
    cantidad_funciones = 0
    cantidad_lineas = 0
    for funcion in range(0,len(diccionario[autor])):
        funcion_nombre=0
        numeros=1
        while numeros < 2:
            cantidad_funciones += 1
            cantidad_lineas += int(diccionario[autor][funcion][numeros])
            print ("%-6s %-23s %+3s" % ( "" , diccionario [ autor ] [funcion] [ funcion_nombre ] , diccionario [ autor ] [funcion] [ numeros ] ) )
            texto_participacion.writelines(("%-6s %-23s %s" % ( "" , diccionario [ autor ] [funcion] [ funcion_nombre ] , diccionario [ autor ] [funcion] [ numeros ] ) ) + '\n')
            if numeros < 2:   
                funcion += 1
                numeros += 1
    porcentaje = cantidad_lineas /  total_lineas*100
    print("%-6s %s %-22s %s %s %s" %("",cantidad_funciones,"funciones - lineas",cantidad_lineas,int(porcentaje),"%"))
    texto_participacion.writelines(("%-6s %s %-22s %s %s %s" %("",cantidad_funciones,"funciones - lineas",cantidad_lineas,int(porcentaje),"%")) + '\n')
    print("")
    texto_participacion.writelines("" + '\n')
#------------------------------------------------------------

def main_cinco():
    """ [Autor:Jose Piñeiro]
        [Ayuda:Esta funcion llama al resto de las funciones]
    """
    texto_participacion = open("participacion.txt","w")
    autores = leo_comentario()
    funciones = leo_fuente()
    diccionario = uno_fuente_comentario(funciones,autores)
    total_lineas,funciones_totales = suma_funciones()
    imprimir (diccionario,total_lineas,funciones_totales,texto_participacion)
    texto_participacion.close()

main_cinco()