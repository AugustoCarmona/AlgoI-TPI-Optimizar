from tabla_1 import tabla

def nombre(lista_codigo,archivo_analizado,valor_archivo,nombre_funcion):
    """[Autor: Luciano Solis]
       [Ayuda: Esta función lo que hace es devolver el nombre de la función]
    """
    if valor_archivo==0:
        nombre_funcion=lista_codigo[archivo_analizado][valor_archivo]
    return nombre_funcion

def contador_parametros(lista_codigo,archivo_analizado,valor_archivo,cont_parametr):
    """[Autor: Gastón Mondín y Luciano Solis]
       [Ayuda: Esta función lo que hace es devolver la cantidad de parametros que tiene la función que se está recorriendo.]
    """
    if valor_archivo==1: 
        cont_comas=lista_codigo[archivo_analizado][valor_archivo].count(",")
        if cont_comas!=0:
            cont_parametr=1+cont_comas
        elif len(lista_codigo[archivo_analizado][valor_archivo]) >=3:
            cont_parametr+=1
    return cont_parametr

def modulo(lista_codigo,archivo_analizado,valor_archivo,nombre_modulo):
    """[Autor: Alejandro Guzman y Luciano Solis]
       [Ayuda: Esta función lo que hace es devolver el módulo de la función que se está recorriendo.]
    """
    if valor_archivo==2:
        nombre_modulo=lista_codigo[archivo_analizado][valor_archivo]
    return nombre_modulo

def contador_lineas(valor_archivo,cont_lineas):
    """[Autor: Alejandro Guzman y Luciano Solis]
       [Ayuda: Esta función lo que hace es devolver la cantidad de líneas que tiene la función que se esta recorriendo.]
    """
    if valor_archivo>2:
        cont_lineas+=1
    return cont_lineas

def contador_return(lista_codigo,archivo_analizado,valor_archivo,cont_return):
    """[Autor: Alejandro Guzman y Luciano Solis]
       [Ayuda: Esta función lo que hace es devolver si la función que se está recorriendo tiene returns.]
    """
    if "return" in lista_codigo[archivo_analizado][valor_archivo]:
        cont_return+=1
    return cont_return
    
def contador_if(lista_codigo,archivo_analizado,valor_archivo,cont_if):
    """[Autor: Alejandro Guzman y Luciano Solis]
       [Ayuda: Esta función lo que hace es devolver la cantidad de if y elif que tiene la función.]
    """
    if "if" in lista_codigo[archivo_analizado][valor_archivo] or "elif" in lista_codigo[archivo_analizado][valor_archivo]:
        cont_if+=1
    return cont_if

def contador_for(lista_codigo,archivo_analizado,valor_archivo,cont_for):
    """[Autor: Alejandro Guzman y Luciano Solis]
       [Ayuda: Esta función lo que hace es devolver la cantidad de for que tiene la función que se esta recorriendo.]
    """
    if "for" in lista_codigo[archivo_analizado][valor_archivo]:
        cont_for+=1
    return cont_for

def contador_while(lista_codigo,archivo_analizado,valor_archivo,cont_while):
    """[Autor: Alejandro Guzman y Luciano Solis]
       [Ayuda: Esta función lo que hace es devolver la cantidad de while que tiene la función que se esta recorriendo.]
    """
    if "while" in lista_codigo[archivo_analizado][valor_archivo]:
                cont_while+=1
    return cont_while

def contador_break(lista_codigo,archivo_analizado,valor_archivo,cont_break):
    """[Autor: Alejandro Guzman y Luciano Solis]
       [Ayuda: Esta función lo que hace es devolver la cantidad de breaks que tiene la función que se esta recorriendo.]
    """
    if lista_codigo[archivo_analizado][valor_archivo]=="break":
                cont_break+=1
    return cont_break

def contador_exit(lista_codigo,archivo_analizado,valor_archivo,cont_exit):
    """[Autor: Alejandro Guzman y Luciano Solis]
       [Ayuda: Esta función lo que hace es devolver la cantidad de returns que tiene la función que se esta recorriendo]
    """
    if "exit" in lista_codigo[archivo_analizado][valor_archivo]:
        cont_exit+=1
    return cont_exit

def cantidad_de_invocaciones(lista_codigo,nombre_funcion,archivo_analizado):
    """[Autor: Alejandro Guzman, Gastón Mondín y Luciano Solis]
       [Ayuda: Esta función recibe una lista anidada, un elemento de una sublista que es una función y una posición de la lista anidada
        y lo que devuelve es la cantidad de veces que se invocó al elemento funcion en la lista anidada.]
    """
    cont_invocaciones=0
    for archivo_analizado_2 in range(len(lista_codigo)):
        for valor_archivo_2 in range(len(lista_codigo[archivo_analizado_2])):
            if archivo_analizado!=archivo_analizado_2 and nombre_funcion+"(" in lista_codigo[archivo_analizado_2][valor_archivo_2]:
                if lista_codigo[archivo_analizado_2][valor_archivo_2][lista_codigo[archivo_analizado_2][valor_archivo_2].index(nombre_funcion+"(")-1].isalnum()==False and lista_codigo[archivo_analizado_2][valor_archivo_2][lista_codigo[archivo_analizado_2][valor_archivo_2].index(nombre_funcion+"(")-1]!="_":
                    cont_invocaciones+=1
    return cont_invocaciones

def obtener_informacion_lista_comentarios(lista_comentarios,archivo_analizado,autor,ayuda,cont_coment):
    """[Autor: Gaston Mondin]
       [Ayuda: Esta funcion lo que hace es obtener la informacion que se necesita de lista_comentarios, como la cantidad
        de comentarios, el autor de la misma, y si tiene ayuda o no.]
    """
    for valor_archivo in range(len(lista_comentarios[archivo_analizado])):
            if "[Autor" in lista_comentarios[archivo_analizado][valor_archivo]:
                autor = lista_comentarios[archivo_analizado][valor_archivo][lista_comentarios[archivo_analizado][valor_archivo].index(":")+2:lista_comentarios[archivo_analizado][valor_archivo].index("]")]
            elif "[Ayuda" in lista_comentarios[archivo_analizado][valor_archivo]:
                ayuda = "Si"
            elif valor_archivo>2:
                cont_coment+=1
                
    return autor,ayuda,cont_coment

def contador(archivo, lista_codigo, lista_comentarios):
    """[Autor: Alejandro Guzman, Gastón Mondín y Luciano Solis]
       [Ayuda: Esta función recibe dos listas anidadas y un archivo vacio. Lo que hace esta función es juntar información
        de la cantidad de veces que se utiliza cada función, como así tambien los comentarios.]
    """   
    for archivo_analizado in range(len(lista_codigo)):
        nombre_funcion=nombre_modulo=""
        autor="S/A"
        ayuda="NO"
        cont_lineas=cont_parametr=cont_return=cont_if=cont_for=cont_while=cont_break=cont_exit=cont_coment=0
        for valor_archivo in range(len(lista_codigo[archivo_analizado])):
            nombre_funcion=nombre(lista_codigo,archivo_analizado,valor_archivo,nombre_funcion)
            cont_parametr=contador_parametros(lista_codigo,archivo_analizado,valor_archivo,cont_parametr)
            nombre_modulo=modulo(lista_codigo,archivo_analizado,valor_archivo,nombre_modulo)
            cont_lineas=contador_lineas(valor_archivo,cont_lineas)
            cont_return=contador_return(lista_codigo,archivo_analizado,valor_archivo,cont_return)
            cont_if=contador_if(lista_codigo,archivo_analizado,valor_archivo,cont_if)
            cont_for=contador_for(lista_codigo,archivo_analizado,valor_archivo,cont_for)
            cont_while=contador_while(lista_codigo,archivo_analizado,valor_archivo,cont_while)
            cont_break=contador_break(lista_codigo,archivo_analizado,valor_archivo,cont_break)
            contador_exit(lista_codigo,archivo_analizado,valor_archivo,cont_exit)
        autor,ayuda,cont_coment=obtener_informacion_lista_comentarios(lista_comentarios,archivo_analizado,autor,ayuda,cont_coment)                          
        cont_invocaciones=cantidad_de_invocaciones(lista_codigo, nombre_funcion, archivo_analizado)
        diccionario={"FUNCION":nombre_funcion+"." +nombre_modulo,"Parámetros":cont_parametr,"Líneas": cont_lineas,"Invocaciones":cont_invocaciones,"Returns":cont_return,"If/elif":cont_if,"For":cont_for,"While":cont_while,"Break":cont_break,"Exit":cont_exit,"Coment":cont_coment,"Ayuda":ayuda,"Autor":autor}
        tabla(diccionario)
        grabar_archivo(diccionario, archivo, archivo_analizado)

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

def imprimir_tabla(archivo,lista_fuente_unico, lista_comentarios):
    """ [Autor: Augusto Carmona]
        [Ayuda: Prepara la impresion de la informacion de contadores en formato tabla]
    """
    print()
    print(" ________________________________________________________________________________________________________________________")
    print("|           Funcion/Modulo           ", "| Par", "| Lín", "| Inv", "| Ret", "| If ", "| For", "| Whi", "| Bre", "| Ext", "| Com", "|Ayu", "|     Autor      |")
    print("|_____________________________________|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|____|________________|")
    contador(archivo,lista_fuente_unico, lista_comentarios)
    print("|_____________________________________|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|____|________________|")
    print()

def grabar_archivo(diccionario, archivo, archivo_analizado):
    """[Autor: Gastón Mondín]
       [Ayuda: Recibe el diccionario y el archivo y guarda los datos en el panel general.]
    """ 
    if archivo_analizado==0:
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
    imprimir_tabla(archivo,lista_fuente_unico, lista_comentarios)
    archivo.close()