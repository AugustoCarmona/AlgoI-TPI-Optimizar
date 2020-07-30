def obtener_informacion(): #invocada desde main()
    """ [Autor: Augusto Carmona, Jose Piñeiro]
        [Ayuda: abre el archivo fuente_unico y extrae el codigo de cada funcion y su nombre el cual
        evaluara con la funcion procesar_diccionario() que nos dara  los datos necesarios para armar
        el diagrama de arbol]
    """
    codigos = open("data\\fuente_unico.csv","r")
    linea = codigos.readline().split(";")
    funciones = {}
    
    while(linea != [""]): #extrae el crudo del archivo fuente_unico.csv
        funciones[linea[0]]=linea[3:]
        linea = codigos.readline().split(";")
    codigos.close()

    diccionario_final = procesar_diccionario(funciones) #procesa fuente_unico.csv y le da el formato necesitado
    
    return diccionario_final

#------------------------------------------------------------
def procesar_diccionario(funciones): #invocada desde obtener_informacion()
    """ [Autor: Augusto Carmona, Jose Piñeiro]
        [Ayuda: extrae cuantas lineas de codigo hay en cada funcion e invoca a evaluador_invocaciones() para evaluar
        cuantas invocaciones genera]
    """
    cantidad_lineas = {}
    llamados = {}
    
    for funcion in funciones:
        cantidad_lineas[funcion] = [len(funciones[funcion])] #cantidad de lineas de codigo de la funcion
    
    for funcion in cantidad_lineas:
        evaluador_invocaciones(funcion, funciones, llamados)
        
    
    diccionario_unido = diccionario_unificado(llamados,cantidad_lineas)
    
    return diccionario_unido

#------------------------------------------------------------
def evaluador_invocaciones(funcion, funciones, llamados): #invocada desde procesar diccionario()
    """ [Autor: Augusto Carmona, Jose Piñeiro]
        [Ayuda: extrae cuantas invoaciones genra cada funcion]
    """
    for linea in funciones:
        index = 0
        
        while index < len(funciones[linea]):
            sub_modulos = funciones[linea][index]
            if funcion in sub_modulos:
                veces_que_aparece =  sub_modulos.count(funcion)
                lugar_antiguo = 0
                for veces in range(0,veces_que_aparece):
                    buscador = 0
                    lugar_primera_letra_funcion = sub_modulos[lugar_antiguo:].find(funcion) + lugar_antiguo
                    if ((not sub_modulos[lugar_primera_letra_funcion-1].isalnum) or (not sub_modulos[lugar_primera_letra_funcion-1]== "_")) and ((not sub_modulos[lugar_primera_letra_funcion + len(funcion)].isalnum) or (not sub_modulos[lugar_primera_letra_funcion+ len(funcion)]== "_")):
                        es_funcion = "puede ser"
                        while es_funcion == "puede ser" or buscador == (len (sub_modulos)- (lugar_primera_letra_funcion + len(funcion))):
                            if sub_modulos[lugar_primera_letra_funcion + len(funcion) + buscador] == "(":
                                es_funcion = "si"
                                if not linea in llamados:
                                    llamados[linea] = [[funcion]]
                                else: llamados[linea][0].append(funcion)

                            elif (not sub_modulos[lugar_primera_letra_funcion + len(funcion) + buscador] == " "):
                                es_funcion = "no"
                            elif sub_modulos[lugar_primera_letra_funcion + len(funcion) + buscador] == " ":
                                buscador +=1
                    if (len(sub_modulos) > (lugar_primera_letra_funcion + len(funcion)+1)):
                        if (not sub_modulos[lugar_primera_letra_funcion + len(funcion)] == funcion[0]):
                            lugar_antiguo = lugar_primera_letra_funcion+1
                    else:
                        lugar_antiguo = lugar_primera_letra_funcion
            index += 1
    return llamados
#------------------------------------------------------------
def diccionario_unificado(llamados, cantidad_lineas): #invocada desde procesar_diccionario()
    """ [Autor: Augusto Carmona, Jose Piñeiro]
        [Ayuda: da estructura final al diccionario de funciones]
    """
    funciones_no_llamadas = []
    lista_final = llamados
    
    for funcion in cantidad_lineas:
        funciones_no_llamadas.append(funcion)
    
    for funciones_que_llaman in llamados:
        lista_final[funciones_que_llaman].append(cantidad_lineas[funciones_que_llaman])
        funciones_no_llamadas.remove(funciones_que_llaman)
    
    for funciones_llamadas in funciones_no_llamadas:
        lista_final[funciones_llamadas] = ("", cantidad_lineas[funciones_llamadas])
    
    return lista_final

#--------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------#
def imprimir(diccionario):
    """ [Autor: Augusto Carmona, Jose Piñeiro]
        [Ayuda: imprime un diagrama de arbol indicando que funcion llama a que funcion y entre parentesis 
        la cantidad de lineas de codigo de cada una]
    """
    print()
    print("=====ARBOL DE INVOCACIONES=====================================================")
    generar_diagrama(diccionario)
    print("===============================================================================")
    print()

#---------------------------------#
def generar_diagrama(diccionario):
    """ [Autor: Augusto Carmona, Jose Piñeiro]
        [Ayuda: busca en el diccionario la informacion de invocaciones y cantidad de lineas sobre cada funcion
        y la estructura en modo de diagrama de arbol]
    """
    llamados_secundarios= identificar_funcion_principal(diccionario)
    for clave in diccionario: 
        if (diccionario[clave][0] != "") and (not clave in llamados_secundarios):
            print("{}({})".format(clave, diccionario[clave][-1][0]))
            
            for funcion in diccionario[clave][0]:
                print()
                print("\t--> {}({})".format(funcion, diccionario[funcion][-1][0]))
            
                if (diccionario[funcion][0] != ""):
                        for elemento in diccionario[funcion][0]:
                            espacio = "\t\t"
                            ajuste= espacio + "--> {}({})"
                            print(ajuste.format(elemento, diccionario[elemento][-1][0]))
                            print()
                            imprimir_exponencial(diccionario,elemento,espacio)
#------------------------------------------------------------

def imprimir_exponencial(diccionario,elemento,espacio):
    if not diccionario[elemento][0] == "":
        espacio += "\t"
        ajuste= espacio + "--> {}({})"
        for seudo_elemento in diccionario[elemento][0]:
            print(ajuste.format(seudo_elemento, diccionario[seudo_elemento][-1][0]))
            print()
            if diccionario[seudo_elemento][0] != "":
                imprimir_exponencial(diccionario,seudo_elemento,espacio)
#------------------------------------------------------------

def identificar_funcion_principal(diccionario): #llamada desde generar_diagrama()
    """ [Autor: Augusto Carmona, Jose Piñeiro]
        [Ayuda: identifica a la funcion que llama a más funciones del programa]
    """
    llamados_principal = []

    for clave in diccionario:
        if len(diccionario[clave][0]) > len(llamados_principal):
            llamados_principal = diccionario[clave][0]
    
    fue_llamada_luego = llamados_principal.copy()
    
    for clave in diccionario:
        if len(diccionario[clave][0]) >= 1:
            for funcion in diccionario[clave][0]:
                if not funcion in fue_llamada_luego:
                    fue_llamada_luego.append(funcion)
    
    return fue_llamada_luego
                        
#------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------- bloque principal ---------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------#
def main_diagrama_arbol():
    """ [Autor: Augusto Carmona, Jose Piñeiro]
        [Ayuda: divide el programa en dos bloques principales, uno que extrae la
        informacion del archivo fuente_unico.csv y otro que la imprime como un diagrama de arbol]
    """
    diccionario_funciones = obtener_informacion()
    imprimir(diccionario_funciones)

main_diagrama_arbol()