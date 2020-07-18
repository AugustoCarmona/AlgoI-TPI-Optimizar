def imprimir (diccionario,total_lineas,funciones_totales):
    """ [Autor:Jose Piñeiro]
        [Ayuda:Esta funcion imprime el diccionario de autores de la forma pedida y da el porcentaje]
    """
    for autor in diccionario:
        print ("%-1s %s" %("Autor:", autor))
        print("%-6s %-23s %s" %("","Funcion", "Lineas"))
        print ("---------------------------------------")
        print("")
        lineas_imprimir(diccionario,autor,total_lineas)
    print("%s %s %-1s %6s" %("Total:",funciones_totales, "Funciones - Lineas",total_lineas) )

def lineas_imprimir(diccionario,autor,total_lineas):
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
            print ("%-6s %-23s %s" % ( "" , diccionario [ autor ] [funcion] [ funcion_nombre ] , diccionario [ autor ] [funcion] [ numeros ] ) )
            if numeros < 2:   
                funcion += 1
                numeros += 1
    porcentaje = cantidad_lineas /  total_lineas*100
    print("%-6s %s %-22s %s %s %s" %("",cantidad_funciones,"funciones - lineas",cantidad_lineas,int(porcentaje),"%"))
    print("")
    
def autores ():
    """ [Autor:Jose Piñeiro]
        [Ayuda:Esta funcion lee el archivo panel_general y separa por autor,
         que funcion escribioy cuantas lineas tiene esa funcion y luego a nivel 
         general cuantas lineas de codigo hay]
    """
    diccionario_De_autores={}
    total_lineas = 0
    funciones_totales = 0
    with open ("panel_general.csv") as archivo:
        linea = archivo.readline().split(",")
        linea = archivo.readline().split(",")
        while linea != [""]:
            if linea[12] in diccionario_De_autores:
                diccionario_De_autores[linea[12]].append([linea[0] , linea[2]])
            else:
                diccionario_De_autores[linea[12]] = [[linea[0] , linea[2]]]
            total_lineas += int(linea[2])
            funciones_totales += 1
            linea = archivo.readline().split(",")
    return diccionario_De_autores,total_lineas,funciones_totales

def main_cinco():
    """ [Autor:Jose Piñeiro]
        [Ayuda:Esta funcion llama al resto de las funciones]
    """
    diccionario,total_lineas,funciones_totales = autores()
    imprimir (diccionario,total_lineas,funciones_totales)

main_cinco()