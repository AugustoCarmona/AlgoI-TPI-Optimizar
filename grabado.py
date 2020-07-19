def grabar (texto,archivo):
    donde_Grabo = open(archivo,"a")
    donde_Grabo.writelines(texto + '\n')
    donde_Grabo.close()