def nombre(lista_codigo,posicion,caracter,nombre_funcion):
    """[Autor: Luciano Solis]
       [Ayuda: Esta función lo que hace es devolver el nombre de la función]
    """
    if caracter==0:
        nombre_funcion=lista_codigo[posicion][caracter]
    return nombre_funcion

def contador_parametros(lista_codigo,posicion,caracter,cont_parametr):
    """[Autor: Gastón Mondín y Luciano Solis]
       [Ayuda: Esta función lo que hace es devolver la cantidad de parametros que tiene la función que se está recorriendo.]
    """
    if caracter==1: 
        cont_comas=lista_codigo[posicion][caracter].count(",")
        if cont_comas!=0:
            cont_parametr=1+cont_comas
        elif len(lista_codigo[posicion][caracter]) >=3:
            cont_parametr+=1
    return cont_parametr

def modulo(lista_codigo,posicion,caracter,nombre_modulo):
    """[Autor: Alejandro Guzman y Luciano Solis]
       [Ayuda: Esta función lo que hace es devolver el módulo de la función que se está recorriendo.]
    """
    if caracter==2:
        nombre_modulo=lista_codigo[posicion][caracter]
    return nombre_modulo

def contador_lineas(caracter,cont_lineas):
    """[Autor: Alejandro Guzman y Luciano Solis]
       [Ayuda: Esta función lo que hace es devolver la cantidad de líneas que tiene la función que se esta recorriendo.]
    """
    if caracter>2:
        cont_lineas+=1
    return cont_lineas

def contador_return(lista_codigo,posicion,caracter,cont_return):
    """[Autor: Alejandro Guzman y Luciano Solis]
       [Ayuda: Esta función lo que hace es devolver si la función que se está recorriendo tiene returns.]
    """
    if "return" in lista_codigo[posicion][caracter]:
        cont_return+=1
    return cont_return
    
def contador_if(lista_codigo,posicion,caracter,cont_if):
    """[Autor: Alejandro Guzman y Luciano Solis]
       [Ayuda: Esta función lo que hace es devolver la cantidad de if y elif que tiene la función.]
    """
    if "if" in lista_codigo[posicion][caracter] or "elif" in lista_codigo[posicion][caracter]:
        cont_if+=1
    return cont_if

def contador_for(lista_codigo,posicion,caracter,cont_for):
    """[Autor: Alejandro Guzman y Luciano Solis]
       [Ayuda: Esta función lo que hace es devolver la cantidad de for que tiene la función que se esta recorriendo.]
    """
    if "for" in lista_codigo[posicion][caracter]:
        cont_for+=1
    return cont_for

def contador_while(lista_codigo,posicion,caracter,cont_while):
    """[Autor: Alejandro Guzman y Luciano Solis]
       [Ayuda: Esta función lo que hace es devolver la cantidad de while que tiene la función que se esta recorriendo.]
    """
    if "while" in lista_codigo[posicion][caracter]:
                cont_while+=1
    return cont_while

def contador_break(lista_codigo,posicion,caracter,cont_break):
    """[Autor: Alejandro Guzman y Luciano Solis]
       [Ayuda: Esta función lo que hace es devolver la cantidad de breaks que tiene la función que se esta recorriendo.]
    """
    if "break" in lista_codigo[posicion][caracter]:
                cont_break+=1
    return cont_break

def contador_exit(lista_codigo,posicion,caracter,cont_exit):
    """[Autor: Alejandro Guzman y Luciano Solis]
       [Ayuda: Esta función lo que hace es devolver la cantidad de returns que tiene la función que se esta recorriendo]
    """
    if "exit" in lista_codigo[posicion][caracter]:
        cont_exit+=1
    return cont_exit

def cantidad_de_invocaciones(lista_codigo,nombre_funcion,posicion):
    """[Autor: Alejandro Guzman, Gastón Mondín y Luciano Solis]
       [Ayuda: Esta función recibe una lista anidada, un elemento de una sublista que es una función y una posición de la lista anidada
        y lo que devuelve es la cantidad de veces que se invocó al elemento funcion en la lista anidada.]
    """
    cont_invocaciones=0
    for posicion_2 in range(len(lista_codigo)):
        for caracter_2 in range(len(lista_codigo[posicion_2])):
            if posicion!=posicion_2 and nombre_funcion+"(" in lista_codigo[posicion_2][caracter_2]:
                if lista_codigo[posicion_2][caracter_2][lista_codigo[posicion_2][caracter_2].index(nombre_funcion+"(")-1].isalnum()==False and lista_codigo[posicion_2][caracter_2][lista_codigo[posicion_2][caracter_2].index(nombre_funcion+"(")-1]!="_":
                    cont_invocaciones+=1
    return cont_invocaciones

def obtener_informacion_lista_comentarios(lista_comentarios,posicion,autor,ayuda,cont_coment):
    """[Autor: Gaston Mondin]
       [Ayuda: Esta funcion lo que hace es obtener la informacion que se necesita de lista_comentarios, como la cantidad
        de comentarios, el autor de la misma, y si tiene ayuda o no.]
    """
    for caracter in range(len(lista_comentarios[posicion])):
            if "[Autor" in lista_comentarios[posicion][caracter]:
                autor = lista_comentarios[posicion][caracter][lista_comentarios[posicion][caracter].index(":")+2:lista_comentarios[posicion][caracter].index("]")]
            elif "[Ayuda" in lista_comentarios[posicion][caracter]:
                ayuda = "Si"
            elif caracter>2:
                cont_coment+=1
                
    return autor,ayuda,cont_coment

def contador(archivo, lista_codigo, lista_comentarios):
    """[Autor: Alejandro Guzman, Gastón Mondín y Luciano Solis]
       [Ayuda: Esta función recibe dos listas anidadas y un archivo vacio. Lo que hace esta función es juntar información
        de la cantidad de veces que se utiliza cada función, como así tambien los comentarios.]
    """   
    for posicion in range(len(lista_codigo)):
        nombre_funcion=nombre_modulo=""
        autor="S/A"
        ayuda="NO"
        cont_lineas=cont_parametr=cont_return=cont_if=cont_for=cont_while=cont_break=cont_exit=cont_coment=0
        for caracter in range(len(lista_codigo[posicion])):
            nombre_funcion=nombre(lista_codigo,posicion,caracter,nombre_funcion)
            cont_parametr=contador_parametros(lista_codigo,posicion,caracter,cont_parametr)
            nombre_modulo=modulo(lista_codigo,posicion,caracter,nombre_modulo)
            cont_lineas=contador_lineas(caracter,cont_lineas)
            cont_return=contador_return(lista_codigo,posicion,caracter,cont_return)
            cont_if=contador_if(lista_codigo,posicion,caracter,cont_if)
            cont_for=contador_for(lista_codigo,posicion,caracter,cont_for)
            cont_while=contador_while(lista_codigo,posicion,caracter,cont_while)
            cont_break=contador_break(lista_codigo,posicion,caracter,cont_break)
            contador_exit(lista_codigo,posicion,caracter,cont_exit)
        autor,ayuda,cont_coment=obtener_informacion_lista_comentarios(lista_comentarios,posicion,autor,ayuda,cont_coment)                          
        cont_invocaciones=cantidad_de_invocaciones(lista_codigo, nombre_funcion, posicion)
        diccionario={"FUNCION":nombre_funcion+"." +nombre_modulo,"Parámetros":cont_parametr,"Líneas": cont_lineas,"Invocaciones":cont_invocaciones,"Returns":cont_return,"If/elif":cont_if,"For":cont_for,"While":cont_while,"Break":cont_break,"Exit":cont_exit,"Coment":cont_coment,"Ayuda":ayuda,"Autor":autor}
        imprimir_diccionario(diccionario)
        grabar_archivo(diccionario, archivo, posicion)

def armado_listas_anidadas(merge_fuente_unico):
    """[Autor: Luciano Solis]
       [Ayuda: Lo que hace esta función es recibir un archivo que contiene código y devuelve una lista anidada con toda la información
        del archivo.]
    """
    linea=merge_fuente_unico.readline().strip("\n").split(";")
    lista_final=[]
    while linea!=[""]:
        lista_final.append(linea)
        linea=merge_fuente_unico.readline().split(";")
    return lista_final

def imprimir_diccionario(diccionario):
    """[Autor: Luciano Solis]
       [Ayuda: Recibe el diccionario con los datos cargados y los muestra.]
    """
    for clave in diccionario:
        print("{}: {}".format(clave, diccionario[clave]))
    print("\n")

def grabar_archivo(diccionario, archivo, posicion):
    """[Autor: Gastón Mondín]
       [Ayuda: Recibe el diccionario y el archivo y guarda los datos en el panel general.]
    """ 
    if posicion==0:
        for campo in diccionario:
            if campo!="Autor":
                archivo.write(campo+";")
            else:
                archivo.write(campo)
        archivo.write("\n")
    for campo in diccionario:
        if campo!="Autor":
            archivo.write(str(diccionario[campo])+";")
        else:
            archivo.write(str(diccionario[campo]))
    archivo.write("\n") 

def main_panel():
    archivo=open("panel_general.csv","w")
    merge_fuente_unico=open("fuente_unico.csv","r")
    merge_comentarios=open("comentarios.csv","r")
    lista_fuente_unico=armado_listas_anidadas(merge_fuente_unico)
    lista_comentarios=armado_listas_anidadas(merge_comentarios)
    merge_fuente_unico.close()
    merge_comentarios.close()
    contador(archivo,lista_fuente_unico, lista_comentarios)
    archivo.close()