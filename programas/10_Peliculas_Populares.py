"""
    Obtener la popularidad de las peliculas
    del dataset u.data bajado de grouplens.org
    
    Recordar que las columnas del archivo son
    userID movieID Rating	Usuario
    196 242 3 81250949
    186 302 3 891717742
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
conf = SparkConf().setMaster("local").setAppName("PeliculaPopular")
sc = SparkContext(conf = conf)

"""
    Se crea el RDD con los datos procesados a partir del archivo original
    separamos los campos del archivo en listas tomando el tabulador '\t' como separador
    y extrayendo la columna de pelicula
    se modifica el valor de pelicula para que aparezcan como un par peliculas + 1
    con el 1 se contara el numero de ocurrencias
    con la primera y segunda funcion lambda respectivamente

    La ruta en textFile puede ser de dos maneras
    Con la ruta absoluta "file:///Users/...../bigdata_python_spark/datos/ml-100k/u.data"
    Con la ruta relativa "../datos/ml-100k/u.data"
"""
lineas = sc.textFile("../datos/ml-100k/u.data")
peliculas = lineas.map(lambda x: (int(x.split()[1]), 1))
conteo_peliculas = peliculas.reduceByKey(lambda x, y: x + y)

"""
    Se invertira el par resultante clave/valor a valor/clave
    de conteo/movieID se modifica como movieID/conteo
    con la funcion lambda, ademas se ordenan las 
    ocurrencias de las peliculas con la funcion
    sortByKey() por la nueva clave movieID
"""
invierte_par = conteo_peliculas.map(lambda xy: (xy[1], xy[0]))
# Por default sortByKey orden en orden ascendente
ordena_peli = invierte_par.sortByKey()
# Si se quiere ordenar en orden descendente se agrega False a sortByKey
#ordena_peli = invierte_par.sortByKey(False)
results = ordena_peli.collect()

# Se imprime la lista de las claves de las peliculas y su popularidad
print("La ocurrencia de las peliculas es la siguiente: ")
print("Conteo\tID de Pelicula")
for result in results:
    print(result)

