"""
    ** Consulta de Funciones **
    Muestra en pantalla los nombres de las funciones ordenados alfabeticamente
    uno al lado del otro y encolumnados
    Debajo de la tabla muestra un mensaje "Funcion: " a la espera del ingreso del
    nombre de una funcion y un caracter reservado ? o #
    El prgrama deja de solicitar ingresos cuando el usuario ingresa ENTER
    Si el usuario ingresa un dato incorrecto indica el error
    Si el usuario ingresa ?todo o #todo se debe listar la informacion descripta, pero para cada una
    de las funciones por pantalla
    Si el usuario ingresa imprimir?todo, se envia al archivo ayuda_funciones.txt, el contenido
    correspondiente formateado tal que no supere los 80 caracteres por linea
"""
def extractor_informacion():
    with open("panel_general.csv", "r") as archivo:

        funciones = []
        linea = archivo.readline()
        for linea in archivo:
            nombre, parametros, lineas, invocaciones, retorno, si, para, mientras, quiebre, salida, comentarios, ayuda, autor, pregunta = linea.rstrip().split(",")
            funcion, modulo = nombre.split(".")
            funciones.append(funcion)

        return sorted(funciones)

#--------------------------------------------------------------------
    
def menu_ingreso(lista_funciones):
    ing = input("Funcion: ")
    
    while (ing != ""):
        if (ing not in lista_funciones) and ("?"not in ing) or (ing not in lista_funciones) and ("#"not in ing):
            print("")
            ing = input("Usted ha ingresado una orden incorrecta. Por favor reingrese: ")
        else:
            print("")
            ing = input("Funcion: ")
    
#----main------------------------------------------------------------------
lista_funciones = extractor_informacion()
print(lista_funciones)
print("")
menu_ingreso(lista_funciones)