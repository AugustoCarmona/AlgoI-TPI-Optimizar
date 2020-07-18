def imprimir (diccionario,total_lineas):
    for autor in diccionario:
        print ("%-1s %s" %("Autor:", autor))
        print("%-6s %-23s %s" %("","Funcion", "Lineas"))
        print ("---------------------------------------")
        print("")
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
        [Ayuda:Esta funcion lee el archivo y establece que ]
    """
    diccionario_De_autores={}
    total_lineas = 0
    with open ("panel_general.csv") as archivo:
        linea = archivo.readline().split(",")
        linea = archivo.readline().split(",")
        while linea != [""]:
            if linea[12] in diccionario_De_autores:
                diccionario_De_autores[linea[12]].append([linea[0] , linea[2]])
            else:
                diccionario_De_autores[linea[12]] = [[linea[0] , linea[2]]]
            total_lineas += int(linea[2])
            linea = archivo.readline().split(",")
    return diccionario_De_autores,total_lineas

def main_cinco():
    diccionario,total_lineas = autores()
    imprimir (diccionario,total_lineas)

main_cinco()