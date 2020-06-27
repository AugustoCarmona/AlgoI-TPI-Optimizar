def ingresoUsuario(lista):
    print (lista)
    igreso=str(imput("Funcion:"))
    while ingreso not "":
        if ingreso in lista:
            if "?" in ingreso:
                #podemos hacer un slice y
                #y abrimos el archivo que
                #sea en el cual esta la
                #descripcion y el parametro
            elif "#" in ingreso:
                #igual que arriba pero con
                #lo relativo
        elif ingreso =="?todo" or ingreso == "#todo":
            with open (descripciones.txt) as descripciones:
                descripciones.readline()
        elif ingreso == "inprimir?todo":
            with open(ayuda_funciones.txt,"r") as archivo:
                archivo.readline()
        else:
            print("ingreso invalido, porfavor ingrese un nombre de funcion valido o un comando valido")
        igreso=str(imput("Funcion:"))
    
