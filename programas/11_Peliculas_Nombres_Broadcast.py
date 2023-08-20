"""
    Obtener la popularidad de las peliculas
    con ayuda de una funcion broadcast

    Del dataset u.data bajado de grouplens.org
    recordar que las columnas del archivo son
    userID Pelicula Rating	Usuario
    196 242 3 81250949
    186 302 3 891717742
    Ademas del dataset u.item
    se obtendra el nombre de la pelicula
"""

# Importamos las librerias de Spark
from pyspark import SparkConf, SparkContext

"""
    Se crea una funcion para el nombre de la pelicula
    se crea un diccionario vacio llamado nombre_peliculas
    se abre el archivo con el nombre de las peliculas u.item
    separamos el archivo por pipe '|'
    extraemos el movieID que esta como entero (int)
    asignamos el movieID con su respectivo movieName
    para crear el par de clave/valor necesario para un diccionario
    que se encuentra en el segundo campo del archivo

    La ruta del archivo en open() puede ser de dos maneras
    Con la ruta absoluta "C:/Users/...../bigdata_python_spark/datos/ml-100k/u.item"
    Con la ruta relativa "../datos/ml-100k/u.item"
"""
def obtenNombres():
    nombre_peliculas = {}
    with open("../datos/ml-100k/u.item") as f:
        for linea in f:
            campos = linea.split('|')
            # Se generan los pares clave/valor del dicionario {movieID: movieName}
            nombre_peliculas[int(campos[0])] = campos[1]
    return nombre_peliculas

"""
    Se realiza la configuracion de Spark, de manera local
    se configura para que sea de manera local y se le asigna un nombre
    se la pasa la configuracion realizada al contexto de Spark
    en setMaster se le pueden pasar los nucleos a ejecutar
    esto depende de los nucleos de la maquina local 
    con local[n] siendo n el numero de nucleos a usar
"""
conf = SparkConf().setMaster("local").setAppName("PeliculaPopularNombre")
sc = SparkContext(conf = conf)

"""
    Se crea un nuevo diccionario de datos, con la funcion broadcast
    sc.broadcast(): se pone el nombre de la funcion creada loadMovieName()
    que ayudara a obtener el nombre de las peliculas por su ID
"""
dic_nombres = sc.broadcast(obtenNombres())

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
cuenta_pelicula = peliculas.reduceByKey(lambda x, y: x + y)

"""
    Se invertira el par resultante clave/valor a valor/clave
    de conteo/movieID se modifica como movieID/conteo
    con la funcion lambda, ademas se ordenan las 
    ocurrencias de las peliculas con la funcion
    sortByKey() por la nueva clave movieID
"""
invierte_par = cuenta_pelicula.map(lambda xy: (xy[1], xy[0]))
# Por default sortByKey orden en orden ascendente
peliculas_ordenadas = invierte_par.sortByKey()
# Si se quiere ordenar en orden descendente se agrega False a sortByKey
#peliculas_ordenadas = invierte_par.sortByKey(False)

"""
    Se tiene un mapeo que toma cada par clave/valor
    el mapeo map() reemplazara con el diccionario
    dic_nombres = sc.broadcast(loadMovieName())
    que creamos usando broadcast la columna movieID
    por el movieName
    Se pueda hacer esto en map porque la funcion
    la cual estamos llamando con la funcion lambda
    como dic_nombres.value[countMovie[1]]
    para complementar la informacion con el valor
    obtenido como movieName: clave/valor - movieID/movieName
"""
nombres_ordenados_peliculas = peliculas_ordenadas.map(lambda countMovie : (dic_nombres.value[countMovie[1]], countMovie[0]))
resultados = nombres_ordenados_peliculas.collect()

# Se imprime la lista con el nombre de las peliculas y su popularidad
print("La ocurrencia de las peliculas es la siguiente: ")
print("Conteo\tID de Pelicula")
for resultado in resultados:
    print(resultado)
