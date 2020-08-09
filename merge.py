def leer_archivo(archivo):
    """[Autor: Gastón Mondín]
       [Ayuda: Lee una línea del archivo.]
    """
    linea=archivo.readline().strip("\n")
    return linea if linea else ""

def grabar_archivo(archivo, linea):
    """[Autor: Gastón Mondín]
       [Ayuda: Graba una línea del archivo.]
    """
    archivo.write(linea+"\n")

def unir_archivos(archivos, archivofinal):
    """[Autor: Gastón Mondín]
       [Ayuda: Une todos los archivos en uno solo.]
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
    """[Autor: Gastón Mondín]
       [Ayuda: Función principal del programa encargado de realizar el merge.]
    """
    opciones={"Código":["codigo","fuente_unico"],"Comentarios":["comentarios","comentarios"]}
    for opcion in opciones:
        archivos=[]
        for programa in programas:
            if programa.count("\\")>0:
                nombre_programa=programa[programa.rindex("\\")+1:]
            elif programa.count("/")>0:
                nombre_programa=programa[programa.rindex("/")+1:]
            else:
                nombre_programa=programa
            archivos.append(open("./data/"+nombre_programa[:nombre_programa.index(".")]+"_"+opciones[opcion][0]+".csv","r"))
        codigo=open(opciones[opcion][1]+".csv","w")
        unir_archivos(archivos, codigo)
        for archivo in archivos:
            archivo.close()
        codigo.close()