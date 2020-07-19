def solicitar_parametros (mensaje, minimo, maximo):
   
    valor = input(mensaje)
    while (not valor.isdigit()) or ((int(valor) < minimo) or (int(valor) > maximo)):
        print("Error: Valor debe estar entre", minimo, "y", maximo)
        valor = input(mensaje)
        
    return int(valor)

def menu_opciones():
    
    
    print("++++++++++++++++++++++++++++++++++++++++++")
    print("MENU DE OPCIONES")
    print()
    print("1. Panel General de Funciones ")
    print("2. Consulta Funciones")
    print("3. Analizador de reutilizacion del codigo")
    print("4. Arbol de Invocacion")
    print("5. Informacion por Desarrollador")
    print("6. Terminar")
    print("___________________________________________")
    print()



def menu_elegir():
    menu_opciones()
    opcion = solicitar_parametros("elija una opcion:",1,6)
    
    print('+----------------------------------+')
    while opcion != 6:
        if opcion == 1:
            panel_general()
        elif opcion == 2:
            tabla()
        elif opcion == 3:
            punto3()
        elif opcion == 4:
            arbol()
        else:
            informacion()
        menu_opciones()
        opcion = solicitar_parametros("Elija una opcion:",1,6)
        print("+-----------------------------------+")
       
          

   
menu_elegir()















