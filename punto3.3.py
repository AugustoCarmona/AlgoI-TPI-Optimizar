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


def lista_solo_funciones(lista_merge):
    """[Autor:Luciano Solis]
       [Ayuda: recibe una lista anidada y devuelve una lista con solo la primera posicion de cada sublista de la lista anidada]
    """
    lista_solo_funciones=[]
    for i in range(len(lista_merge)):
        lista_solo_funciones.append(lista_merge[i][0])
    
    return lista_solo_funciones


def invocaciones_funciones_a_funcion(linea_1,registro_de_invocadores,lista_merge,nombre_funcion,total_invocaciones):
    """[Autor:Luciano Solis]
       [Ayuda: Esta funcion lo que hace es recorrer cada una de las funciones e ir obteniendo las veces que dicha funcion que se esta
       recorriendo fue e invocada por las demas funciones, y cuando dicha funcion se esta recorriendo en su propia funcion,
       se va a invocar a otra funcion para que se obtenga las veces que esa funcion invoco a las demas funciones]
    """
    cont_total_invocaciones=0
    for linea_2 in range(len(lista_merge)):
          cont_invocaciones=0
          invocadores=[]
          
          for dato_2 in range(len(lista_merge[linea_2])):
                            
                   if dato_2==0: # si se cumple esta condicion significa que esta en la posicion del nombre la funcion
                      invocador=lista_merge[linea_2][dato_2]
                   elif nombre_funcion in lista_merge[linea_2][dato_2]:
                      cont_invocaciones="x"#cont_invocaciones+=1 #revisar
                      cont_total_invocaciones+=1
                   if cont_invocaciones==0 and dato_2==len(lista_merge[linea_2])-1:
                      cont_invocaciones=""#cont_invocaciones=""
          invocadores+=[[invocador,cont_invocaciones]]
          
          if nombre_funcion not in registro_de_invocadores:
                      registro_de_invocadores[nombre_funcion]=invocadores
          else:
              registro_de_invocadores[nombre_funcion]+=invocadores
          #if dato_2==len(lista_merge[linea_2])-1 and linea_2==len(lista_merge)-1:
          if linea_1==linea_2:
              registro_de_invocaciones_de_funcion=invocaciones_de_funcion_a_funciones(linea_2,lista_solo_funciones,lista_merge,nombre_funcion)
    total_invocaciones.append(cont_total_invocaciones)
    
    return registro_de_invocadores,registro_de_invocaciones_de_funcion,total_invocaciones


        

def invocaciones_de_funcion_a_funciones(linea_2,lista_solo_funciones,lista_merge,nombre_funcion):
        """[Autor:Luciano Solis]
           [Ayuda: Esta funcion solo es invocada cuando linea_2 y linea_1 son igual, y lo que hace es saber las veces
           que  la variable nombre_funcion invoca a las demas funciones]
        """
        total_invocaciones=[]
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


def juntar_informacion(lista_merge,lista_solo_funciones):
    """[Autor:Luciano Solis]
       [Ayuda: Recibe una lista anidada, y va recorriendo cada sublista para verificar las veces en que la funcion
       la cual se esta recorriendo invoco a las demas funciones y las veces que las demas funciones invocaron a la funcion
       a la cual estoy recorriendo, y una vez obtenida esa informacion la imprime por pantalla]
    """
    
    total_invocaciones=[]
    diccionario_1={}
    diccionario_2={}
    
    
    total_invocaciones=[]
    numero_de_funcion=0
    for linea_1 in range(len(lista_merge)):
        registro_de_invocadores={}
        
        for dato_1 in range(len(lista_merge[linea_1])):
            
            if dato_1==0: # si se cumple esta condicion , es que dato_1 es el nombre de la funcion
                nombre_funcion=lista_merge[linea_1][dato_1]
                #numero_de_funcion+=1
                registro_de_invocadores, registro_de_invocaciones_de_funcion,ultima_fila=invocaciones_funciones_a_funcion(linea_1,registro_de_invocadores,lista_merge,nombre_funcion,total_invocaciones)# invoco esta funcion para saber las veces que es invocada la variabla nombre_funcion que estoy recorriendo
        for clave in registro_de_invocadores:
            if clave not in diccionario_1:
                diccionario_1[clave]=registro_de_invocadores[clave]
            if clave not in diccionario_2:
                diccionario_2[clave]=registro_de_invocaciones_de_funcion[clave]
        
        
             
        print("")
        
    
    
    return ultima_fila,diccionario_1,diccionario_2


def tamaño_primer_columna(lista_solo_funciones):
    """[Autor":Luciano Solis]
       [Ayuda: Esta funcion recibe la lista que solo contiene los nombres de las funciones y lo que hace  es encontrar la palabra
       mas larga.A esto a la lista se le agrega dos strings, una dice funciones y la otra dice total invocaciones, ya que estas
       van a ser parte de la primer columna]
       
    """
    maximo=0
    adicionales=0
    lista_solo_funciones_nueva=lista_solo_funciones +["funciones","total invocaciones"]
    for funcion in lista_solo_funciones_nueva:
      
      if funcion!="funciones" and funcion!="total invocaciones":
          adicionales+=1
          funcion=str(adicionales)+"."+funcion
        
      if len(funcion)>maximo:
        maximo=len(funcion) # la variable maximo va a ser un valor, y ese valor es la longitud de la funcion mas larga
    
    return maximo 

def tamaño_columnas_de_datos(ultima_fila,lista_solo_funciones):
    """[Autor: Luciano Solis]
       [Ayuda: Esta funcion lo que hace es encontrar el valor mas grande de la ultima fila ya que esta nos va a dar el tamaño
       que se necesita para todas las columnas, excpeto la primer columna que es de nombre de funciones]
    """
    maximo_2=max(ultima_fila) #con el max encuentro el valor mas grande que pertenece a ultima_fila, y esta como dato tiene la suma total de las invocaciones que se le hace a cada funcion
    maximo_2=str(maximo_2)
    
    contador_columna_de_datos=0# este contador va a guardar el valor del tamaño de las columnas,excepto la primer columna.
    for i in ultima_fila:
            i=str(i)
            while len(i)<len(maximo_2):
                i+=" "
            contador_columna_de_datos+=len(" "+i+"|")# con esto tengo todo el tamaño de las columnas de datos, menos la primer columna
    
    return contador_columna_de_datos, maximo_2#este el tamañano maximo de las columnas de los datos

                       #contador_1
def tamaño_fila(maximo,contador_columna_de_datos):
    """[Autor: Luciano Solis]
       [Ayuda: Esta funcion lo que hace es encontrar el ancho total de la tabla,y ese ancho lo vamos a mostrar en
       forma de guiones, para eso, lo que hacemos
       es sumar el ancho de la columna de la primer fila con el ancho restante de columnas
    """
    suma_de_columnas_totales=maximo+2 + contador_columna_de_datos # sumo la columna mas grande de las funciones con la columna total de los datos, tambien le sumo dos debido a que cuando lo muestro por pantalla le agregue dos palitos
    guiones_totales=""
    for guiones in range(suma_de_columnas_totales):
           guiones_totales+="-"
    return guiones_totales
    


def generar_columna_a_caracter(variable,maximo_primer_columna):
    """[Autor:Luciano Solis]
       [Ayuda: Esta funcion solo recibe al primer valor de cada fila, es decir, a la primer columa de cada fila,y lo que hace
       es comparar dichos valores con el valor maximo que se habia calculado. Esto se hace para que todas las primer columnas
       tengan el mismo ancho,y por ultimo, lo muesta por pantalla]
    """
    variable=str(variable)
    while len(variable)<maximo_primer_columna:
        variable+=" "
    print("|"+variable+"|",end="")
                                              
def generar_columna_para_datos(columna_de_datos,maximo_2):
    """[Autor:Luciano Solis]
       [Ayuda: Esta funcion lo que hace, es recibir como parametro el tamaño de las columnas, excepto la primera,
       y lo que hace es calibrar cada valor a cierta medida especifica para que todas tenga el mismo ancho de columnas]
    """
    columna_de_datos=str(columna_de_datos)
    while len(columna_de_datos)<len(str(maximo_2)):
        columna_de_datos+=" "
    print(" "+columna_de_datos+"|",end="")

def imprimir_primer_fila(lista_solo_funciones,maximo_2,maximo_primer_columna):
    """[Autor:Luciano Solis]
       [Ayuda: Esta funcion lo que hace es imprimir la primer fila, para esto se invoca a dos funciones, una para calibrar el ancho de la primer
       columna y la otra para calibrar en ancho de las columnas restantes]
    """   
    generar_columna_a_caracter("funciones",maximo_primer_columna)#generar_columna_para_datos("funciones",maximo_2)
    for i in range(1,len(lista_solo_funciones)+1):
        generar_columna_para_datos(i,maximo_2)#generar_columna_a_caracter(i,maximo)


def imprimir_filas_para_funciones(diccionario_1, diccionario_2,maximo_primer_columna,maximo_2):
    """[Autor:Luciano Solis]
       [Ayuda:Esta funcion recibe dos diccionarios que contienen toda la informacion que se necesita para mostrar por tabla
       para lograr esto lo que se hace es recorrer uno de los dos diccionarios, no importa cual, ya que estan ordenados de la misma
       forma, las claves son las funciones a analizar.Para ir imprimiendo invoco a dos funciones, la de calibrar el ancho de la primer
       columna y la de calibrar el ancho de las columnas restantes]
    """
    numero_de_funcion=0
    for clave in diccionario_2:
              numero_de_funcion+=1
              
              generar_columna_a_caracter(str(numero_de_funcion)+"."+clave,maximo_primer_columna)
              for posicion in range(len(diccionario_2[clave])):
                
                
                if diccionario_2[clave][posicion][1]=="" and diccionario_1[clave][posicion][1]=="":
                          generar_columna_para_datos(diccionario_2[clave][posicion][1],maximo_2) #generar_columna_a_caracter(diccionario_2[clave][posicion][1],maximo)
                         
                elif diccionario_1[clave][posicion][1]=="x" and diccionario_2[clave][posicion][1]=="":
                          generar_columna_para_datos(diccionario_1[clave][posicion][1],maximo_2)#generar_columna_a_caracter(diccionario_1[clave][posicion][1],maximo)
                      
                elif diccionario_1[clave][posicion][1]=="" and diccionario_2[clave][posicion][1]>0:
                          generar_columna_para_datos(diccionario_2[clave][posicion][1],maximo_2)#generar_columna_a_caracter(diccionario_2[clave][posicion][1],maximo)
    
              print("")  



def imprimir_ultima_fila(ultima_fila,maximo_primer_columna):
    """[Autor:Luciano Solis]
       [Ayuda: Esta funcion recibe una lista que contiene las invocacionces total que tuvo cada funcion a analizar, ordenada de la misma
       forma que los dos diccionarios, y se invoca a dos funciones, la de calibrar el ancho de la primer columna y la de calibrar
       el ancho de las columnas restantes, y por ultimo lo muestra por pantalla]
    """
    generar_columna_a_caracter("total invocaciones",maximo_primer_columna)
    for total_invocaciones in ultima_fila:
        generar_columna_para_datos(total_invocaciones,maximo_primer_columna)#generar_columna_a_caracter(total_invocaciones,maximo)
    

def imprimir_total_invocaciones(ultima_fila,diccionario_1,diccionario_2,maximo_primer_columna,maximo_2,lista_solo_funciones):
    """[Autor: Luciano Solis]
       [Ayuda: Esta funcion lo que hace es mostrar toda la informacion que se obtuvo en formato tabla]
    """
    
    imprimir_primer_fila(lista_solo_funciones,maximo_2,maximo_primer_columna)
    print("")
    imprimir_filas_para_funciones(diccionario_1, diccionario_2,maximo_primer_columna,maximo_2)
    imprimir_ultima_fila(ultima_fila,maximo_primer_columna)
#----------------------------------------BLOQUE PRINCIPAL-------------------------------------------------------
#archivo=open("analizador.txt","w")  solo falta agregar la informacion obtenida a este archivo!!!!                     
merge=open("app_matematica_codigo.csv","r")
lista_merge=armado_listas(merge)
lista_solo_funciones=lista_solo_funciones(lista_merge)
maximo_primer_columna=tamaño_primer_columna(lista_solo_funciones)
ultima_fila,diccionario_1,diccionario_2=juntar_informacion(lista_merge,lista_solo_funciones)
contador_columna_de_datos, maximo_2=tamaño_columnas_de_datos(ultima_fila,lista_solo_funciones)
guiones_totales=tamaño_fila(maximo_primer_columna,contador_columna_de_datos)              #contador_1
print(guiones_totales)
imprimir_total_invocaciones(ultima_fila,diccionario_1,diccionario_2,maximo_primer_columna,maximo_2,lista_solo_funciones)
print("")                                                                                   #contador_columna_de_datos reemplazado por maximo_2                                                              
print(guiones_totales)

#print("")
#print(lista_solo_funciones)