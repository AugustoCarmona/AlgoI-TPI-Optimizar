#Tabla con numeros del 1 al 10 mostrando el resultado de la elevacion al cuadrado y al cubo
for i in range(1,11):
    print('{3}{0:2d}{3} {3}{1:3d}{3} {3}{2:4d}{3}'.format(i, i*i, i*i*i, '|'))
    #el bucle for crea un rango del uno al 10 para i
    #dentro del format se hace el calculo
    #i es el numero que estamos calculando
    #i*i es el numero al cuadrado
    #i*i*i es el numero al cubo
    #entre las barras imprimimos el cero el uno y el dos 3 corresponde a '|'
    #0 1 y 2 corresponden a i , i*i , i*i*i
    
    #2d 3d y 4d corresponden a la cantidad de caracteres para indicar la alineacion de los eleentos segun la cantidad de cifras de estos
    #la letra d indica que son numeros enteros (en caso de datos de texto se utiliza s 'string')