def abro (programa):
    listaP= programa.readline()
    lineaP= open(listaP,"r")
    return (listaP)

def grabado(archivo,linea):
    archivo.write(linea + "/n")
    
def separacion (archivo):
    linea= archivo.readline()
    while linea:
        if "#" in linea:
            grabado(comentarios.cvs,linea)
        elif linea != "":
            #me fijo si no es vacio
            grabado(fuente_unico.csv,linea)
        
        linea= archivo.readline()
