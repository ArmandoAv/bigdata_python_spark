"""
    Obtener a los superherores mas y menos populares de
    Marvel se obtendra un listado de los 10 superheroes
    con mayores y menores apariciones con otros superheroes

    Se ocupan 2 sets de datos
    Marvel-Graph.txt
    empieza con el ID de superheroe a revisar
    seguido con una lista todos los ID de superheroes
    que han aparecido con el, por ejemplo
    271 4935 5716 4309 3829 5794 3405 4929 1449 2940
    3519 4704 2460 763 1602 5306 5358 6121

    Marvel-Names.txt
    Vienen dos columnas el ID y el Nombre del superheroe
    1 "24-HOUR MAN/EMMANUEL"
    2 "3-D MAN/CHARLES CHAN"

    No se ocupara la funcion broadcast para ver otra
    alternativa de cruzar informacion entre RDDs
"""

# Importamos las librerias de Spark
from pyspark import SparkConf
from pyspark import SparkContext

"""
    Se realiza la configuracion de Spark, de manera local
    se configura para que sea de manera local y se le asigna un nombre
    se la pasa la configuracion realizada al contexto de Spark
    en setMaster se le pueden pasar los nucleos a ejecutar
    esto depende de los nucleos de la maquina local 
    con local[n] siendo n el numero de nucleos a usar
"""
conf = SparkConf().setMaster("local").setAppName("PopularidadHeroes")
sc = SparkContext(conf = conf)


"""
    Se crea una funcion que separa las lineas
    en listas por el caracter de espacio y
    devuelve el primer elemento ademas de
    cuantos elementos hay despues del primero
"""
def cuentaOcurrencia(linea):
    elementos = linea.split()
    return (int(elementos[0]), len(elementos) - 1)

"""
    Se crea una funcion que separa las lineas
    en listas por el caracter de comillas dobles (")
    debido a que comillas es un caracter especial
    para poder usarlo se usa \"  
    La funcion devuelve el primer y segundo elemento
    para el segundo elemento se puede usar la funcion
    encode() es para indicar el tipo de codificacion
"""
def parseaNombre(linea):
    campos = linea.split('\"')
    return (int(campos[0]), campos[1])
    #return (int(campos[0]), campos[1].encode("utf8"))

"""
    Se crean los dos RDD con los datos a procesar
    se usan las funciones creadas para darles formato

    La ruta en textFile puede ser de dos maneras
    Con la ruta absoluta "file:///Users/...../bigdata_python_spark/datos/nombre_arch.txt"
    Con la ruta relativa "../datos/nombre_arch.txt"
"""
nombres = sc.textFile("../datos/marvel-names.txt")
nombre_RDD = nombres.map(parseaNombre)

lineas = sc.textFile("../datos/marvel-graph.txt")
popular = lineas.map(cuentaOcurrencia)

"""
    Se busca el nombre del ganador y se muestra
    Si el set tuviera alguna reundancia se elimina
    Con la funcion reduceByKey() y la primer funcion lambda
    Se invertira el mapeo del DDR
    clave/valor a valor/clave
    heroeID/num_ocurrencias a num_ocurrencias/heroeID
    Con la funcion map() y la segunda funcion lambda
    Se encuentran las mayores y menores ocurrencias
    Con las funciones sortByKey() y take()
    Si se usa top se obtienen los valores mas grandes
    Sin importar como se ordenen
"""
totales_por_heros = popular.reduceByKey(lambda x, y : x + y)
invierte_par = totales_por_heros.map(lambda xy: (xy[1], xy[0]))

# Se ordena en orden descendente para los mas populares
mas_popular = invierte_par.sortByKey(False).take(10)
# Se ordena en orden ascendente para los menos populares
menos_popular = invierte_par.sortByKey().take(10)

"""
    Se imprimen los nombres de los superheroes con sus apariciones
    los 10 mas populares y los 10 menos populares

    Debido a que son varios superheroes y que las variables
    mas_popular y menusPopular tienen una lista de pares
    no es posible usar directamente en ellos la funcion lookup
    por lo que primero se va obteniendo cada par de la lista
    con ayuda del ciclo for, buscando de cada par el heroeID
    para obtener de la variable de nombre_RDD el nombre del
    superheroe en cada iteracion con la funcion lookup()

"""
print("Los heroes mas populares son los siguientes: \n")
mas_populares_nombres = range(len(mas_popular))
for nombres in mas_populares_nombres:
    par_unico_mas = mas_popular[nombres]
    mas_popular_nombre = nombre_RDD.lookup(par_unico_mas[1])[0]
    print(str(mas_popular_nombre) + " con " + str(par_unico_mas[0]) + " apariciones con otros superherores.")

menos_populares_nombres = range(len(menos_popular))
print("\nLos heroes menos populares son los siguientes: \n")
for nombres in menos_populares_nombres:
    par_unico_menos = menos_popular[nombres]
    menos_popular_nombre = nombre_RDD.lookup(par_unico_menos[1])[0]
    print(str(menos_popular_nombre) + " con " + str(par_unico_menos[0]) + " apariciones con otros superherores.")
