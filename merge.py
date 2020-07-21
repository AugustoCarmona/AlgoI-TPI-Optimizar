def leer_archivo(archivo):
    """
    [Autor:Gaston Mondin]
    [Ayuda: Lee cada archivo si hay linea]
    """
    linea=archivo.readline().strip("\n")
    return linea if linea else ""

def unir_archivos(archivos, archivofinal):
    """
    [Autor:Gaston Mondin]
    [Ayuda:]
    """
    funciones=[]
    for archivo in archivos:
        funciones.append(leer_archivo(archivo))
    while funciones!=[]:
        menor=""
        for i in range(len(funciones)):
            if menor=="":
                menor=funciones[i]
                j=i
            elif funciones[i]<menor:
                menor=funciones[i]
                j=i
        grabar_archivo(archivofinal, menor)
        funciones[j]=leer_archivo(archivos[j])
        if funciones[j]=="":
            del(funciones[j])
            del(archivos[j])

def realizar_merge(programas):
    """
    [Autor:Gaston Mondin]
    [Ayuda: Esta funcion realiza el llamado a la funcion que une]
    """
    opciones={"Código":["codigo","fuente_unico"],"Comentarios":["comentarios","comentarios"]}
    for opcion in opciones:
        archivos=[]
        for programa in programas:
            archivos.append(open("./data/"+programa[programa.rindex("\\"):programa.index(".")]+"_"+opciones[opcion][0]+".csv","r"))
        codigo=open("./data/"+opciones[opcion][1]+".csv","w")
        unir_archivos(archivos, codigo)
        for archivo in archivos:
            archivo.close()
        codigo.close()