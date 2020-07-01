#falta forma de definir cuando es un nuevo autor y depende mucho del archivo en y el orden pero
#imagine que el archivo lo haciamos nosotros asi que no habria drama
tony=open("ejemplo.txt","r")
numeros="12345678990"
funciones=0
lineas=0
cantidad_de_lineas=43
autor=tony.readline()
funcion = tony.readline().split(',')
linea = tony.readline().split()
total_f=0
total_l=0
line="0"
porcentaje=(lineas//cantidad_de_lineas)*100
funcion_nombres=[]
print ("%-1s %s" %("Autor:", autor))
print("%-6s %-20s %s" %("","funcion", "lineas"))
print(("----------------------------------"))
while linea!=[''] and autor!=[]:
    if line in numeros:
        print("%-6s %-20s %s" %("",funcion,linea))
        line=linea[0]
        funciones+=1
        if funcion not in funcion_nombres:
            total_f+=1
            funcion_nombres+=funcion
        lineas+=int(line)
        funcion = tony.readline().split()
        linea = tony.readline().split()
        porcentaje=((lineas/cantidad_de_lineas))*100
        total_l+=1
    else:
        print("%-6s %s %-19s %s %s %s" %("",funciones,"funciones - lineas",lineas,porcentaje,"%"))
        autor=funcion
        funciones=0
        lineas=0
        print ("%-1s %s" %("Autor:", autor))
        funcion = tony.readline().split()
        linea = tony.readline().split()
print("%s %-6s %-20s %s"%("total:", total_f, "funciones - lineas",total_l))
ejemplo.close()