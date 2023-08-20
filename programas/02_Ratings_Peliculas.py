"""
    Obtener el conteo de ratings de los usuarios
    del dataset u.data bajado de grouplens.org
    
    Recordar que las columnas del archivo son
    userID Pelicula Rating	Usuario
    196 242 3 81250949
    186 302 3 891717742
"""

# Importamos las librerias de Spark y collection
from pyspark import SparkConf, SparkContext
import collections

"""
    Se realiza la configuracion de Spark, de manera local
    se configura para que sea de manera local y se le asigna un nombre
    se la pasa la configuracion realizada al contexto de Spark
    en setMaster se le pueden pasar los nucleos a ejecutar
    esto depende de los nucleos de la maquina local 
    con local[n] siendo n el numero de nucleos a usar
"""
conf = SparkConf().setMaster("local").setAppName("ContadorRatings")
sc = SparkContext(conf=conf)

"""
    Se crea el RDD con los datos procesados a partir del archivo original
    separamos los campos del archivo en listas tomando el tabulador '\t' como separador
    y extrayendo la columna de Rating

    La ruta en textFile puede ser de dos maneras
    Con la ruta absoluta "file:///Users/...../bigdata_python_spark/datos/ml-100k/u.data"
    Con la ruta relativa "../datos/ml-100k/u.data"
"""
lineas = sc.textFile("../datos/ml-100k/u.data")
rating = lineas.map(lambda x: x.split()[2])

"""
    Se hace un conteo por rating con countByValue
    se crea el par (clave, valor)
    donde clave/Valor son ratings/conteo_por_rating
"""
resultado = rating.countByValue()

# Se hace un ordenamiento al resultado obtenido y se presentan los datos
result_orden = collections.OrderedDict(sorted(resultado.items()))
print("Los ratings de las peliculas son los siguientes: \n")
print("Ratings\tNum_Usuarios")

for key, value in result_orden.items():
    print("{}\t{}".format(key,value))
