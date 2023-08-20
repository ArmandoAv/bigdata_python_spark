"""
    Obtener las ocurrencias de cada palabras
    del dataset Book.txt

    El archivo es un documento de texto comun
    Este programa es una mejora del programa 
    07_Conteo_Palabras_Regex.py
    mostraremos las palabras que mas ocurrencia tienen
"""

# Importamos las librerias de Spark y de expresiones regulares
import re
from pyspark import SparkConf, SparkContext

"""
    Se define una funcion con expresiones regulares para
    manejar los signos de puntuacion con la opcion r'\W+'
    indica que queremos cortar las lineas en palabras luego
    hacemos el split de las palabras convirtiendolas en minusculas
"""
def normalizaPalabra(text):
    return re.compile(r'\W+', re.UNICODE).split(text.lower())

"""
    Se realiza la configuracion de Spark, de manera local
    se configura para que sea de manera local y se le asigna un nombre
    se la pasa la configuracion realizada al contexto de Spark
    en setMaster se le pueden pasar los nucleos a ejecutar
    esto depende de los nucleos de la maquina local 
    con local[n] siendo n el numero de nucleos a usar
"""
conf = SparkConf().setMaster("local").setAppName("ContadorPalabrasClasificado")
sc = SparkContext(conf = conf)

"""
    Se aplica flatMap a la funcion creada
    para que corte las palabras en su propia linea
    esa informacion es el RDD de entrada
    contamos cuantas veces ocurre cada palabra

    La ruta en textFile puede ser de dos maneras
    Con la ruta absoluta "file:///Users/...../bigdata_python_spark/datos/Book.txt"
    Con la ruta relativa "../datos/Book.txt"
"""
input = sc.textFile("../datos/Book.txt")
words = input.flatMap(normalizaPalabra)

"""
    Se modifica las palabras para que aparezcan como palabras + 1
    con el 1 se contara el numero de ocurrencias
    con la primera y segunda funcion lambda respectivamente
    se invertira el par resultante clave/valor a valor/clave
    de conteo/palabra se modifca como palabra/conteo
    con la tercera funcion lambda
    esto para ordenar las ocurrencias de las palabras
    con la funcion sortByKey
"""
wordCounts = words.map(lambda x: (x,1)).reduceByKey(lambda x, y: x + y)
wordCountSorted = wordCounts.map(lambda x: (x[1], x[0])).sortByKey()
# Si se dea ordenar en orden descendente se incluye el valor False en sortByKey
# wordCountSorted = wordCounts.map(lambda x: (x[1], x[0])).sortByKey(False)
results = wordCountSorted.collect()

"""
    Se imprime la lista de palabras y su ocurrencia
    el ascii se encarga de errores de codificacion
    se vuelve a cambiar el par clave/valor por valor/clave
    en el print del if
"""
print("La ocurrencia de las palabras es la siguiente: ")
for result in results:
    count = str(result[0])
    word = result[1].encode('ascii','ignore')
    if (word):
        print(word.decode() + ":\t\t" + count)

