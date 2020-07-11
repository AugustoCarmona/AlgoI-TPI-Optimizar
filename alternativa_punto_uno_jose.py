def imprimir (diccionarioCodigo,diccionarioComentarios):
    for funcion in diccionarioCodigo:
        parametros = diccionarioCodigo[funcion][0]
        
        print("Nombre de la Función.Módulo:",funcion) 
        print("Cantidad de Parámetros Formales",parametros.count(" ")+1)
        print("Cantidad de líneas de código",len(diccionarioCodigo[funcion])-1)
        print("Cantidad de invocaciones a la función",contartodo(funcion,diccionarioCodigo))
        print ("Cantidad de Puntos de Salida",contar("return",diccionarioCodigo))
        print ("Cantidad de If, contabilizar los anidamientos elif",contar("if",diccionarioCodigo)+contar("elif",diccionarioCodigo))
        print ("Cantidad de For",contar("for",diccionarioCodigo))
        print ("Cantidad de While",contar("while",diccionarioCodigo))
        print ("Cantidad de Break",contar("break",diccionarioCodigo))
        print ("Cantidad de Exit", contar ("exit",diccionarioCodigo))
        print ("Cantidad de lineas de comentarios",)
        print ("Ayudas:")
        print ("Autor")

#--------------------------------------------------------------------------------------------
def guardado (archivo, diccionarioCodigo):
    
    archivo.write("FUNCION,Parámetros,Líneas,Invocaciones,Returns,If/elif,for,while,Break,Exit,Coment,Ayuda,Autor"+ "\n")
    for funcion in diccionarioCodigo:
        
        parametros=diccionarioCodigo[funcion][0]
        
        guardar ("Nombre de la Función.Módulo:",funcion,archivo)
        guardar ("Cantidad de Parámetros Formales",parametros.count(" ")+1,archivo)
        guardar ("Cantidad de Parámetros Formales",parametros.count(" ")+1,archivo)
        guardar ("Cantidad de líneas de código",len(diccionarioCodigo[funcion])-1,archivo)
        guardar ("Cantidad de invocaciones a la función",contartodo(funcion,diccionarioCodigo),archivo)
        guardar ("cantidad de Puntos de Salida", contar("return",diccionarioCodigo),archivo)
        guardar ("Cantidad de If, contabilizar los anidamientos elif",contar("if",diccionarioCodigo) + contar("elif",diccionarioCodigo), archivo)
        guardar ("Cantidad de For",contar("for",diccionarioCodigo), archivo)
        guardar ("Cantidad de While", contar ("while",diccionarioCodigo), archivo)
        guardar ("Cantidad de Break",contar("break",diccionarioCodigo),archivo)
        guardar ("Cantidad de Exit", contar ("exit",diccionarioCodigo),archivo)
        guardar ("Cantidad de lineas de comentarios",,archivo)
        guardar ("Ayudas:",,archivo)
        guardar ("Autor",,archivo)

#--------------------------------------------------------------------------------------------
def guardar (texto,valor,archivo):
    archivo.write(texto + valor + "\n")

#--------------------------------------------------------------------------------------------
def contartodo(palabra,diccionario):
    contador=0
    for funcion in diccionario:
        x=1
        while x<len(diccionario[funcion]):
            linea= diccionario[funcion][x]
            if palabra in linea[0:(len(palabra)-1)]:
                contador+=1
            x+=1
    return contador

#--------------------------------------------------------------------------------------------
def contar(palabra,diccionario):
    contador=0
    x=1
    while x<len(diccionario[funcion]):
        linea= diccionario[funcion][x]
        if palabra in linea[0:(len(palabra)-1)]:
            contador+=1
        x+=1
    return contador

#--------------------------------------------------------------------------------------------    
archivo = open("panel_general.csv","w")
main():
    imprimir()
    guardado()
main()
archivo.close()