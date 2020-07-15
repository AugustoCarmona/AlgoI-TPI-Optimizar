Falta hacer algunas condiciones y verificar las que están hechas y despues adaptarlo al verdadero inicio" "
def  contador ( archivo , lista_codigo ):
    
    for posicion  in  rango ( len ( lista_codigo )):
        diccionario = {}
        nombre_funcion = ""
        nombre_modulo = ""
        autor = ""
        ayuda = "NO"
        cont_parametr = 0
        cont_return = 0
        cont_if = 0
        cont_for = 0
        cont_while = 0
        cont_break = 0
        cont_exit = 0
        cont_coment = 0
        for  caracter  in   gama ( len ( lista_codigo [ posicion ])):
            if caracter == 0 :
                     nombre_funcion = lista_codigo [ posicion ] [ caracter ]

                 elif  caracter == 1 : # revisar parámetros
                     cont_comas = lista_codigo [ posicion ] [ caracter ].count( "," )
                     if  cont_comas ! = 0 :
                         cont_parametr = 1 + cont_comas
                elif  caracter == 2 :
                     nombre_modulo = lista_codigo [ posicion ] [ caracter ]
                
                if  "return"  en  lista_codigo [ posicion ] [ caracter ]:
                    cont_return + = 1
                 
                 if  "if"  in   lista_codigo [ posicion ] [ caracter ] or   "elif"  in  lista_codigo [ posicion ] [ caracter ]:
                     
                     
def contador (archivo, lista_codigo):
    
    for posicion_c in rango ( len ( lista_codigo ) ) :
        autor = ""
        ayuda = "NO"
        cont_coment = 0
        for linea in gama ( len ( lista_codigo [ posicion_c ])):
            if "autor" in linea:
                autor= linea[linea.index(":"):]
                
            elif "ayuda" in linea:
                ayuda ="si"
            
            elif linea > 1 :
                if linea.isupper() and  not "ayuda" in linea:
                    cont_coment +=1
                             
              invocaciones = cantidad_de_invocaciones ( lista_merge_fuente_unico , nombre_funcion , posicion ) # revisión invocaciones   
              merge_comentarios.seek( 0 )
              diccionario = { "nombre funcion" : nombre_funcion , "nombre_modulo" : nombre_modulo , "parametros" : cont_parametr , "devuelve" : cont_return , "elif / if" : cont_if , "for" : cont_for , "while" : cont_while , "break " : cont_break , " exit " : cont_exit , " comentarios " : cont_coment , "autor " : autor, "ayuda" : ayuda }
              diccionario = { "nombre funcion" : nombre_funcion , "nombre_modulo" : nombre_modulo , "parametros" : cont_parametr , "devuelve" : cont_return , "elif / if" : cont_if , "for" : cont_for , "while" : cont_while , "break " : cont_break , " exit " : cont_exit , " comentarios " : cont_coment , "autor " : autor, "ayuda" : ayuda , "invocaciones" : invocaciones }
              print ( diccionario )
              archivo.write ( str ( nombre_funcion ) + ";"  +  str ( nombre_modulo ) +  ";"  +  str ( cont_parametr ) + ";" +  str ( cont_return ) + ";" + str ( cont_if ) + ";" + str ( cont_for ) + ";" + str ( cont_while ) + ";" +str ( cont_break ) + ";" + str ( cont_exit ) + ";" + str ( cont_coment ) + " \ n " )

def armado_listas_comentarios (fusionar):
   volver  lista_final




def  cantidad_de_invocaciones ( lista_codigo , nombre_funcion , posicion ):
     cont_invocaciones = 0
     for posicion_2  in  range ( len ( lista_codigo )):
         for caracter_2 in range ( len ( lista_codigo [ posicion_2 ])):
             si  posicion ! = posicion_2 :
                 si  nombre_funcion  en  lista_codigo [ posicion_2 ] [ caracter_2 ]:
                     cont_invocaciones + = 1

     volver  cont_invocaciones



def armado_listas_comentarios (fusionar):
contador ( archivo , lista_merge_fuente_unico )
archivo.close()