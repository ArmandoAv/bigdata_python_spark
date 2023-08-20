"""
    Obtener las peliculas similares de una pelicula
    Con base en los ratings y similitudes
    Asi como las vistas de peliculas por los usuarios

    Se le deben de pasar un argumento al programa
    movieID, por ejemplo
    15_Similitudes_Peliculas.py 1

    El movieID que se usuara de ejemplo sera
    Star Wars (1977)
    movieID: 50

    Del dataset u.data bajado de grouplens.org
    Recordar que las columnas del archivo son
    Persona Pelicula Rating	Usuario
    196 242 3 81250949
    186 302 3 891717742
    Ademas del dataset u.item
    Se obtendra el nombre de la pelicula
"""

# Importamos las librerias de Spark, de matematicas y de sistema
import sys
from pyspark import SparkConf
from pyspark import SparkContext
from math import sqrt

"""
    Se crea una funcion que obtiene el nombre de la pelicula
    Con un diccionario vacio llamado nombre_peliculas
    Se abre el archivo con el nombre de las peliculas u.item
    Separamos el archivo por pipe '|'
    Extraemos el movieID que esta como entero (int)
    Asignamos el movieID con su respectivo movieName
    Para crear el par de clave/valor necesario para un diccionario
    Que se encuentra en el segundo campo del archivo

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
    Se crea una funcion de elimine pares duplicados
    Del par que tenemos
    (userID, ((movieID1, rating1), (movieID2, rating2)))
    Extraemos el valor
    ((movieID1, rating1), (movieID2, rating2))
    Separandolos por el primero y el segundo elemento
    (movieID1, rating1) y (movieID2, rating2)
    Con eso validamos si una pelicula esta duplicada
    Devolviendo la misma estructura pero sin
    Peliculas duplicadas
    (userID, ((movieID1, rating1), (movieID2, rating2)))
    Esto es porque se filtra por la clave
    (CLAVE/((clave/valor)/(clave/valor)))
    (USERID, ((movieID1, rating1), (movieID2, rating2)))
"""
def filtraDuplicados(usuario_rating):
    ratings = usuario_rating[1]
    (pelicula1, rating1) = ratings[0]
    (pelicula2, rating2) = ratings[1]
    return pelicula1 < pelicula2

"""
    Se define una funcion que cree pares de peliculas
    Y pares de los ratings
    Por lo que de la estructura original
    (userID, ((movieID1, rating1), (movieID2, rating2)))
    Genera una nueva estructura
    (((movieID1, movieID2), (rating1, rating2))
    Esta funcion es importante porque se obtendra
    La relacion del par de la pelicula evaluada 
    Con las demas peliculas con su respectivo par 
    De ratings otorgados por los usuarios
"""
def creaPares(usuario_rating):
    ratings = usuario_rating[1]
    (pelicula1, rating1) = ratings[0]
    (pelicula2, rating2) = ratings[1]
    return ((pelicula1, pelicula2), (rating1, rating2))

"""
    Se defina una funcion que obtenga la similitud
    de cada par de peliculas

    Se hace por medio del siguiente algoritmo

    1. Se Multiplican los ratings de la misma posicion
       (rating1, rating2), (rating1, rating2)
       rating1 * rating1
       rating2 * rating2

       Se multiplican los ratings de diferente posicion
       (rating1, rating2), (rating1, rating2)
       rating1 * rating2

       Se va contando cada evento que suceda con
       el mismo par de peliculas

    2. Al resultado de cada multiplicacion de
       los ratings de la misma posicion se les
       aplica una raiz cuadrada y el resultado
       de las raices se mutiplican entre si
       los ratings de la misma posicion se les
       sqrt(rating1 * rating1) * sqrt(rating2 * rating2)
       A este resultado sera un denominador

    3. El resultado de la mutiplicacion de los
       ratings de diferente posicion es dividido
       por el denominador obtenido el otro paso

    La funcion devuelve ademas del par de peliculas
    el resultado obtenido en el paso 3 asi como el
    resultado final del conteo de cada evento para
    el mismo par de peliculas
"""
def generaSimilitud(par_rating):
    # Se inicializan las variables a 0
    cuenta_par = 0
    sum_xx = sum_yy = sum_xy = 0
    for ratingX, ratingY in par_rating:
        sum_xx += ratingX * ratingX
        sum_yy += ratingY * ratingY
        sum_xy += ratingX * ratingY
        cuenta_par += 1

    numerador = sum_xy
    denominador = sqrt(sum_xx) * sqrt(sum_yy)

    resultado = 0
    if (denominador):
        resultado = (numerador / (float(denominador)))

    return (resultado, cuenta_par)

"""
    Se realiza la configuracion de Spark, de manera local
    se configura para que sea de manera local y se le asigna un nombre
    se la pasa la configuracion realizada al contexto de Spark
    en setMaster se le pueden pasar los nucleos a ejecutar
    por los calculos que debe realizar se asingnan
    todos los recuresos del CPU con la opcion local[*]
"""
conf = SparkConf().setMaster("local[*]").setAppName("SimilitudesPeliculas")
sc = SparkContext(conf = conf)

"""
    Se manda a llamar a la funcion obtenNombres()
    que crea el RDD con los nombres de las peliculas
"""
print("\nCargando nombres de pelicuas...")
nombre_dicc = obtenNombres()

"""
    Se crea el RDD con los datos procesados a partir del archivo original
    separamos los campos del archivo con el caracter de espacio como separador
    con la funcion lambda se pone el formato como pares
    (clave/valor)
    (clave/(clave/valor))
    (userID, (movieID, rating)
	
    La ruta en textFile puede ser de dos maneras
    Con la ruta absoluta "file:///Users/...../bigdata_python_spark/datos/ml-100k/u.data"
    Con la ruta relativa "../datos/ml-100k/u.data"
"""
datos = sc.textFile("../datos/ml-100k/u.data")
ratings = datos.map(lambda l: l.split()).map(lambda l: (int(l[0]), (int(l[1]), float(l[2]))))

"""
    Se hace un self-join para encontrar todas las combinaciones
    de las peliculas calificadas por el mismo usuario por la
    clave en este caso userID

    Esta funcion requiere mucho CPU porque hace relaciones factoriales
    Matematicamente
    1! = 1
    2! = (1)(2) = 2
    3! =  2!(3) = 6
    4! =  3!(4) = 24

    n! = (n-1)!(n)

    Esto devuelve un RDD con la estructura
    (clave/((clave/valor)/(clave/valor)))
    (userID, ((movieID1, rating1), (movieID2, rating2)))
"""
unir_ratings = ratings.join(ratings)

"""
    Debido a que el DDR contiene todas las combinaciones posibles
    hay varias combinaciones duplicadas, por lo que se necesita
    filtrar los pares duplicados con la funcion filtraDuplicados()
"""
ratings_unicos = unir_ratings.filter(filtraDuplicados)

"""
    Ahora que ya no hay registros duplicados
	se crean pares de peliculas y de ratings
	con la funcion map() se cambia la estructura del RDD
	((movieID1, movieID2), (rating1, rating2))
"""
pares_peliculas = ratings_unicos.map(creaPares)

"""
    Ahora aplicamos al RDD la funcion groupBy Key()
    para juntar los pares de peliculas con todos
    sus respectivos pares de ratings

    Es decir, de una estructura
    ((pelicula1, pelicula2), (rating11, rating21))
    ((pelicula1, pelicula2), (rating12, rating22))

    Se agrupan los ratings de la siguiente manera
    ((pelicula1, pelicula2), ((rating11, rating21), (rating12, rating22), ...))
"""
pares_ratings = pares_peliculas.groupByKey()

"""
    Se manda a llamar la funcion que obtenga las
    similitudes de cada par de peliculas
"""
peliculas_similitudes = pares_ratings.mapValues(generaSimilitud).cache()

# Si se desea guardar los resultados en un archivo descomentar
#moviePairSorted = peliculas_similitudes.sortByKey()
# Guarda los resultados en la carpeta asiganada con el nombre part-00000
#moviePairSorted.coalesce(1).saveAsTextFile("../salidas/peliculas_recomendadas")

# Extract similarities for the movie we care about that are "good".
"""
    Debido a que tenemos las similitudes de todas las peliculas
    se le pasa un ID de pelicula al momento de ser ejecutado
    esto es para obtener las similitudes de una pelicula en 
    particular y poder hacer sus recomendaciones

    Si no se pasa el IDs al ejecutar el programa mandara el
    siguiente error
    pelicula_ID = int(sys.argv[1])
    IndexError: list index out of range

    Con la funcion argv obtenemos todos los argumentos que
    se le pasan al ejecutar un programa incluyendo el nombre
    del programa por lo que el valor de sys.argv[0] en este
    caso es: 15_Similitudes_Peliculas.py
"""
if (len(sys.argv) > 1):

    puntuacion_umbral = 0.97
    ocurrencia_umbral = 50

    pelicula_ID = int(sys.argv[1])

    # Las recomendaciones de las peliculas se haran con los siguientes parametros
    # si la similitud es mayor al 97% (0.97) y si por lo menos a sido rankeada
    # por lo menos por 50 usuarios, para lograr buenas recomendaciones
    resultados_filtrados = peliculas_similitudes.filter(lambda par_similitud: \
        (par_similitud[0][0] == pelicula_ID or par_similitud[0][1] == pelicula_ID) \
        and par_similitud[1][0] > puntuacion_umbral and par_similitud[1][1] > ocurrencia_umbral)

    # Se ordenan los resultados por el mejor score obtenido
	# se filtran solo las mejores 10 peliculas rankeadas
    resultados = resultados_filtrados.map(lambda par_similitud: (par_similitud[1], par_similitud[0])).sortByKey(False).take(10)

    # El ciclo for muestra las peliculas recomendadas
    # con el movieID se obtiene el nombre de la pelicula
    # debido a que los nombres de las peliculas estan
    # contenidas en un diccionario con la estructura
    # clave: valor
    # movieID: movieName
    print("\nPeliculas similares a " + nombre_dicc[pelicula_ID] + "\n")
    for resultado in resultados:
        (sim, pair) = resultado
        # Muestra las recomendaciones para la pelicula vista
        similarpelicula_ID = pair[0]
        if (similarpelicula_ID == pelicula_ID):
            similarpelicula_ID = pair[1]
        print(nombre_dicc[similarpelicula_ID] + "\tsimilitud: " + str(sim[0]) + "\tvistas por usuarios: " + str(sim[1]))
