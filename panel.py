def contador(archivo, lista_codigo, lista_comentarios):
    """[Autor: Alejandro Guzman, Gastón Mondín y Luciano Solis]
    [Ayuda: Esta funcion recibe una lista anidada y un archivo vacio. Lo que hace esta funcion es juntar información
    de la cantidad de veces que se utiliza cada función, como así tambien los comentarios, y esa información la guarda en un archivo.]
    """   
    for posicion in range(len(lista_codigo)):
        nombre_funcion=nombre_modulo=""
        autor="S/A"
        ayuda="NO"
        cont_lineas=cont_parametr=cont_return=cont_if=cont_for=cont_while=cont_break=cont_exit=cont_coment=0
        for caracter in range(len(lista_codigo[posicion])):
            if caracter==0:
                nombre_funcion=lista_codigo[posicion][caracter]
            elif caracter==1: 
                cont_comas=lista_codigo[posicion][caracter].count(",")
                if cont_comas!=0:
                    cont_parametr=1+cont_comas
                elif len(lista_codigo[posicion][caracter]) >=3:
                    cont_parametr+=1
            elif caracter==2:
                nombre_modulo=lista_codigo[posicion][caracter]
            elif caracter>2:
                cont_lineas+=1
            if "return" in lista_codigo[posicion][caracter]:
                cont_return+=1
            if "if" in lista_codigo[posicion][caracter] or "elif" in lista_codigo[posicion][caracter]:
                cont_if+=1
            if "for" in lista_codigo[posicion][caracter]:
                cont_for+=1
            if "while" in lista_codigo[posicion][caracter]:
                cont_while+=1
            if "break" in lista_codigo[posicion][caracter]:
                cont_break+=1
            if "exit" in lista_codigo[posicion][caracter]:
                cont_exit+=1
        for caracter in range(len(lista_comentarios[posicion])):
            if "[Autor" in lista_comentarios[posicion][caracter]:
                autor = lista_comentarios[posicion][caracter][lista_comentarios[posicion][caracter].index(":")+2:lista_comentarios[posicion][caracter].index("]")]
            elif "[Ayuda" in lista_comentarios[posicion][caracter]:
                ayuda = "Si"
            elif caracter>2:
                cont_coment+=1                          
        cont_invocaciones=cantidad_de_invocaciones(lista_codigo, nombre_funcion, posicion)
        diccionario={"FUNCION":nombre_funcion+"." +nombre_modulo,"Parámetros":cont_parametr,"Líneas": cont_lineas,"Invocaciones":cont_invocaciones,"Returns":cont_return,"If/elif":cont_if,"For":cont_for,"While":cont_while,"Break":cont_break,"Exit":cont_exit,"Coment":cont_coment,"Ayuda":ayuda,"Autor":autor}
        imprimir_diccionario(diccionario)
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

def cantidad_de_invocaciones(lista_codigo,nombre_funcion,posicion):
    """[Autor: Alejandro Guzman, Gastón Mondín y Luciano Solis]
    [Ayuda: Esta función recibe una lista anidada, un elemento de una sublista que es una función y una posición de la lista anidada
    y lo que devuelve es la cantidad de veces que se invocó al elemento funcion en la lista anidada.]
    """
    cont_invocaciones=0
    for posicion_2 in range(len(lista_codigo)):
        for caracter_2 in range(len(lista_codigo[posicion_2])):
            if posicion!=posicion_2 and nombre_funcion+"(" in lista_codigo[posicion_2][caracter_2]:
                if lista_codigo[posicion_2][caracter_2][lista_codigo[posicion_2][caracter_2].index(nombre_funcion)-1].isalnum()==False and lista_codigo[posicion_2][caracter_2][lista_codigo[posicion_2][caracter_2].index(nombre_funcion)-1]!="_":
                    cont_invocaciones+=1
    return cont_invocaciones


def imprimir_diccionario(diccionario):
    """[Autor: Luciano Solis]
    [Ayuda: Recibe el diccionario con los datos cargados y los muestra.]
    """
    for clave in diccionario:
        print("{}: {}".format(clave, diccionario[clave]))
    print("\n")
        
def main():
    archivo=open("panel_general.csv","w")
    merge_fuente_unico=open("fuente_unico.csv","r")
    merge_comentarios=open("comentarios.csv","r")
    lista_fuente_unico=armado_listas_anidadas(merge_fuente_unico)
    lista_comentarios=armado_listas_anidadas(merge_comentarios)
    merge_fuente_unico.close()
    merge_comentarios.close()
    contador(archivo,lista_fuente_unico, lista_comentarios)
    archivo.close()