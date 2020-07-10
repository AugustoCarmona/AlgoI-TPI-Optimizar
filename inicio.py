def crear_lista():
    with open("programas.txt","r") as archivo_programas:
        programas=[]
        linea=archivo_programas.readline().rstrip("\n")
        while linea!="":
            programas.append(linea)
            linea=archivo_programas.readline().rstrip("\n")
    return programas

def crear_tabla(programas):
    tabla={}
    for programa in programas:
        with open(programa,"r") as archivo_programa:
            funcion_actual=""
            comentado=False
            for linea in archivo_programa:
                linea=linea.strip("    ").strip("\n")
                if "#" in linea:
                    linea=linea[:linea.index("#")]
                if "def " in linea:
                    funcion_actual=linea[linea.index(" ")+1:linea.index("(")]
                    tabla[funcion_actual]=[]
                    tabla[funcion_actual].append(linea[linea.index("("):linea.index(":")])
                    tabla[funcion_actual].append(programa)
                elif funcion_actual!="" and linea!="":
                    if '"""' in linea and comentado:
                        comentado=False
                    elif '"""' in linea and not comentado:
                        comentado=True
                    elif not comentado:
                        tabla[funcion_actual].append(linea)
    return tabla


programas=crear_lista()
tabla=crear_tabla(programas)
for funcion in sorted(tabla):
    print(funcion)