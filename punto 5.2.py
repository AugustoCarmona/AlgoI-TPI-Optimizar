def contador(archivo,lista_codigo):
          """[Autor:Luciano Solis y Alejandro Guzman]
             [Ayuda: Esta funcion recibe una lista anidada y un archivo vacio.Lo que hace esta funcion es juntar informacion
             de la cantidad de veces que se utiliza cada funcion, como asi tambien los comentarios, y esa informacion la guarda en un archivo
          """   
          for posicion in range(len(lista_codigo)):
              diccionario={}
              nombre_funcion=""
              nombre_modulo=""
              autor=""
              ayuda="NO"
              cont_parametr=0
              cont_return=0
              cont_if=0
              cont_for=0
              cont_while=0
              cont_break=0
              cont_exit=0
              cont_coment=0
              for caracter in range(len(lista_codigo[posicion])):
                 if caracter==0:
                     nombre_funcion=lista_codigo[posicion][caracter]

                 elif caracter==1: # revisar parametros 
                     cont_comas=lista_codigo[posicion][caracter].count(",")
                     if cont_comas!=0:
                         cont_parametr=1+cont_comas
                     elif len(lista_codigo[posicion][caracter]) >=3:
                         cont_parametr+=1
                 elif caracter==2:
                     nombre_modulo=lista_codigo[posicion][caracter]

                # if "(" in lista_codigo[posicion][caracter] and ")" in lista_codigo[posicion][caracter]:#verificar esto
                     #cont_parametr+=1

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

                 lista_comentarios=merge_comentarios.readline().split(";")
                 if nombre_funcion in lista_comentarios:
                             for posicion_comentario in lista_comentarios:
                                 if "Autor" in posicion_comentario:
                                      autor = posicion_comentario[posicion_comentario.index(":")+1:posicion_comentario.index("]")]
                                 elif "Ayuda" in posicion_comentario:
                                      ayuda= "Si"
                                 elif ayuda=="Si" or (len(lista_comentarios[:lista_comentarios.index(posicion_comentario)]) > 1 and "[Ayuda" not in posicion_comentario) :
                                      cont_coment+=1

              invocaciones=cantidad_de_invocaciones(lista_merge_fuente_unico,nombre_funcion,posicion) # revisar invocaciones   
              merge_comentarios.seek(0)
              diccionario={"Funcion":nombre_funcion+"." +nombre_modulo,"parametros":cont_parametr,"returns":cont_return,"elif/if":cont_if,"for":cont_for,"while":cont_while,"break":cont_break,"exit":cont_exit,"comentarios":cont_coment,"autor":autor,"ayuda":ayuda,"invocaciones":invocaciones}
              #print(diccionario)
              imprimir_diccionario(diccionario)
              archivo.write(str(nombre_funcion)+"."+str(nombre_modulo) + ";" + str(cont_parametr) +";"+ str(cont_return)+";"+str(cont_if)+";"+str(cont_for)+";"+str(cont_while)+";"+str(cont_break) +";"+str(cont_exit)+";"+str(cont_coment)+"\n")
              print("")

def armado_listas_fuente_unico(merge):
    """[Autor:Luciano Solis]
       [Ayuda: Lo que hace esta funcion es recibir un archivo que contiene codigo y devuelve una lista anidada con toda la informacion del archivo]
    """
    linea=merge_fuente_unico.readline().strip("\n").split(";")
    lista_final=[]
    while linea!=[""]:
         lista_final.append(linea)
         linea=merge_fuente_unico.readline().split(";")

    return lista_final


def armado_listas_comentarios(merge):
    """[Autor:Luciano Solis]
       [Ayuda: Lo que hace esta funcion es recibir un archivo que contiene comentarios y devuelve una lista anidada con toda la informacion del archivo]
    """
    linea=merge_fuente_unico.readline().rstrip("\n").split(";")
    lista_final=[]
    while linea!=[""]:
         lista_final.append(linea)
         linea=merge_fuente_unico.readline().split(";")

    return lista_final


def cantidad_de_invocaciones(lista_codigo,nombre_funcion,posicion):
     """[Autor:Luciano Solis]
        [Ayuda: Esta funcion recibe una lista anidada, un elemento de una sublista que es una funcion y una posicion de la lista anidada
       y lo que devuelve es la cantidad de veces que se invoco al elemento funcion en la lista anidada
     """
     cont_invocaciones=0
     for posicion_2 in range(len(lista_codigo)):
          for caracter_2 in range(len(lista_codigo[posicion_2])):
             if posicion!=posicion_2:
                 if nombre_funcion in lista_codigo[posicion_2][caracter_2]:
                     cont_invocaciones+=1

     return cont_invocaciones


def imprimir_diccionario(diccionario):
    for clave in diccionario:
        print(clave,": ",diccionario[clave])

#---------------------------bloque principal -----------------------------------------
archivo=open("panel_general.csv","w")
merge_fuente_unico=open("lib_matematica_codigo.csv","r")
merge_comentarios=open("lib_matematica_comentarios.csv","r")
lista_merge_fuente_unico=armado_listas_fuente_unico(merge_fuente_unico)
#lista_comentarios=armado_listas_comentarios(merge_comentarios)
contador(archivo,lista_merge_fuente_unico)
archivo.close()
print(lista_merge_fuente_unico)