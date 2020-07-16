

def armado_de_tabla(lista_merge,registro_de_invocadores,registro_de_invocaciones_de_funcion):
    """En revision"""    
    for b in registro_de_invocadores:
        print(registro_de_invocadores[b]["invoco a"],end="             ")


def armado_fila(lista_merge):
    """En revision"""
    print("funciones",end="              ")
    for i in range(1,len(lista_merge)+1):
         
         print(i,end="                "   )
    print("")     


def lista_solo_funciones(lista_merge):
    """[Autor:Luciano Solis]
       [Ayuda: recibe una lista anidada y devuelve una lista con solo la primera posicion de cada sublista de la lista anidada]
    """
    lista_solo_funciones=[]
    for i in range(len(lista_merge)):
        lista_solo_funciones.append(lista_merge[i][0])
    
    return lista_solo_funciones




def armado_listas(merge):
    """[Autor]:Luciano Solis
       [Ayuda]: Recibe un archivo y devuelve toda su informacion en una lista anidada
       
    """
    
    linea=merge.readline().strip("\n").split(";")
    lista_final=[]
    while linea!=[""]:
        lista_final.append(linea)
        linea=merge.readline().strip("\n").split(";")
    return lista_final

def invocaciones(lista_merge,archivo,lista_solo_funciones):
    """[Autor:Luciano Solis]
       [Ayuda: Recibe una lista anidada, y va recorriendo cada sublista para verificar las veces en que la funcion
       la cual se esta recorriendo invoco a las demas funciones y las veces que las demas funciones invocarion a la funcion
       a la cual estoy recorriendo]
    """
    #armado_fila(lista_merge)
    
    
    for i in range(len(lista_merge)):
        registro_de_invocadores={}
        
        for b in range(len(lista_merge[i])):
            
            if b==0:
                nombre_funcion=lista_merge[i][b]
                for c in range(len(lista_merge)):
                    cont_invocaciones=0
                    if i!=c:#esta condicion es para saber las veces que fue invocada tal funcion
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
#----------------------------------------BLOQUE PRINCIPAL-------------------------------------------------------
archivo=open("analizador.txt","w")                        
merge=open("app_matematica_codigo.csv","r")
lista_merge=armado_listas(merge)
lista_solo_funciones=lista_solo_funciones(lista_merge)
invocaciones(lista_merge,archivo,lista_solo_funciones)

#print("")
#print(lista_solo_funciones)
