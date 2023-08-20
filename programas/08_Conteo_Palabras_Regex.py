"""
    Obtener las ocurrencias de cada palabras
    del dataset Book.txt

    El archivo es un documento de texto comun
    este programa es una mejora del programa 
    06_Conteo_Palabras.py
    con ayuda de expresiones regulares (REGEX)
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
conf = SparkConf().setMaster("local").setAppName("ContadorPalabrasRegex")
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
arch = sc.textFile("../datos/Book.txt")
palabras = arch.flatMap(normalizaPalabra)
cuenta_palabra = palabras.countByValue()

"""
    Se imprime la lista de palabras y su ocurrencia
    el ascii se encarga de errores de codificacion
"""
print("La ocurrencia de las palabras es la siguiente: ")
for palabra, cuenta in cuenta_palabra.items():
    limpia_palabra = palabra.encode('ascii','ignore')
    if (limpia_palabra):
        print(limpia_palabra.decode() + " " + str(cuenta))

