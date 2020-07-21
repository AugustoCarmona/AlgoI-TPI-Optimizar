def juntar_informacion(linea_1,lista_merge,nombre_funcion,registro_de_invocadores):
    """[Autor: Luciano Solis]
       [Ayuda:Esta funcion lo que hace es devolver las invocaciones de la funcion que se esta recorriendo a las demas funciones,
       y las invocaciones de las demas a funciones a la funcion que se esta recorriendo]
    """
    for linea_2 in range(len(lista_merge)):
        #cont_invocaciones=0
        #if linea_1!=linea_2:#esta condicion es para saber si son diferentes la linea, asi no corro la misma linea, ya que seria innecesario.
        registro_de_invocadores=invocaciones_a_funcion(linea_2,registro_de_invocadores,lista_merge,nombre_funcion)
            
                      
                      
        if linea_1==linea_2:#else:# esta condicion entra cuando linea_1 es igual a linea_2
            registro_de_invocaciones_de_funcion=invocaciones_de_funcion_a_funciones(linea_2,lista_solo_funciones,lista_merge,nombre_funcion)
            
    return registro_de_invocadores, registro_de_invocaciones_de_funcion


def invocaciones_a_funcion(linea_2,registro_de_invocadores,lista_merge,nombre_funcion):
          """[Autor: Luciano Solis]
             [Ayuda: Esta funcion lo que hace es juntar la informacion necesaria para saber las veces que la funcion
             que se esta recorriendo es invocada por las demas funciones]
          """
          cont_invocaciones=0
          invocadores=[]
          for dato_2 in range(len(lista_merge[linea_2])):
                            
                   if dato_2==0: # si se cumple esta condicion significa que esta en la posicion del nombre la funcion
                      invocador=lista_merge[linea_2][dato_2]
                   elif nombre_funcion in lista_merge[linea_2][dato_2]:
                      cont_invocaciones="x"#cont_invocaciones+=1 #revisar
                   if cont_invocaciones==0 and dato_2==len(lista_merge[linea_2])-1:
                      cont_invocaciones=""#cont_invocaciones=""
          invocadores+=[[invocador,cont_invocaciones]]
          if nombre_funcion not in registro_de_invocadores:
                      registro_de_invocadores[nombre_funcion]=invocadores
          else:
              registro_de_invocadores[nombre_funcion]+=invocadores
          
        
          return registro_de_invocadores
        

def invocaciones_de_funcion_a_funciones(linea_2,lista_solo_funciones,lista_merge,nombre_funcion):
        """[Autor:Luciano Solis]
           [Ayuda: Esta funcion solo es invocada cuando linea_2 y linea_1 son igual, y lo que hace es saber las veces
           que la la variable nombre_funcion invoca a las demas funciones]
        """
        registro_de_invocaciones_de_funcion={}
        for funcion in lista_solo_funciones:
                invocada=[]
                cantidad=0
                for dato_3 in range(len(lista_merge[linea_2])):
                            if dato_3!=0:#if nombre_funcion!=funcion:
                                
                                if funcion in lista_merge[linea_2][dato_3]:
                                       cantidad +=1
                                       
                                    
                                       
                if cantidad==0:
                   cantidad=""
                invocada+=[[funcion,cantidad]]
                if nombre_funcion not in registro_de_invocaciones_de_funcion:
                    registro_de_invocaciones_de_funcion[nombre_funcion]=invocada
                                        
                else:
                     registro_de_invocaciones_de_funcion[nombre_funcion]+=invocada
        
        
        return registro_de_invocaciones_de_funcion

def armado_de_tabla(lista_merge,registro_de_invocadores,registro_de_invocaciones_de_funcion):
    """[Autor:Luciano Solis]
           [Ayuda: 
        ]      
    """
    """En revision"""    
    for b in registro_de_invocadores:
        print(registro_de_invocadores[b]["invoco a"],end="             ")


def armado_fila(lista_merge):
    """[Autor:Luciano Solis]
           [Ayuda: 
        ]      
    """
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

def generador_columnas_y_guiones(lista_solo_funciones):
    """[Autor":Luciano Solis]
       [Ayuda: Esta funcion recibe la lista que solo contiene los nombres de las funciones y lo que hace es calibar el ancho necesario
       para las columnas y la cantidad de guiones para el tamaño de la fila]
    """
    maximo=0
    lista_solo_funciones_nueva=lista_solo_funciones +["funciones"]
    for funciones_nuevas in lista_solo_funciones_nueva:
      if len(funciones_nuevas)>maximo:
        maximo=len(funciones_nuevas)
    contador_final=0
    for funciones_nuevas in lista_solo_funciones_nueva:
       while len(funciones_nuevas)<maximo:
           funciones_nuevas+=" "
       contador_final+=len("|"+b+"|")
    
    espacios=""
    for ciclo_de_contador in  range(contador_final):
        espacios+="-"
    
        
    return maximo,espacios

def imprimir_invocaciones(lista_merge,lista_solo_funciones,maximo,espacios):
    """[Autor:Luciano Solis]
       [Ayuda: Recibe una lista anidada, y va recorriendo cada sublista para verificar las veces en que la funcion
       la cual se esta recorriendo invoco a las demas funciones y las veces que las demas funciones invocaron a la funcion
       a la cual estoy recorriendo, y una vez obtenida esa informacion la imprime por pantalla]
    """
    #armado_fila(lista_merge)
    print(espacios)
    funciones="funciones"
    while len(funciones)<maximo:
        funciones+= " "
    print("|"+funciones+"|",end="")
    
    for i in range(1,len(lista_solo_funciones)+1):
        i=str(i)
        while len(i)<maximo:
            i+= " "
        print(" "+i+"|",end="")
    print("")
    print(espacios)
    for linea_1 in range(len(lista_merge)):
        registro_de_invocadores={}
        
        for dato_1 in range(len(lista_merge[linea_1])):
            
            if dato_1==0: # si se cumple esta condicion , es que dato_1 es el nombre de la funcion
                nombre_funcion=lista_merge[linea_1][dato_1]
                registro_de_invocadores, registro_de_invocaciones_de_funcion=juntar_informacion(linea_1,lista_merge,nombre_funcion,registro_de_invocadores)# invoco esta funcion para saber las veces que es invocada la variabla nombre_funcion que estoy recorriendo
        
        while len(nombre_funcion)<maximo:
            nombre_funcion+=" "
        print("|"+nombre_funcion+"|",end="")
        
        
        #print(registro_de_invocadores) # esto representaria  la funcion de la fila que es invocada por las funciones de las columnas
        #print("")
        #print(registro_de_invocaciones_de_funcion)# muestra la cantidad de veces que la funcion la cual se recorrio invoco a las demas
        #print("")
        #print("-----------------------------------------------------------------")
        
        for clave in registro_de_invocaciones_de_funcion:
              
              
              for posicion in range(len(registro_de_invocaciones_de_funcion[clave])):
                """
                print(registro_de_invocaciones_de_funcion[clave][posicion],end="")
                print(registro_de_invocadores[clave][posicion])
                """
                if registro_de_invocaciones_de_funcion[clave][posicion][1]=="" and registro_de_invocadores[clave][posicion][1]=="":
                           caracter=str(registro_de_invocaciones_de_funcion[clave][posicion][1])
                           while len(caracter)<maximo:
                               caracter+=" "
                           print(" "+caracter+"|",end="")
                elif registro_de_invocadores[clave][posicion][1]=="x" and registro_de_invocaciones_de_funcion[clave][posicion][1]=="":
                           caracter=str(registro_de_invocadores[clave][posicion][1])
                           while len(caracter)<maximo:
                               caracter+=" "
                           print(" "+caracter+"|",end="")
                elif registro_de_invocadores[clave][posicion][1]=="" and registro_de_invocaciones_de_funcion[clave][posicion][1]>0:
                           caracter=str(registro_de_invocaciones_de_funcion[clave][posicion][1])
                           while len(caracter)<maximo:
                               caracter+=" "
                           print(" "+caracter+"|",end="")
                     
          
        print("")
        print(espacios)
  
#----------------------------------------BLOQUE PRINCIPAL-------------------------------------------------------
#archivo=open("analizador.txt","w")                        
merge=open("app_matematica_codigo.csv","r")
lista_merge=armado_listas(merge)
lista_solo_funciones=lista_solo_funciones(lista_merge)
maximo,espacios=generador_columnas_y_guiones(lista_solo_funciones)
imprimir_invocaciones(lista_merge,lista_solo_funciones,maximo,espacios)

#print("")
#print(lista_solo_funciones)

