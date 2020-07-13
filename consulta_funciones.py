#-----------------------------------
def extractor_informacion():
    """ [Autor: Augusto Carmona]
        [Ayuda: Lee cada linea del archivo .csv y extrae los datos de las funciones.
        Por ultimo genera una lista ordenada alfabeticamente con los nombres de las funciones
        en el archivo y la devuelve.]
    """
    with open("panel_general.csv", "r") as archivo:

        funciones = []
        linea = archivo.readline()
        for linea in archivo:
            nombre, parametros, lineas, invocaciones, retorno, si, para, mientras, quiebre, salida, comentarios, ayuda, autor, pregunta = linea.rstrip().split(",")
            funcion, modulo = nombre.split(".")
            funciones.append(funcion)

        return sorted(funciones)

#-----------------------------------
def ajustar_largo(texto, largo):
    """[Autor: Augussto Carmona]
    """
    if len(texto) > largo:
        texto = texto[:largo]
    elif len(texto) < largo:
        texto = (texto + " " * largo)[:largo]
    
    return texto
#-----------------------------------
def generador_tabla(lista_funciones):
    """ [Autor: Augusto Carmona]
        [Ayuda: Genera e imprime la tabla de funciones]
    """
    funciones_por_columna = round(len(lista_funciones) / 5)
        
    columna_1 = lista_funciones[:funciones_por_columna]
    columna_2 = lista_funciones[funciones_por_columna:funciones_por_columna*2]
    columna_3 = lista_funciones[funciones_por_columna*2:funciones_por_columna*3]
    columna_4 = lista_funciones[funciones_por_columna*3:funciones_por_columna*4]
    columna_5 = lista_funciones[funciones_por_columna*4:]
        
    data = [columna_1, columna_2, columna_3, columna_4, columna_5]
        
    print('FUNCIONES DEL MODULO {}:'.format('lib_matematica.py'), '-'*61)
    print()
    for i in data:
        print("| ", end = " ")
        for columna in i:
            print(ajustar_largo(columna + '()', 20), end = "  |  ")
        print()
    print('-'*101)
            
#-----------------------------------
def consulta_individual(lista_funciones):
    """[Autor: Augussto Carmona]
    """
    print()
    menu_ingreso(lista_funciones)

#-----------------------------------
def descripcion_individual(lista_funciones):
    """[Autor: Augussto Carmona]
    """
    print()
    menu_ingreso(lista_funciones)

#-----------------------------------
def consulta_general(lista_funciones):
    """[Autor: Augussto Carmona]
    """
    print()
    menu_ingreso(lista_funciones)

#-----------------------------------
def descripcion_general(lista_funciones):
    """[Autor: Augussto Carmona]
    """
    print()
    menu_ingreso(lista_funciones)

#-----------------------------------
def menu_ingreso(lista_funciones):
    """ [Autor: Augusto Carmona]
        [Ayuda: Solicita el ingreso de la funcion a analizar]
    """
    ing = input(" Funcion: ")
    
    while (ing != ""):
        if ing.strip('?').strip('#') in lista_funciones:
            if '?' in ing:
                consulta_individual(lista_funciones)
            if '#' in ing:
                descripcion_individual(lista_funciones)
            else:
                print()
                ing = input(" Usted ha ingresado una orden incorrecta, por favor reingrese: ")
        elif ing == '?todo':
            consulta_general(lista_funciones)
        elif ing == '#todo':
            consulta_general(lista_funciones)
        else:
            print()
            ing = input(" Usted ha ingresado una orden incorrecta, por favor reingrese: ")

#---------------------------------- bloque principal ----------------------------------#
def main():
    """[Autor: Augussto Carmona]
    """
    lista_funciones = extractor_informacion()
    generador_tabla(lista_funciones)
    print()
    menu_ingreso(lista_funciones)

main()