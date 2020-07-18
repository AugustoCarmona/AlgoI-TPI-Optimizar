def merge(diccionario,archivo):
    lista_Completa_Pero_No_Ordenada=[]
    lista_de_archivos=[]
    for clave in diccionario:
        item=0
        lista_de_archivos.append(clave)
        while item < len(diccionario[clave]):
            lista_Completa_Pero_No_Ordenada.append(diccionario[clave][item])
            item+=1
    lista_Completa_Y_Ordenada=sorted(lista_Completa_Pero_No_Ordenada)
    abrir(lista_Completa_Y_Ordenada,diccionario,lista_de_archivos)
    
def abrir(lista_Completa_Y_Ordenada,diccionario,lista_de_archivos):
    lista_de_programas={}
    for archivo in lista_de_archivos:
        index=0
        valor=open(archivo,"r")
        while index < len(diccionario[archivo]):
            linea=valor.readline().rstrip('\n')
            lista_de_programas[diccionario[archivo][index]]=linea
            index+=1
        valor.close()
    for funcion in lista_Completa_Y_Ordenada:
        linea_a_guardar=lista_de_programas[funcion]
        print(linea_a_guardar)
        guardar(linea_a_guardar,union)
def guardar(nombre,archivo):
    
    archivo.write(nombre+"\n")

diccionario={"app_matematica_codigo.csv":["menu_MCD","menu_MCM","menu_elegir","menu_factorial","menu_opciones","menu_potencia","menu_primo","solicitar_valor"],"lib_matematica_codigo.csv":["es_primo","factorial","mcd","mcm","potencia"]}
union=open("union.csv","w")
merge(diccionario,union)
union.close()