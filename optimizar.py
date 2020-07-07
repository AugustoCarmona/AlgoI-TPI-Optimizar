def leer (programa):
    lista = open(programas.txt,"r")
    lineaP = lista.readline()
   
    return linea.rstrip("\n").split(",")
    
def separacion (archivo):
    lineaA= archivo.readline()
    while lineaA:
        if "#" in lineaA:
            grabado(comentarios.cvs,linea)
        elif linea != "":
            #me fijo si no es vacio
            grabado(fuente_unico.csv,linea)
        
        linea= archivo.readline()


def grabar (archivo,Funcion,Parametros,Lineas,Invocaciones,Returns,If/Elif,For,While,Break,Exit,coment,Ayuda,Autor):
    archivo.write(Funcion + "," + Parametros + "," + Lineas "," + Invocaciones+ "," + Returns + "," + If/Elif "," + For + "," + While + "," + Break + "," + Exit + "," + coment +"," + Ayuda +"," + Autor +"\n",sep ="\t")
    
    
    


def nombre_funciones(archivo):
    
   
    
    lineaF = linea.readline()
    
    
    if "def" in lineaF :
        
        funciones ={}
        nombre =lineaF.(lineaF.index("def ") :lineaF.index(" ("))
        
        while condicion_1 : # aun no se cual podria ser la condicion
            
            if  not (nombre in funciones) :
                # si la funcion no esta se agrega al diccionario
                funciones["modulo"] = "nombre":nombre 
                
                
                
                
            
        
        
            
            