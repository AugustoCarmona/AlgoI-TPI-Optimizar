import merge, panel, consulta, analizador, arbol, informacion

def crear_lista():
    """[Autor: Gastón Mondín]
       [Ayuda: Crea una lista con las ubicaciones de cada uno de los programas que se encuentran en "programas.txt"]
    """
    with open("programas.txt","r") as archivo_programas:
        programas=[]
        linea=archivo_programas.readline().rstrip("\n")
        while linea!="":
            programas.append(linea)
            linea=archivo_programas.readline().rstrip("\n")
    return programas

def generar_archivos_csv(programa, codigo, comentarios):
    """[Autor: Gastón Mondín]
       [Ayuda: Crea los archivos csv en base a los diccionarios con código y comentarios que se generaron.]
    """
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

def analizar_linea(linea, programa, codigo, comentarios, funcion_actual, string, comentado):
    """[Autor: Gastón Mondín]
       [Ayuda: Analiza una línea del programa que se está recorriendo, haciendo los cambios de línea necesarios
        y guardando todos los datos en diccionarios.]
    """
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
        if ('"""' in linea or "'''" in linea) and comentado:
            comentado=False
        elif ('"""' in linea or "'''" in linea) and not comentado:
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
    return funcion_actual, string, comentado   

def recorrer_programas(programas):
    """[Autor: Gastón Mondín]
       [Ayuda: Recorre cada uno de los programas de la lista creada.]
    """
    for programa in programas:
        codigo={}
        comentarios={}
        with open(programa,"r") as archivo:
            funcion_actual=""
            string=""
            comentado=False
            for linea in archivo:
                funcion_actual, string, comentado = analizar_linea(linea, programa, codigo, comentarios, funcion_actual, string, comentado)
            generar_archivos_csv(programa, codigo, comentarios)

def menu_de_opciones():
    """[Autor: Gastón Mondín]
       [Ayuda: Menú de opciones encargado de llamar a cada uno de los puntos.]
    """
    print("\n-----MENÚ DE OPCIONES-----\n")
    print("1. Panel General de Funciones\n2. Consulta de Funciones\n3. Analizador de Reutilización de Código")
    print("4. Árbol de Invocación\n5. Información por Desarrollador\n6. Salir")
    opcion=input("Ingrese una opción: ")
    while opcion!="6":
        if not opcion.isdigit() or int(opcion)<1 or int(opcion)>6:
            opcion=input("Valor ingresado incorrecto, intente de nuevo: ")
        else:
            if opcion=="1":
                panel.main()
            elif opcion=="2":
                consulta.main()
            elif opcion=="3":
                analizador.main()
            elif opcion=="4":
                arbol.main()
            elif opcion=="5":
                informacion.main()
            print("\n-----MENÚ DE OPCIONES-----\n")
            print("1. Panel General de Funciones\n2. Consulta de Funciones\n3. Analizador de Reutilización de Código")
            print("4. Árbol de Invocación\n5. Información por Desarrollador\n6. Salir")
            opcion=input("Ingrese una opción: ")

def main():
    programas=crear_lista()
    recorrer_programas(programas)
    merge.realizar_merge(programas)
    menu_de_opciones()

main()