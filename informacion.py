def leo_comentario ():
    """ [Autor: Jose Piñeiro]
        [Ayuda: Esta función señala qué autor hizo qué función.]
    """
    diccionario_De_autores={}
    with open ("comentarios.csv") as archivo:
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

def leo_fuente ():
    """ [Autor: Jose Piñeiro]
        [Ayuda: Esta función devuelve un diccionario con las funciones y su cantidad de líneas de código.]
    """
    with open ("fuente_unico.csv") as archivo:
        diccionario_De_funciones={}
        linea = archivo.readline().split(";")
        while linea != [""]:
            diccionario_De_funciones[linea[0]]=[len(linea)-3]
            linea = archivo.readline().split(";")
    return diccionario_De_funciones

def uno_fuente_comentario (funciones,autores):
    """ [Autor: Jose Piñeiro]
        [Ayuda: Esta función une a las funciones con su cantidad de líneas de código]
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

def suma_funciones ():
    """ [Autor: Jose Piñeiro]
        [Ayuda: Esta función mantiene la cuenta de cantidad de código y cantidad de funciones.]
    """
    with open ("fuente_unico.csv") as archivo:
        numero_renglones=0
        numero_funciones=0
        linea = archivo.readline().split(";")
        while linea != [""]:
            numero_renglones += len(linea)-3
            numero_funciones += 1
            linea = archivo.readline().split(";")
    return numero_renglones,numero_funciones

def imprimir (diccionario,total_lineas,funciones_totales,texto_participacion):
    """ [Autor: Jose Piñeiro]
        [Ayuda: Esta función imprime el diccionario de autores de la forma pedida y da el porcentaje.]
    """
    print("\n    Informe de Desarrollo por Autor")
    texto_participacion.writelines("    Informe de Desarrollo por Autor\n")
    for autor in diccionario:
        print ("\nAutor: {}\n".format(autor))
        texto_participacion.writelines("\nAutor: {}\n\n".format(autor))
        print("\tFuncion{:>22}".format("Lineas"))
        texto_participacion.writelines("\tFuncion{:>22}\n".format("Lineas"))
        print ("\t---------------------------------------")
        texto_participacion.writelines("\t---------------------------------------\n")
        lineas_imprimir(diccionario,autor,total_lineas,texto_participacion)
    print("\nTotal:{:>3} Funciones - Lineas {:>6}\n".format(funciones_totales, total_lineas))
    texto_participacion.writelines("\nTotal:{:>3} Funciones - Lineas {:>6}\n\n".format(funciones_totales, total_lineas))

def lineas_imprimir(diccionario,autor,total_lineas,texto_participacion):
    """ [Autor: Jose Piñeiro]
        [Ayuda: Esta funcón imprime el o los renglones de las funciones en las que trabajó cada autor
        y también da el porcentaje de trabajo.]
    """
    cantidad_funciones = 0
    cantidad_lineas = 0
    for funcion in range(0,len(diccionario[autor])):
        funcion_nombre=0
        numeros=1
        while numeros < 2:
            cantidad_funciones += 1
            cantidad_lineas += int(diccionario[autor][funcion][numeros])
            print("\t{:<22}{:>5}".format(diccionario[autor][funcion][funcion_nombre], diccionario[autor][funcion][numeros]))
            texto_participacion.writelines("\t{:<22}{:>5}\n".format(diccionario[autor][funcion][funcion_nombre], diccionario[autor][funcion][numeros]))
            if numeros < 2:   
                funcion += 1
                numeros += 1
    porcentaje = cantidad_lineas /  total_lineas*100
    print("\t{} Funciones - Lineas\t{:>3}   {}%\n".format(cantidad_funciones, cantidad_lineas, int(porcentaje)))
    texto_participacion.writelines("\t{} Funciones - Lineas\t{:>3}   {}%\n\n".format(cantidad_funciones, cantidad_lineas, int(porcentaje)))

def main():
    """ [Autor: Jose Piñeiro]
        [Ayuda: Esta función llama al resto de las funciones.]
    """
    texto_participacion = open("participacion.txt","w")
    autores = leo_comentario()
    funciones = leo_fuente()
    diccionario = uno_fuente_comentario(funciones,autores)
    total_lineas,funciones_totales = suma_funciones()
    imprimir (diccionario,total_lineas,funciones_totales,texto_participacion)
    texto_participacion.close()