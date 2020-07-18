def contar (archivo,loContado):
    contador=0
    with open ("archivo.txt","r"):
        linea = archivo.readline()
        if linea != "" and loContado in linea :
            contador +=1
        linea = archivo.readline()
    print (contador)
contar (tony,"en")