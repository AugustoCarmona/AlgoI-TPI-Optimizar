def leer_archivo(archivo):
    linea=archivo.readline().strip("\n")
    return linea if linea else ""

def grabar_archivo(archivo, linea):
    archivo.write(linea+"\n")

def unir_archivos(archivos, archivofinal):
    """[Autor: Gastón Mondín]
    [Ayuda: Une todos los archivos en uno solo mediante un merge.]
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
            archivos[j].close()
            del(archivos[j])

def realizar_merge(programas):
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