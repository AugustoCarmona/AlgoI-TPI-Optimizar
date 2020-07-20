def crear_lista():
    with open("programas.txt","r") as archivo_programas:
        programas=[]
        linea=archivo_programas.readline().rstrip("\n")
        while linea!="":
            programas.append(linea)
            linea=archivo_programas.readline().rstrip("\n")
    return programas

def generar_archivos_csv(programa, codigo, comentarios):
    with open("./data/"+programa[programa.rindex("\\")+1:programa.index(".")]+"_codigo.csv","w") as archivo_codigo:
        for items in sorted(codigo):
            archivo_codigo.writelines(items)
            for item in codigo[items]:
                archivo_codigo.writelines(";"+item)
            archivo_codigo.writelines("\n")
    with open("./data/"+programa[programa.rindex("\\")+1:programa.index(".")]+"_comentarios.csv","w") as archivo_comentarios:
        for items in sorted(comentarios):
            archivo_comentarios.writelines(items)
            for item in comentarios[items]:
                archivo_comentarios.writelines(";"+item)
            archivo_comentarios.writelines("\n")

def analizar_lineas(archivo, programa, codigo, comentarios):
    funcion_actual=""
    string=""
    comentado=False
    for linea in archivo:
        if linea.count("    ")==0 and linea!="\n":
            funcion_actual=""
        linea=linea.strip("    ").strip("\n")
        if "#" in linea and funcion_actual=="":
                linea=linea[:linea.index("#")]
        elif "#" in linea:
            comentarios[funcion_actual].append(linea[linea.index("#")+1:])
            linea=linea[:linea.index("#")]
        if "def " in linea:
            funcion_actual=linea[linea.index("def ")+4:linea.index("(")]
            codigo[funcion_actual]=[]
            comentarios[funcion_actual]=[]
            codigo[funcion_actual].append(linea[linea.index("("):linea.index(":")])
            codigo[funcion_actual].append(programa[programa.rindex("\\")+1:])
        elif funcion_actual!="" and linea!="":
            if '"""' in linea and comentado:
                comentado=False
            elif '"""' in linea and not comentado:
                comentado=True
                if "[Autor:" in linea:
                    comentarios[funcion_actual].append(linea[linea.index("["):])
            elif not comentado:
                codigo[funcion_actual].append(linea)
            elif comentado:
                if "[Ayuda: " in linea and "]" in linea:
                    comentarios[funcion_actual].append(linea)
                elif "[Ayuda: " in linea:
                    string=""
                    string+=linea+" "
                elif "]" in linea:
                    string+=linea
                    comentarios[funcion_actual].append(string)
                else:
                    string+=linea+" "
    generar_archivos_csv(programa, codigo, comentarios)

def recorrer_programas(programas):
    for programa in programas:
        codigo={}
        comentarios={}
        with open(programa,"r") as archivo:
            analizar_lineas(archivo, programa, codigo, comentarios)

def menu_de_opciones():
    print("-----MENÚ DE OPCIONES-----\n")
    print("1. Panel General de Funciones")
    print("2. Consulta de Funciones")
    print("3. Analizador de Reutilización de Código")
    print("4. Árbol de Invocación")
    print("5. Información por Desarrollador")
    print("6. Salir")
    opcion=input("Ingrese una opción: ")
    import panel
    while not opcion.isdigit() or int(opcion)<1 or int(opcion)>6:
        print("Valor ingresado incorrecto, intente de nuevo.")
        opcion=input("Ingrese una opción: ")

def main():
    import merge
    programas=crear_lista()
    recorrer_programas(programas)
    merge.realizar_merge(programas)
    menu_de_opciones()

main()