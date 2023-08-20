"""
    Obtener las recomendaciones de peliculas
    con base en mis gustos
    
    Por lo que se agregara al archivo u.data
    las siguientes lineas
    0 50 5 881250949
    0 172 5 881250949
    0 133 1 881250949
    Creando al usuario cero con "mis gustos"

    Se le deben de pasar un argumento al programa
    el userID creado anteriormente
    16_Recomendaciones_Peliculas.py 0

    Se obtendra el nombre de la pelicula
    del dataset u.item
    Se obtendra la descripcion del usuario
    del dataset u.user

    Se agrega la siguiente linea al archivo u.user
    0|10|M|Bart|09876
    Para obtener el nombre del nuevo usuario creado
"""

# Importamos las librerias de Spark y de sistema
import sys
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.mllib.recommendation import ALS
from pyspark.mllib.recommendation import Rating

"""
    Se crea una funcion que obtiene el nombre de la pelicula
    con un diccionario vacio llamado nombre_peliculas
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
    Se crea una funcion que obtiene el la descripcion del usuario
    se crea un diccionario vacio llamado nombre_usuarios
    se abre el archivo con el nombre de los usuarios u.user
    separamos el archivo por pipe '|'
    extraemos el userID que esta como entero (int)
    asignamos el userID con su respectivo userName
    para crear el par de clave/valor necesario para un diccionario
    que se encuentra en el cuarto campo del archivo

    La ruta del archivo en open() puede ser de dos maneras
    Con la ruta absoluta "C:/Users/...../bigdata_python_spark/datos/ml-100k/u.user"
    Con la ruta relativa "../datos/ml-100k/u.user"
"""
def obtenUsuarios():
    nombre_usuarios = {}
    with open("../datos/ml-100k/u.user") as f:
        for linea in f:
            campos = linea.split('|')
			# Se generan los pares clave/valor del dicionario {movieID: movieName}
            nombre_usuarios[int(campos[0])] = campos[3]
    return nombre_usuarios

"""
    Se realiza la configuracion de Spark, de manera local
    se configura para que sea de manera local y se le asigna un nombre
    se la pasa la configuracion realizada al contexto de Spark
    en setMaster se le pueden pasar los nucleos a ejecutar
    por los calculos que debe realizar se asingnan
    todos los recuresos del CPU con la opcion local[*]
    se pone un checkpoint del directorio, si no se pone
    una ruta, el directorio se crea en la misma ruta donde
    se esta ejecutando el programa con el nombre que se le
    indica, este direcorio creado contiene algunas particiones
"""
conf = SparkConf().setMaster("local[*]").setAppName("PeliculasRecomendacionesALS")
sc = SparkContext(conf = conf)
sc.setCheckpointDir('../salidas/checkpoint')

"""
    Se manda a llamar a la funcion obtenNombres()
    que crea el RDD con los nombres de las peliculas
"""
print("\nCargando nombres de peliculas...")
nombre_dicc = obtenNombres()

"""
    Se manda a llamar a la funcion obtenUsuarios()
    que crea el RDD con los nombres de las peliculas
"""
print("Cargando nombres de usuarios...")
usuario_dicc = obtenUsuarios()

"""
    Se crea el RDD con los datos procesados a partir del archivo original
    separamos los campos del archivo con el caracter de espacio como separador
    con la funcion lambda se pone el formato
    (userID, movieID, rating)
    se pone el RDD en memoria con la funcion cache()
	
    La ruta en textFile puede ser de dos maneras
    Con la ruta absoluta "file:///Users/...../bigdata_python_spark/datos/ml-100k/u.data"
    Con la ruta relativa "../datos/ml-100k/u.data"
"""
datos = sc.textFile("../datos/ml-100k/u.data")
ratings = datos.map(lambda l: l.split()).map(lambda l: Rating(int(l[0]), int(l[1]), float(l[2]))).cache()

"""
    Comienza el entrenamiento del modelo con ayuda
    del algoritmo ALS y la funcion train() se le
    dice al modelo que se entrene basado en los
    datos de los ratings

    El modelo realizara 6 iteraciones y las
    peliculas seran rankeadas en un top 10

"""
print("\nEntrenado el modelo de recomendaciones...")
rank = 10
num_iteraciones = 6
modelo = ALS.train(ratings, rank, num_iteraciones)

usuario_ID = int(sys.argv[1])

# Obtiene las recomendaciones del usuario
print("\nRatings del usuario " + usuario_dicc[usuario_ID] + ":\n")
usuario_ratings = ratings.filter(lambda l: l[0] == usuario_ID)
for rating in usuario_ratings.collect():
    print(nombre_dicc[int(rating[1])] + ": " + str(rating[2]))

# Da las recomendaciones para el usuario
print("\nMejores recomendaciones para el usuario " + usuario_dicc[usuario_ID] + ":\n")
recomendaciones = modelo.recommendProducts(usuario_ID, 10)
for recomendacion in recomendaciones:
    print (nombre_dicc[int(recomendacion[1])] + \
        " score " + str(recomendacion[2]))
