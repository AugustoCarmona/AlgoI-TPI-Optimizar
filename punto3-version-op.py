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

def almacenar_datos_en_diccionarios(nombre_funcion,diccionario,lista_de_datos):
    """[Autor: Luciano Solis]
       [Ayuda: Esta funcion lo que hace es agregar datos de las invocaciones a un diccionario]
    """
    if nombre_funcion not in diccionario:
              diccionario[nombre_funcion]=lista_de_datos
    else:
              diccionario[nombre_funcion]+=lista_de_datos
              
    return diccionario

def almacenar_informacion_obtenida(total_invocaciones_a_funciones,total_invocaciones_de_funciones,registro_de_invocaciones_a_funcion,registro_de_invocaciones_de_funcion):
    """[Autor: Luciano Solis]
       [Ayuda: Esta funcion lo que hace es ir guardando la informacion obtenida en los dos diccionarios finales]
    """
    for clave in registro_de_invocaciones_a_funcion:
        
            if clave not in total_invocaciones_a_funciones:
                total_invocaciones_a_funciones[clave]=registro_de_invocaciones_a_funcion[clave]
            if clave not in total_invocaciones_de_funciones:
                total_invocaciones_de_funciones[clave]=registro_de_invocaciones_de_funcion[clave]
    
    return total_invocaciones_a_funciones,total_invocaciones_de_funciones

def invocaciones_de_funcion_a_funciones(linea_2,lista_solo_funciones,lista_merge,nombre_funcion):
        """[Autor:Luciano Solis]
           [Ayuda: Esta funcion solo es invocada cuando linea_2 y linea_1 son iguales, y lo que hace es saber las veces
           que  la variable nombre_funcion invoca a las demas funciones]
        """
        
        registro_de_invocaciones_de_funcion={} # guardo la informacion que se obtiene de la funcion que se esta recorriendo
        for funcion in lista_solo_funciones:
                invocada=[]
                cantidad=0
                for dato_3 in range(len(lista_merge[linea_2])):
                            if dato_3!=0:
                                
                                if funcion in lista_merge[linea_2][dato_3]:
                                       cantidad +=1
                                       
                if cantidad==0:
                   cantidad=""
                
                invocada+=[[funcion,cantidad]] # guardo la funcion que se recorrio con las veces que fue invocada
                registro_de_invocaciones_de_funcion=almacenar_datos_en_diccionarios(nombre_funcion,registro_de_invocaciones_de_funcion,invocada)
               
        return registro_de_invocaciones_de_funcion

def devolver_informacion_de_invocaciones(linea_1,lista_merge,nombre_funcion,total_invocaciones):
    """[Autor:Luciano Solis]
       [Ayuda: Esta funcion lo que hace es recorrer cada una de las funciones e ir obteniendo las veces que dicha funcion que se esta
       recorriendo fue e invocada por las demas funciones, y cuando dicha funcion se esta recorriendo en su propia funcion,
       se va a invocar a otra funcion para que se obtenga las veces que esa funcion invoco a las demas funciones]
    """
    
    registro_de_invocaciones_a_funcion={}# en este dic pongo los valores que se va a obtener de la funcion que se este recorriendo
    cont_total_invocaciones=0 # es contador total de las veces que fueron invocadas todas las funciones por las demas
    for linea_2 in range(len(lista_merge)):
          cont_invocaciones=0 # es para saber las veces que tal funcion invoco a la funcion que se esta recorriendo
          invocadores=[]#esta lista lo que hace es guardar al invocador y la cantidad de invocaciones
          
          for dato_2 in range(len(lista_merge[linea_2])):
                            
                   if dato_2==0: # si se cumple esta condicion significa que esta en la posicion del nombre la funcion
                      invocador=lista_merge[linea_2][dato_2]
                   
                   elif nombre_funcion in lista_merge[linea_2][dato_2]:
                      cont_invocaciones="x"#cont_invocaciones+=1 #revisar
                      cont_total_invocaciones+=1
                   
                   if cont_invocaciones==0 and dato_2==len(lista_merge[linea_2])-1:
                     cont_invocaciones=""#cont_invocaciones=""
          
          invocadores+=[[invocador,cont_invocaciones]] # guardo los datos obtenidos en la lista invocadores
          
          registro_de_invocaciones_a_funcion=almacenar_datos_en_diccionarios(nombre_funcion,registro_de_invocaciones_a_funcion,invocadores)
          
          if linea_1==linea_2:
              registro_de_invocaciones_de_funcion=invocaciones_de_funcion_a_funciones(linea_2,lista_solo_funciones,lista_merge,nombre_funcion)
    
    total_invocaciones.append(cont_total_invocaciones)#guardo el total de veces que dicha funcion fue invocada por las demas funciones en una lista
    
    return registro_de_invocaciones_a_funcion,registro_de_invocaciones_de_funcion,total_invocaciones



def juntar_informacion(lista_merge):
    """[Autor:Luciano Solis]
       [Ayuda: Recibe una lista anidada, y va recorriendo cada sublista para verificar las veces en que la funcion
       la cual se esta recorriendo invoco a las demas funciones y las veces que las demas funciones invocaron a la funcion
       a la cual estoy recorriendo, y una vez obtenida esa informacion la imprime por pantalla]
    """
    total_invocaciones_a_funciones={}
    total_invocaciones_de_funciones={}
    total_invocaciones=[] # en esta lista se guardara el total de invocaciones que tuvieron las funciones a analizar
    
    for linea_1 in range(len(lista_merge)):
        
        for dato_1 in range(len(lista_merge[linea_1])):
            
            if dato_1==0: # si se cumple esta condicion , es que dato_1 es el nombre de la funcion
                nombre_funcion=lista_merge[linea_1][dato_1]
                
                registro_de_invocaciones_a_funcion, registro_de_invocaciones_de_funcion,ultima_fila=devolver_informacion_de_invocaciones(linea_1,lista_merge,nombre_funcion,total_invocaciones)# invoco esta funcion para saber las veces que es invocada la variabla nombre_funcion que estoy recorriendo
                
        total_invocaciones_a_funciones,total_invocaciones_de_funciones=almacenar_informacion_obtenida(total_invocaciones_a_funciones,total_invocaciones_de_funciones,registro_de_invocaciones_a_funcion,registro_de_invocaciones_de_funcion)
        
        
    return ultima_fila,total_invocaciones_a_funciones,total_invocaciones_de_funciones


def tamaño_primer_columna(lista_solo_funciones):
    """[Autor":Luciano Solis]
       [Ayuda: Esta funcion recibe la lista que solo contiene los nombres de las funciones y lo que hace  es encontrar la palabra
       mas larga.A esto a la lista se le agrega dos strings, una dice funciones y la otra dice total invocaciones, ya que estas
       van a ser parte de la primer columna]
       
    """
    maximo_primer_columna=0
    adicionales=0
    lista_solo_funciones_nueva=lista_solo_funciones +["funciones","total invocaciones"]
    for funcion in lista_solo_funciones_nueva:
      
      if funcion!="funciones" and funcion!="total invocaciones":
          adicionales+=1
          funcion=str(adicionales)+"."+funcion
        
      if len(funcion)>maximo_primer_columna:
        maximo_primer_columna=len(funcion) # la variable maximo va a ser un valor, y ese valor es la longitud de la funcion mas larga
    
    return maximo_primer_columna 

def tamaño_columnas_de_datos(ultima_fila,lista_solo_funciones):
    """[Autor: Luciano Solis]
       [Ayuda: Esta funcion lo que hace es encontrar el valor mas grande de la ultima fila ya que esta nos va a dar el tamaño
       que se necesita para todas las columnas, excpeto la primer columna que es de nombre de funciones]
    """
    maximo_columna_datos=max(ultima_fila) #con el max encuentro el valor mas grande que pertenece a ultima_fila, y esta como dato tiene la suma total de las invocaciones que se le hace a cada funcion
    maximo_columna_datos=str(maximo_columna_datos)
    
    contador_columna_de_datos=0# este contador va a guardar el valor del tamaño de las columnas,excepto la primer columna.
    for i in ultima_fila:
            i=str(i)
            while len(i)<len(maximo_columna_datos):
                i+=" "
            contador_columna_de_datos+=len(" "+i+"|")# con esto tengo todo el tamaño de las columnas de datos, menos la primer columna
    
    return contador_columna_de_datos, maximo_columna_datos #este el tamañano maximo de las columnas de los datos

                       #contador_1
def tamaño_fila(maximo_primer_columna,contador_columna_de_datos):
    """[Autor: Luciano Solis]
       [Ayuda: Esta funcion lo que hace es encontrar el ancho total de la tabla,y ese ancho lo vamos a mostrar en
       forma de guiones, para eso, lo que hacemos
       es sumar el ancho de la columna de la primer fila con el ancho restante de columnas
    """
    suma_de_columnas_totales=maximo_primer_columna+2 + contador_columna_de_datos # sumo la columna mas grande de las funciones con la columna total de los datos, tambien le sumo dos debido a que cuando lo muestro por pantalla le agregue dos palitos
    guiones_totales=""
    for guiones in range(suma_de_columnas_totales):
           guiones_totales+="-"
    
    return guiones_totales
    


def generar_primer_columna(variable,maximo_primer_columna):
    """[Autor:Luciano Solis]
       [Ayuda: Esta funcion solo recibe al primer valor de cada fila, es decir, a la primer columa de cada fila,y lo que hace
       es comparar dichos valores con el valor maximo que se habia calculado. Esto se hace para que todas las primer columnas
       tengan el mismo ancho,y por ultimo, lo muesta por pantalla]
    """
    variable=str(variable)
    while len(variable)<maximo_primer_columna:
        variable+=" "
    print("|"+variable+"|",end="")
    
    return variable
    
def generar_columna_para_datos(columna_de_datos,maximo_columna_datos):
    """[Autor:Luciano Solis]
       [Ayuda: Esta funcion lo que hace, es recibir como parametro el tamaño de las columnas, excepto la primera,
       y lo que hace es calibrar cada valor a cierta medida especifica para que todas tenga el mismo ancho de columnas]
    """
    columna_de_datos=str(columna_de_datos)
    while len(columna_de_datos)<len(str(maximo_columna_datos)):
        columna_de_datos+=" "
    print(" "+columna_de_datos+"|",end="")
    
    return columna_de_datos

def procesar_primer_fila(lista_solo_funciones,archivo):
    """[Autor:Luciano Solis]
       [Ayuda: Esta funcion lo que hace es imprimir la primer fila, para esto se invoca a dos funciones, una para calibrar el ancho de la primer
       columna y la otra para calibrar en ancho de las columnas restantes]
    """   
    primer_columna=generar_primer_columna("funciones",maximo_primer_columna)
    archivo.write(primer_columna+"|")
    for i in range(1,len(lista_solo_funciones)+1):
        columna_de_datos=generar_columna_para_datos(i,maximo_columna_datos)
        archivo.write(columna_de_datos+"|")
    
    archivo.write("\n")

def comparacion_entre_valores(total_invocaciones_a_funciones,diccionario_2,clave,posicion,archivo):
                """[Autor: Luciano Solis]
                   [Ayuda: Esta funcion lo que hace es comparar los valores que hay en los dos diccionarios para decidir
                   cual se va a mostrar en la tabla]
                """
                if diccionario_2[clave][posicion][1]=="" and total_invocaciones_a_funciones[clave][posicion][1]=="":
                          columna_de_datos=generar_columna_para_datos(diccionario_2[clave][posicion][1],maximo_columna_datos) 
                          archivo.write(str(columna_de_datos)+"|")
                
                elif total_invocaciones_a_funciones[clave][posicion][1]=="x" and diccionario_2[clave][posicion][1]=="":
                          columna_de_datos=generar_columna_para_datos(total_invocaciones_a_funciones[clave][posicion][1],maximo_columna_datos)
                          archivo.write(str(columna_de_datos)+"|")
                
                elif total_invocaciones_a_funciones[clave][posicion][1]=="" and diccionario_2[clave][posicion][1]>0:
                          columna_de_datos=generar_columna_para_datos(diccionario_2[clave][posicion][1],maximo_columna_datos)
                          archivo.write(str(columna_de_datos)+"|")
                

def procesar_filas_para_funciones(total_invocaciones_a_funciones, total_invocaciones_de_funciones,archivo):
    """[Autor:Luciano Solis]
       [Ayuda:Esta funcion recibe dos diccionarios que contienen toda la informacion que se necesita para mostrar por tabla
       y guardarlo en el archivo.]
    """
    numero_de_funcion=0
    for clave in total_invocaciones_de_funciones:
              numero_de_funcion+=1
              
              primer_columna=generar_primer_columna(str(numero_de_funcion)+"."+clave,maximo_primer_columna)
              archivo.write(primer_columna+"|")
              for posicion in range(len(total_invocaciones_de_funciones[clave])):
                
                
                comparacion_entre_valores(total_invocaciones_a_funciones,total_invocaciones_de_funciones,clave,posicion,archivo)
                
              archivo.write("\n")
              print("")  



def procesar_ultima_fila(archivo):
    """[Autor:Luciano Solis]
       [Ayuda: Esta funcion recibe una lista que contiene las invocacionces total que tuvo cada funcion a analizar, ordenada de la misma
       forma que los dos diccionarios, y se invoca a dos funciones, la de calibrar el ancho de la primer columna y la de calibrar
       el ancho de las columnas restantes, y por ultimo lo muestra por pantalla]
    """
    primer_columna=generar_primer_columna("total invocaciones",maximo_primer_columna)
    archivo.write(primer_columna+"|")
    for total_invocaciones in ultima_fila:
        columna_de_datos=generar_columna_para_datos(total_invocaciones,maximo_columna_datos)#generar_columna_a_caracter(total_invocaciones,maximo)
        archivo.write(str(columna_de_datos+"|"))

def procesar_total_invocaciones():
    """[Autor: Luciano Solis]
       [Ayuda: Esta funcion lo que hace es mostrar toda la informacion que se obtuvo en formato tabla]
    """
    
    procesar_primer_fila(lista_solo_funciones,archivo)
    print("")
    procesar_filas_para_funciones(total_invocaciones_a_funciones, total_invocaciones_de_funciones,archivo)
    procesar_ultima_fila(archivo)

#----------------------------------------BLOQUE PRINCIPAL-------------------------------------------------------
archivo=open("analizador.txt","w")                      
merge=open("app_matematica_codigo.csv","r")
lista_merge=armado_listas(merge)
lista_solo_funciones=lista_solo_funciones(lista_merge)
maximo_primer_columna=tamaño_primer_columna(lista_solo_funciones)
ultima_fila,total_invocaciones_a_funciones,total_invocaciones_de_funciones=juntar_informacion(lista_merge)
contador_columna_de_datos, maximo_columna_datos=tamaño_columnas_de_datos(ultima_fila,lista_solo_funciones)
guiones_totales=tamaño_fila(maximo_primer_columna,contador_columna_de_datos)              
print(guiones_totales)
procesar_total_invocaciones()
print("")                                                                                                                                                
print(guiones_totales)
archivo.close()
