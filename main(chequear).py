def crear_lista():
    with open("programas.txt","r") as archivo_programas:
        programas=[]
        linea=archivo_programas.readline().rstrip("\n")
        while linea!="":
            programas.append(linea)
            linea=archivo_programas.readline().rstrip("\n")
    return programas

#-----------------------------------------------------------------------------------------
#def crear_comentarios_archivos()

#-----------------------------------------------------------------------------------------
def crear_archivos(programas):
    for programa in programas:
        codigo={}
        comentarios={}
        with open(programa,"r") as archivo:
            funcion_actual=""
            comentado=False
            for linea in archivo:
                linea=linea.strip("    ").strip("\n")

                if "#" in linea:
                    linea=linea[:linea.index("#")]
                if "def " in linea:
                    funcion_actual=linea[linea.index(" ")+1:linea.index("(")]
                    codigo[funcion_actual]=[]
                    comentarios[funcion_actual]=[]
                    codigo[funcion_actual].append(linea[linea.index("("):linea.index(":")])
                    codigo[funcion_actual].append(programa)

                elif funcion_actual!="" and linea!="":
                    if '"""' in linea and comentado:
                        comentado=False
                    elif '"""' in linea and not comentado:
                        comentado=True
                    elif not comentado:
                        codigo[funcion_actual].append(linea)
            with open(programa.strip(".py")+"_codigo.csv","w+") as archivo_codigo:
                for items in codigo:
                    archivo_codigo.writelines(items)
                    for item in codigo[items]:
                        archivo_codigo.writelines(","+item)
                    archivo_codigo.writelines("\n")
    return codigo
#-----------------------------------------------------------------------------------------
programas=crear_lista()
#crear_tabla(programas)
codigo=crear_archivos(programas)