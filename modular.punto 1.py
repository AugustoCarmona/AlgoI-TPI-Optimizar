def nombre_funcion(linea,posicion_cod):
    
    N_funcion = ""
    
    if posicion_cod == 0 :
        
        N_funcion = linea
    
    
    return N_funcion
    
    
    
def nombre_modulo(linea,posicion_cod):
    
    N_modulo = ""
    
    if  posicon_cod == 2:
        
        N_nombre = linea
    
    
    
def contar_for(linea):
    
    cont_for = 0
    
    if "for" in linea:
        
        cont_for +=1
        
    return cont_for

def contar_lineas(linea,posicion_cod):
    
    cont_lineas = 0
    
    if posicion_cod > 2 and linea != "":
        cont_lineas +=1
        

def contar_parametros (linea,posicion_cod):
    
    cont_parametro = 0
    
    if posicion_cod  == 1:
        
        cont_comas =linea.count(",")
        
        if cont_comas != 0:
            cont_parametros = 1 + cont_comas
            
        else:
            cont_parametros = cont_comas
            
            
    return cont_parametros


def contar_if (linea):
    
    
    if "if " in linea or  "elif" in linea:
        
        cont_if  +=1
        
    return cont_lineas


def contar_while (linea):
    
    cont_while = 0
    
    if  "while" in linea :
        
        cont_while +=1
        
    return cont_while
        



def comentarios(linea):
    
    ayuda ="S/A"
    
    cont_comentarios = 0
    
    if "ayuda" in linea:
        
        ayuda ="SI"
    
    elif ayuda = "SI" and linea[0].isupper() and not "ayuda" in linea:
        
        cont_comentarios +=1
        
    return cont_parametros,ayuda


def autor(linea):
    
    autor = "NO"
    
    if "autor" in linea:
        
        autor = linea[linea.index(":"):linea.index("]")]
        
    return autor

def contar_break(linea):
    
    cont_brike = 0
    
    if "brike" in linea:
        
        cont_brike +=1
        
    return cont_brike



def contar_exit():
    
    cont_exit = 0
    
    if  "exit" in linea :
        
        cont_exit +=1
        
    return cont_exit

def escribir(archivo,lista_codigo):
    
    
    posicion = 0
    
    while posicion < len (lista_codigo):
        
        for caracter in len (range(lista_codigo[posicion])):
            
            
            nombre_funcion = contar_lineas(lista_codigo[posicon][caracter],caracter)
            nombre_modulo = contar_lineas(lista_codigo[posicon][caracter],caracter)
            cont_lineas = contar_lineas(lista_codigo[posicon][caracter],caracter)
            cont_parametros = contar_lineas(lista_codigo[posicon][caracter],caracter)
            cont_while = contar_lineas(lista_codigo[posicon][caracter])
            cont_for = contar_lineas(lista_codigo[posicon][caracter])
            cont_if = contar_lineas(lista_codigo[posicon][caracter])
            cont_exit = contar_lineas(lista_codigo[posicon][caracter])
            cont_brike = contar_lineas(lista_codigo[posicon][caracter])
            
    
    




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
             if posicion_2!=caracter_2:
                 if nombre_funcion in lista_codigo[posicion_2][caracter_2]:
                     cont_invocaciones+=1

     return cont_invocaciones


#def imprimir_diccionario(diccionario):
    #print()
    #for clave in diccionario:
        #print(clave,": ",diccionario[clave])

#---------------------------bloque principal -----------------------------------------
archivo=open("panel_general.csv","w")
merge_fuente_unico=open("lib_matematica_codigo.csv.txt","r")
merge_comentarios=open("lib_matematica_comentarios.csv.txt","r")
lista_merge_fuente_unico=armado_listas_fuente_unico(merge_fuente_unico)
#lista_comentarios=armado_listas_comentarios(merge_comentarios)
contador(archivo,lista_merge_fuente_unico)
archivo.close()