# El objetivo del modulo es extraer la informacion de reutilizacion del codikgo y sus funciones
#------------------------------------------------------------------------------------------------------------
def armado_listas(merge): #aqui llega el archivo previamente mergeado (app_matematica_codigo.csv)
    """ [Autor: Luciano Solis]
        [Ayuda: Recibe un archivo csv con toda la informacion sobre las funciones ya mergeada
        y lo devuelve convertido en una lista anidada]
    """
    linea = merge.readline().strip("\n").split(";")
    lista_final = []
    while linea != [""]:
        lista_final.append(linea)
        linea = merge.readline().strip("\n").split(";")
    
    return lista_final

#---------------------------------------
def lista_solo_funciones(lista_merge):
    """ [Autor: Luciano Solis]
        [Ayuda: Recibe la lista anidada en la funcion anterior y crea una nueva lista solo con
        los nombres de las funciones]
    """
    lista_solo_funciones = []
    for i in range(len(lista_merge)):
        lista_solo_funciones.append(lista_merge[i][0])
    
    return lista_solo_funciones

#---------------------------------------
def invocaciones(lista_merge, lista_solo_funciones, archivo):
    """ [Autor: Luciano Solis]
        [Ayuda: Recibe la lista anidada con toda la informacion del modulo y la lista que solo contiene
        los nombres de las funciones y ]
    """
    #armado_fila(lista_merge)
    
    for i in range(len(lista_merge)): #aca entra lista merge
        registro_de_invocadores = {} #basicamente es un contador del largo de lista_merge
        
        for b in range(len(lista_merge[i])): #contador interno de la lista en la que esta posicionado el contador previo
            
            if b == 0: #si b es igual a cero?
                nombre_funcion = lista_merge[i][b] #aca identifica el nombre de la funcion
                for c in range(len(lista_merge)): #este es el mismo recorrido del primer i in range
                    cont_invocaciones=0
                    
                    if i != c:#esta condicion es para saber las veces que fue invocada tal funcion
                       for d in range(len(lista_merge[c])):
                            
                            if d==0:
                              invocador=lista_merge[c][d]
                            elif nombre_funcion in lista_merge[c][d]:
                                    cont_invocaciones+=1
                   
                       if invocador not in registro_de_invocadores:
                          registro_de_invocadores[invocador]={"invoco a":nombre_funcion,"cantidad de invocaciones":cont_invocaciones}
                       else:
                          registro_de_invocadores[invocador]["cantidad de invocaciones"]+=cont_invocaciones
                    
                    else: # esta es para saber la cantidad de invocaciones hizo tal funcion
                        registro_de_invocaciones_de_funcion={}
                        invocada=[]
                        lista_parcial=[]    
                       #aca entra lista_solo_funciones y se une con lista_merge
                        for funcion in lista_solo_funciones:
                            
                            cantidad=0
                            for e in range(len(lista_merge[c])):
                                if nombre_funcion!=funcion:
                                    if funcion in lista_merge[c][e] and funcion not in invocada:
                                       cantidad+=1
                                       invocada=[funcion,cantidad]
                                    elif funcion in lista_merge[c][e] and funcion in invocada:
                                        invocada[1]+=1
                                    
                                    if e==len(lista_merge[c])-1 and funcion not in invocada:
                                       invocada=[funcion,cantidad]
                            
                            if invocada!=[] and invocada not in lista_parcial:           
                                 lista_parcial.append(invocada)          
                                 
                        registro_de_invocaciones_de_funcion[nombre_funcion]=lista_parcial         
                        
        print(registro_de_invocadores) # esto representaria  la funcion de la fila que es invocada por las funciones de las columnas
        print("")
        print(registro_de_invocaciones_de_funcion)# muestra la cantidad de veces que la funcion la cual se recorrio invoco a las demas
        print("")
        print("-----------------------------------------------------------------")

#---------------------------------------
def armado_de_tabla(lista_merge,registro_de_invocadores,registro_de_invocaciones_de_funcion):
    """ [Autor: Luciano Solis]
    """     
    for b in registro_de_invocadores:
        print(registro_de_invocadores[b]["invoco a"],end="             ")

#---------------------------------------
def armado_fila(lista_merge):
    """ [Autor: Luciano Solis]
    """
    print("funciones",end="              ")
    for i in range(1,len(lista_merge)+1):
         print(i,end="                "   )
    print("")     


#----------------------------------------BLOQUE PRINCIPAL-------------------------------------------------------
archivo = open("analizador.txt","w") #crea el archivo analizador.txt
merge = open("app_matematica_codigo.csv","r") #abre el archivo app_matematica_codigo.csv en modo lectura y le da el nombre de merge

lista_merge = armado_listas(merge) #convierte el csv en una lista anidada con la informacion de todo el programa
lista_solo_funciones = lista_solo_funciones(lista_merge) #convierte la lista anidada en una lista solo con los nombres de todas las funciones
invocaciones(lista_merge, lista_solo_funciones, archivo) #analiza la lista anidada y la lista de funciones

#print("")
#print(lista_solo_funciones)

"""
Comentarios y modularizacion por Augusto Carmona
"""