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
    for programa in lista_Completa_Y_Ordenada:
        lugar = 0
        while not programa in diccionario[lista_de_archivos[lugar]]:
            lugar+=1
        guardar(programa,archivo)
    
def guardar(nombre,archivo):
    
    archivo.write(nombre+"\n")


diccionario={"app_matematica_codigo":["menu_MCD","menu_MCM","menu_elegir","menu_factorial","menu_opciones","menu_potencia","menu_primo","solicitar_valor"],"lib_matematica_codigo":["es_primo","factorial","mcd","mcm","potencia"]}
union=open("union.csv","w")
merge(diccionario,union)
union.close()