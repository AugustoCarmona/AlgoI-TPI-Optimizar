"""Falta hacer algunas condiciones y verificar las que estan hechas y despues adaptarlo al verdadero inicio"""



def contador(archivo,lista_final):
          
          for posicion in range(len(lista_final)):
              diccionario={}
              nombre_funcion=""
              nombre_modulo=""
              cont_parametr=0
              cont_return=0
              cont_if=0
              cont_for=0
              cont_while=0
              cont_break=0
              cont_exit=0
              cont_coment=0
              for caracter in range(len(lista_final[posicion])):
                 if caracter==0:
                     nombre_funcion=lista_final[posicion][caracter]
                 elif caracter==2:
                     nombre_modulo=lista_final[posicion][caracter]
                 
                 if "(" in lista_final[posicion][caracter] and ")" in lista_final[posicion][caracter]:
                     cont_parametr+=1
                 if "return" in lista_final[posicion][caracter]:
                    cont_return+=1
                 if "if" in lista_final[posicion][caracter] or "elif" in lista_final[posicion][caracter]:
                     cont_if+=1
                 if "for" in lista_final[posicion][caracter]:
                     cont_for+=1
                 if "while" in lista_final[posicion][caracter]:
                     cont_while+=1
                 if "break" in lista_final[posicion][caracter]:
                     cont_break+=1
                 if "exit" in lista_final[posicion][caracter]:
                     cont_exit+=1
                 if "#" in lista_final[posicion][caracter]:
                     cont_coment+=1
              diccionario={"nombre funcion":nombre_funcion,"nombre_modulo":nombre_modulo,"parametros":cont_parametr,"returns":cont_return,"elif/if":cont_if,"for":cont_for,"while":cont_while,"break":cont_break,"exit":cont_exit,"comentarios":cont_coment}
              print(diccionario)
              archivo.write(str(nombre_funcion) +";" + str(nombre_modulo) + ";" + str(cont_parametr) +";"+ str(cont_return)+";"+str(cont_if)+";"+str(cont_for)+";"+str(cont_while)+";"+str(cont_break) +";"+str(cont_exit)+";"+str(cont_coment)+"\n")
            

def armado_listas(merge):
    lista_total=merge.readlines()
    merge.seek(0)
    lista_parcial=merge.readline().split(";")
    lista_final=[]
    for i in range(len(lista_total)):
        lista_final.append(lista_parcial)
        lista_parcial=merge.readline().split(";")
    
    return lista_final
    
  







#---------------------------bloque principal -----------------------------------------
archivo=open("panel_general.csv","w")
elegir=input("elija merge_codigo o merge_comentario: ")
if elegir=="merge_codigo":
     merge=open("app_matematica_codigo.csv","r")
     
else:
    merge=open("lib_matematica_codigo.csv","r")

lista_final=armado_listas(merge)
contador(archivo,lista_final)
archivo.close()