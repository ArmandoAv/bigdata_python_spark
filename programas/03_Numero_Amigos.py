"""
    Obtener el numero de amigos por edad de una red social
    del dataset amigos.csv creado
    
    Recordar que las columnas por archivo son
    user_id Nombre Edad	Num_Amigos
    0	Will	33	385
    1	Jean	33	2
"""

# Importamos las librerias de Spark
from pyspark import SparkConf, SparkContext

"""
    Se realiza la configuracion de Spark, de manera local
    se configura para que sea de manera local y se le asigna un nombre
    se la pasa la configuracion realizada al contexto de Spark
    en setMaster se le pueden pasar los nucleos a ejecutar
    esto depende de los nucleos de la maquina local 
    con local[n] siendo n el numero de nucleos a usar
"""
conf = SparkConf().setMaster("local").setAppName("AmigosPorEdad")
sc = SparkContext(conf=conf)

"""
    Separamos los campos del archivo en listas tomando el caracter ',' como separador
    obtenemos de la lista los campos de la edad y el numero de amigos
    creamos el par (clave, valor)
    donde clave/Valor son edad/num_amigos

    La ruta en textFile puede ser de dos maneras
    Con la ruta absoluta "file:///Users/...../bigdata_python_spark/datos/amigos.csv"
    Con la ruta relativa "../datos/amigos.csv"
""" 
def parseoLinea(line):
    campos = line.split(',')
    edad = int(campos[2])
    num_amigos = int(campos[3])
    return (edad, num_amigos)

# Se crea el RDD con los datos procesados a partir del archivo original
lineas = sc.textFile("../datos/amigos.csv")
rdd = lineas.map(parseoLinea)

"""
    Transformamos los valores en el par (clave, valor)
    calculamos los promedios
    transformamos los valores obtenidos sumados a un promedio
    para los valores de Edad y Num_Amigos
    33  385
    33  2
    55  221
    Como necesitamos saber el promedio de amigos por edad se hace lo siguiente
    Primero se anidad los pares
    (33,385) -> (33,(385,1)) Se agrega un 1 al par anidado
    (33,2)   -> (33,(2,1))   Se agrega un 1 al par anidado
    (55,221) -> (55,(221,1)) Se agrega un 1 al par anidado
    Por eso se usa reduceByKey para combinar cosas juntas por la misma clave (pares anidados)
    Se suman los valores del par anidado y se agrupan en el valor del primer valor de la clave
    (33,(387,2))
    (55,(221,1))
    Se obtiene el promedio de con los valores del par anidado
    (33,(387/2)) -> (33,193.5)
    (55,(221/1)) -> (55,221)
"""
total_por_edad = rdd.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
promedio_edad = total_por_edad.mapValues(lambda x: x[0] / x[1])

"""
    Esta funcion regresa todos los elementos de los nodos al nodo controlador
    es decir que recolecta los resultados de la operacion que se acaba de realizar
"""
resultados = promedio_edad.collect()

# Imprime los resultados obtenidos con ayuda del ciclo for
print("Los resultados del numero de amigos por edad para los usuarios son: ")
print("Edad\tNumero_Amigos")
for resultado in resultados:
    print(resultado)
